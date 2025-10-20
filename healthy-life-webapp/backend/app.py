"""
Life Expectancy Prediction API
Flask backend for the healthy-life web application
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

# Add utils to path
sys.path.append(os.path.dirname(__file__))

from utils.converter import FeatureConverter
from utils.predictor import LifeExpectancyPredictor

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Initialize model and utilities
MODEL_DIR = os.path.join(os.path.dirname(__file__), 'model')
converter = FeatureConverter(os.path.join(MODEL_DIR, 'feature_info.json'))
predictor = LifeExpectancyPredictor(MODEL_DIR)


@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'Life Expectancy Prediction API',
        'status': 'running',
        'version': '1.0.0'
    })


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': predictor.model is not None,
        'scaler_loaded': predictor.scaler is not None
    })


@app.route('/api/predict', methods=['POST'])
def predict():
    """
    Main prediction endpoint
    
    Expects JSON body with user questionnaire data:
    {
        "birth_date": "YYYY-MM-DD",
        "income": 35000,
        "education": "bachelor",
        "smoking": "never",
        "alcohol_units": 5,
        "exercise_days": 3,
        "chronic_conditions": ["none"],
        "mental_health_score": 7,
        "happiness_score": 8,
        "employment_status": "employed"
    }
    
    Returns:
    {
        "predicted_life_expectancy": 82.5,
        "average_life_expectancy": 79.8,
        "difference_from_average": 2.7,
        "percentile": 75.5,
        "factors": [...],
        "recommendations": [...]
    }
    """
    try:
        # Get user data from request
        user_data = request.get_json()
        
        # Validate required fields
        required_fields = ['birth_date', 'income', 'education', 'smoking', 
                          'alcohol_units', 'exercise_days', 'chronic_conditions',
                          'mental_health_score', 'happiness_score', 'employment_status']
        
        missing_fields = [field for field in required_fields if field not in user_data]
        if missing_fields:
            return jsonify({
                'error': f'Missing required fields: {", ".join(missing_fields)}'
            }), 400
        
        # Convert user input to model features
        feature_vector = converter.get_feature_vector(user_data)
        
        # Make prediction
        predicted_life_expectancy = predictor.predict(feature_vector)
        
        # Calculate statistics
        average_life_expectancy = predictor.target_mean
        difference_from_average = predicted_life_expectancy - average_life_expectancy
        
        # Calculate percentile (simplified)
        # In a real scenario, you'd compare against the full dataset distribution
        std = predictor.target_std
        z_score = difference_from_average / std
        # Rough percentile estimate using standard normal distribution
        if z_score > 0:
            percentile = 50 + (z_score / 3) * 50  # Simplified percentile calculation
        else:
            percentile = 50 - (abs(z_score) / 3) * 50
        percentile = max(1, min(99, percentile))  # Clamp between 1-99
        
        # Get factor contributions
        contributions = predictor.get_feature_contributions(feature_vector, user_data)
        
        # Prepare response
        response = {
            'predicted_life_expectancy': round(predicted_life_expectancy, 1),
            'average_life_expectancy': round(average_life_expectancy, 1),
            'difference_from_average': round(difference_from_average, 1),
            'percentile': round(percentile, 1),
            'factors': contributions,
            'user_age': converter.calculate_age(user_data['birth_date'])
        }
        
        return jsonify(response), 200
    
    except ValueError as e:
        return jsonify({
            'error': str(e),
            'message': 'Invalid input data provided'
        }), 400
    except KeyError as e:
        return jsonify({
            'error': f'Missing required data: {str(e)}',
            'message': 'An error occurred while processing your request'
        }), 400
    except Exception as e:  # pylint: disable=broad-except
        return jsonify({
            'error': str(e),
            'message': 'An unexpected error occurred while processing your request'
        }), 500


@app.route('/api/questions', methods=['GET'])
def get_questions():
    """
    Get the questionnaire questions and options
    
    Returns the structured questions for the frontend
    """
    questions = [
        {
            'id': 'birth_date',
            'question': 'What is your date of birth?',
            'type': 'date',
            'required': True,
            'max_date': '2010-01-01',  # Must be at least 15 years old
            'help_text': 'This helps us calculate age-related factors'
        },
        {
            'id': 'income',
            'question': 'What is your annual income (before taxes)?',
            'type': 'slider',
            'required': True,
            'min': 10000,
            'max': 100000,
            'step': 1000,
            'default': 35000,
            'unit': '€',
            'help_text': 'Income level is associated with access to healthcare and lifestyle choices'
        },
        {
            'id': 'education',
            'question': 'What is your highest level of education?',
            'type': 'radio',
            'required': True,
            'options': [
                {'value': 'none', 'label': 'Less than high school'},
                {'value': 'high_school', 'label': 'High school diploma'},
                {'value': 'bachelor', 'label': "Bachelor's degree"},
                {'value': 'master_plus', 'label': "Master's degree or higher"}
            ],
            'help_text': 'Education correlates with health awareness and outcomes'
        },
        {
            'id': 'smoking',
            'question': 'Do you smoke?',
            'type': 'radio',
            'required': True,
            'options': [
                {'value': 'never', 'label': 'Never / Not currently'},
                {'value': 'occasional', 'label': 'Occasionally'},
                {'value': 'daily', 'label': 'Daily'}
            ],
            'help_text': 'Smoking is one of the biggest factors affecting life expectancy'
        },
        {
            'id': 'alcohol_units',
            'question': 'How many alcoholic drinks do you consume per week?',
            'type': 'slider',
            'required': True,
            'min': 0,
            'max': 30,
            'step': 1,
            'default': 5,
            'unit': 'drinks',
            'help_text': 'One drink = one beer, glass of wine, or shot of spirits'
        },
        {
            'id': 'exercise_days',
            'question': 'How many days per week do you exercise for at least 30 minutes?',
            'type': 'slider',
            'required': True,
            'min': 0,
            'max': 7,
            'step': 1,
            'default': 2,
            'unit': 'days',
            'help_text': 'Regular physical activity significantly impacts health and longevity'
        },
        {
            'id': 'chronic_conditions',
            'question': 'Do you have any of these chronic health conditions?',
            'type': 'checkbox',
            'required': True,
            'options': [
                {'value': 'none', 'label': 'None'},
                {'value': 'diabetes', 'label': 'Diabetes'},
                {'value': 'heart_disease', 'label': 'Heart disease'},
                {'value': 'high_blood_pressure', 'label': 'High blood pressure'},
                {'value': 'respiratory', 'label': 'Chronic respiratory disease'},
                {'value': 'arthritis', 'label': 'Arthritis'},
                {'value': 'cancer', 'label': 'Cancer (past or present)'},
                {'value': 'other', 'label': 'Other chronic condition'}
            ],
            'help_text': 'Select all that apply. Managed conditions can still support long life.'
        },
        {
            'id': 'mental_health_score',
            'question': 'How would you rate your mental and emotional well-being?',
            'type': 'scale',
            'required': True,
            'min': 1,
            'max': 10,
            'min_label': 'Poor',
            'max_label': 'Excellent',
            'default': 5,
            'help_text': 'Mental health is as important as physical health for longevity'
        },
        {
            'id': 'happiness_score',
            'question': 'Overall, how satisfied are you with your life?',
            'type': 'scale',
            'required': True,
            'min': 1,
            'max': 10,
            'min_label': 'Not satisfied',
            'max_label': 'Very satisfied',
            'default': 5,
            'help_text': 'Life satisfaction contributes to better health outcomes'
        },
        {
            'id': 'employment_status',
            'question': 'What is your current employment status?',
            'type': 'radio',
            'required': True,
            'options': [
                {'value': 'employed', 'label': 'Employed (full-time or part-time)'},
                {'value': 'unemployed', 'label': 'Unemployed / Looking for work'},
                {'value': 'retired', 'label': 'Retired'},
                {'value': 'student', 'label': 'Student'}
            ],
            'help_text': 'Employment status relates to routine and social engagement'
        }
    ]
    
    return jsonify({'questions': questions}), 200


if __name__ == '__main__':
    # Run the Flask app
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    print("=" * 60)
    print("🏥 Life Expectancy Prediction API Server")
    print("=" * 60)
    print(f"Server running on: http://localhost:{port}")
    print(f"Debug mode: {debug}")
    print("=" * 60)
    
    app.run(host='0.0.0.0', port=port, debug=debug)
