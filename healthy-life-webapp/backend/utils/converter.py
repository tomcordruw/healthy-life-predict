"""
Feature Converter Module
Converts user questionnaire responses to model-compatible feature values
"""

from datetime import datetime
from typing import Dict, Any
import json


class FeatureConverter:
    """
    Converts user-friendly questionnaire responses to ML model features
    """
    
    def __init__(self, feature_info_path: str):
        """
        Initialize converter with feature information
        
        Args:
            feature_info_path: Path to feature_info.json file
        """
        with open(feature_info_path, 'r', encoding='utf-8') as f:
            self.feature_info = json.load(f)
        
        self.feature_names = self.feature_info['feature_names']
        self.feature_medians = self.feature_info['feature_medians']
    
    def calculate_age(self, birth_date: str) -> int:
        """
        Calculate age from birth date
        
        Args:
            birth_date: Birth date in format 'YYYY-MM-DD'
            
        Returns:
            Age in years
        """
        birth = datetime.strptime(birth_date, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        return age
    
    def convert_user_input(self, user_data: Dict[str, Any]) -> Dict[str, float]:
        """
        Convert user questionnaire responses to model features
        
        Args:
            user_data: Dictionary containing user responses
                {
                    'birth_date': 'YYYY-MM-DD',
                    'income': float (20000-80000),
                    'education': str ('none', 'high_school', 'bachelor', 'master_plus'),
                    'smoking': str ('never', 'occasional', 'daily'),
                    'alcohol_units': float (0-20),
                    'exercise_days': int (0-7),
                    'chronic_conditions': list of strings,
                    'mental_health_score': int (1-10),
                    'happiness_score': int (1-10),
                    'employment_status': str ('employed', 'unemployed', 'retired', 'student')
                }
        
        Returns:
            Dictionary with all model features
        """
        # Calculate age
        age = self.calculate_age(user_data['birth_date'])
        
        # Education level mapping (percentage with tertiary education)
        education_map = {
            'none': 10.0,
            'high_school': 20.0,
            'bachelor': 35.0,
            'master_plus': 50.0
        }
        
        # Smoking mapping (percentage of daily smokers)
        smoking_map = {
            'never': 5.0,      # Low smoking in population
            'occasional': 12.0, # Medium smoking
            'daily': 25.0       # High smoking
        }
        
        # Initialize features dictionary with medians as defaults
        features = self.feature_medians.copy()
        
        # Map user responses to specific features
        
        # 1. Income-related features (Top importance: 0.614)
        income = user_data.get('income', 35000)
        features['1. EARNED INCOME, mean'] = float(income)
        features['Disposable cash income,  median'] = float(income * 1.15)  # Disposable is typically higher
        
        # 2. Disability ratio (Importance: 0.056) - based on chronic conditions
        chronic_conditions = user_data.get('chronic_conditions', [])
        features['disability_ratio'] = min(len(chronic_conditions) * 3.0, 20.0)  # Scale 0-20%
        
        # 3. Education (Importance: 0.028)
        education = user_data.get('education', 'high_school')
        features['Share of persons aged 15 or over with tertiary level qualification, %'] = education_map.get(education, 25.0)
        
        # Also set the inverse education feature
        tertiary_pct = education_map.get(education, 25.0)
        features['Share of persons aged 15 or over without upper secondary qualification, %, %'] = max(100 - tertiary_pct - 40, 0)
        features['Share of persons aged 15 or over with at least upper secondary qualification, %'] = min(tertiary_pct + 40, 85)
        
        # 4. Smoking (Importance: 0.027)
        smoking = user_data.get('smoking', 'never')
        features['daily_smokers'] = smoking_map.get(smoking, 12.0)
        
        # 5. Alcohol consumption (Importance: 0.035 for sales, 0.018 for binge)
        alcohol_units = user_data.get('alcohol_units', 5.0)
        features['alcohol_sales'] = alcohol_units * 0.5  # Scale to regional sales
        features['binge_drinking'] = min(alcohol_units * 1.5, 25.0)  # Binge drinking percentage
        
        # 6. Physical activity (Importance: 0.0009)
        exercise_days = user_data.get('exercise_days', 2)
        features['physical_activity'] = (exercise_days / 7.0) * 40  # Convert to percentage (0-40%)
        
        # 7. Mental health (Importance: 0.003 for mental_health, 0.002 for severe_mental_strain)
        mental_health_score = user_data.get('mental_health_score', 5)
        # Higher user score = better mental health, but model feature has negative correlation
        # So we inverse it: 10-score gives us the "mental strain" level
        features['mental_health'] = (11 - mental_health_score) * 15  # Scale to 15-150
        features['severe_mental_strain'] = (11 - mental_health_score) * 2  # Scale to 2-20%
        
        # 8. Happiness (Importance: 0.004)
        happiness_score = user_data.get('happiness_score', 5)
        features['percentage_happy'] = (happiness_score / 10.0) * 80  # Scale to 0-80%
        
        # 9. Work-related features
        employment_status = user_data.get('employment_status', 'employed')
        
        # Estimate years until retirement based on age and employment
        if employment_status == 'retired':
            features['work_until_retired'] = 0
        elif employment_status == 'employed':
            retirement_age = 65
            features['work_until_retired'] = max(retirement_age - age, 0)
        else:
            features['work_until_retired'] = 30  # Default for students/unemployed
        
        # 10. Age-related features
        features['Average age, both sexes'] = float(age)
        features['Average age, men'] = float(age)
        features['Average age, women'] = float(age)
        
        # Additional features that depend on other factors
        
        # Obesity (slight positive correlation, importance: 0.006)
        # Rough estimate based on exercise
        base_obesity = 20.0
        exercise_factor = (7 - exercise_days) * 1.0  # Less exercise = higher obesity
        features['obesity_rate'] = min(base_obesity + exercise_factor, 35.0)
        
        # Population and density features - use medians (not individual-specific)
        # These stay at median values
        
        return features
    
    def get_feature_vector(self, user_data: Dict[str, Any]) -> list:
        """
        Convert user data to ordered feature vector for model prediction
        
        Args:
            user_data: User questionnaire responses
            
        Returns:
            List of feature values in correct order
        """
        features_dict = self.convert_user_input(user_data)
        
        # Ensure all features are present and in correct order
        feature_vector = []
        for feature_name in self.feature_names:
            feature_vector.append(features_dict.get(feature_name, self.feature_medians[feature_name]))
        
        return feature_vector
    
    def get_feature_descriptions(self) -> Dict[str, str]:
        """
        Get human-readable descriptions for each feature
        
        Returns:
            Dictionary mapping feature names to descriptions
        """
        descriptions = {
            '1. EARNED INCOME, mean': 'Annual Income Level',
            'Disposable cash income,  median': 'Available Spending Money',
            'disability_ratio': 'Chronic Health Conditions',
            'alcohol_sales': 'Alcohol Consumption',
            'Share of persons aged 15 or over with tertiary level qualification, %': 'Education Level',
            'daily_smokers': 'Smoking Habits',
            'binge_drinking': 'Heavy Drinking Frequency',
            'Average age, both sexes': 'Age',
            'health_workers_per_10k_public_physicians': 'Healthcare Access',
            'elder_care_per_100k': 'Elder Care Access',
            'work_until_retired': 'Working Years Remaining',
            'obesity_rate': 'Weight and Health',
            'percentage_happy': 'Overall Happiness',
            'mental_health': 'Mental Well-being',
            'severe_mental_strain': 'Stress Levels',
            'physical_activity': 'Exercise and Activity',
            'overcrowded_living': 'Living Conditions',
            'incidence_disability_pension': 'Health Disability Risk'
        }
        return descriptions
