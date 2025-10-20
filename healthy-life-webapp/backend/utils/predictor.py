"""
Predictor Module
Loads the trained model and makes life expectancy predictions
"""

import pickle
import json
import numpy as np
from typing import Dict, List, Any


class LifeExpectancyPredictor:
    """
    Predicts life expectancy using the trained XGBoost model
    """
    
    def __init__(self, model_dir: str):
        """
        Initialize predictor with model files
        
        Args:
            model_dir: Directory containing model files
        """
        self.model_dir = model_dir
        
        # Load the trained model
        with open(f'{model_dir}/model.pkl', 'rb') as f:
            self.model = pickle.load(f)
        
        # Load the scaler
        with open(f'{model_dir}/scaler.pkl', 'rb') as f:
            self.scaler = pickle.load(f)
        
        # Load feature information
        with open(f'{model_dir}/feature_info.json', 'r', encoding='utf-8') as f:
            self.feature_info = json.load(f)
        
        # Load top features analysis
        with open(f'{model_dir}/top_features.json', 'r', encoding='utf-8') as f:
            self.top_features_data = json.load(f)
        
        self.feature_names = self.feature_info['feature_names']
        self.target_mean = self.feature_info['target_mean']
        self.target_std = self.feature_info['target_std']
    
    def predict(self, features: List[float]) -> float:
        """
        Predict life expectancy from feature values
        
        Args:
            features: List of feature values in correct order
            
        Returns:
            Predicted life expectancy in years
        """
        # Convert to numpy array and reshape
        features_array = np.array(features).reshape(1, -1)
        
        # Scale features
        features_scaled = self.scaler.transform(features_array)
        
        # Make prediction
        prediction = self.model.predict(features_scaled)[0]
        
        return float(prediction)
    
    def get_feature_contributions(self, features: List[float], 
                                  user_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Calculate how each top feature contributes to the prediction
        
        Args:
            features: Feature values used for prediction
            user_data: Original user input data
            
        Returns:
            List of top 10 factors with their impact
        """
        contributions = []
        
        # Get top 10 features from analysis
        top_features = self.top_features_data['top_features'][:10]
        
        # Feature name to user-friendly name mapping
        friendly_names = {
            '1. EARNED INCOME, mean': 'Income Level',
            'disability_ratio': 'Health Conditions',
            'Disposable cash income,  median': 'Financial Security',
            'alcohol_sales': 'Alcohol Consumption',
            'Share of persons aged 15 or over with tertiary level qualification, %': 'Education Level',
            'daily_smokers': 'Smoking Habits',
            'binge_drinking': 'Heavy Drinking',
            'Average age, both sexes': 'Current Age',
            'Dwelling population, persons': 'Community Size',
            'health_workers_per_10k_public_physicians': 'Healthcare Access'
        }
        
        # Personalized messages based on feature values
        for feature_data in top_features:
            feature_name = feature_data['Feature']
            importance = feature_data['Importance']
            correlation = feature_data['Correlation']
            effect = feature_data['Effect']
            
            # Get the feature value
            feature_idx = self.feature_names.index(feature_name)
            feature_value = features[feature_idx]
            
            # Get median value for comparison
            median_value = self.feature_info['feature_medians'][feature_name]
            
            # Determine if user's value is better or worse than median
            if correlation > 0:
                # Positive correlation: higher is better
                is_favorable = feature_value > median_value
                impact_direction = 'positive' if is_favorable else 'negative'
            else:
                # Negative correlation: lower is better
                is_favorable = feature_value < median_value
                impact_direction = 'positive' if is_favorable else 'negative'
            
            # Calculate relative difference from median
            if median_value != 0:
                pct_diff = ((feature_value - median_value) / abs(median_value)) * 100
            else:
                pct_diff = 0
            
            # Create personalized message
            message = self._create_message(feature_name, feature_value, median_value, 
                                          correlation, is_favorable, user_data)
            
            # Add to contributions
            contribution = {
                'feature': friendly_names.get(feature_name, feature_name),
                'raw_feature_name': feature_name,
                'importance': round(importance, 4),
                'correlation': round(correlation, 4),
                'effect': effect,
                'impact_direction': impact_direction,
                'your_value': round(feature_value, 2),
                'average_value': round(median_value, 2),
                'percentage_difference': round(pct_diff, 1),
                'message': message,
                'is_favorable': is_favorable
            }
            
            contributions.append(contribution)
        
        return contributions
    
    def _create_message(self, feature_name: str, value: float, _median: float,
                       _correlation: float, is_favorable: bool, 
                       _user_data: Dict[str, Any]) -> str:
        """
        Create personalized message for each feature
        """
        messages = {
            '1. EARNED INCOME, mean': {
                True: f"Your income level (€{value:,.0f}) is above average and positively impacts your life expectancy.",
                False: f"Your income level (€{value:,.0f}) is below average. Improving financial stability can support better health outcomes."
            },
            'disability_ratio': {
                True: "You have few or no chronic health conditions, which is excellent for longevity.",
                False: "Managing chronic conditions through regular medical care can help improve life expectancy."
            },
            'alcohol_sales': {
                True: "Your moderate alcohol consumption is a positive factor for health.",
                False: "High alcohol consumption can negatively impact health. Consider reducing intake."
            },
            'daily_smokers': {
                True: "Not smoking or low smoking exposure is one of the best things for your health!",
                False: "Smoking significantly reduces life expectancy. Quitting is the single best thing you can do."
            },
            'Share of persons aged 15 or over with tertiary level qualification, %': {
                True: "Higher education levels are associated with better health awareness and outcomes.",
                False: "Continuous learning and health education can help improve wellness regardless of formal education."
            },
            'binge_drinking': {
                True: "Avoiding excessive drinking episodes supports better long-term health.",
                False: "Binge drinking can have serious health consequences. Moderation is key."
            },
            'physical_activity': {
                True: "Your regular physical activity is excellent for longevity!",
                False: "Increasing physical activity to at least 150 minutes per week can add years to your life."
            },
            'mental_health': {
                True: "Good mental well-being significantly contributes to overall health and longevity.",
                False: "Mental health is crucial. Consider seeking support or practicing stress-management techniques."
            },
            'percentage_happy': {
                True: "Your positive outlook and happiness contribute to better health outcomes!",
                False: "Life satisfaction matters for health. Small daily practices can help improve well-being."
            }
        }
        
        # Get the appropriate message or create a default
        if feature_name in messages:
            return messages[feature_name][is_favorable]
        
        if is_favorable:
            return "This factor is in a favorable range for life expectancy."
        
        return "This factor could be improved to positively impact life expectancy."

