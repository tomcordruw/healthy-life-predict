# Backend API - Life Expectancy Predictor

Flask backend for the Healthy Life web application.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the development server:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### GET /
Home endpoint with API information

### GET /api/health
Health check endpoint

### GET /api/questions
Get questionnaire questions with all options

### POST /api/predict
Make a life expectancy prediction

**Request Body:**
```json
{
  "birth_date": "1990-01-15",
  "income": 45000,
  "education": "bachelor",
  "smoking": "never",
  "alcohol_units": 5,
  "exercise_days": 3,
  "chronic_conditions": ["none"],
  "mental_health_score": 7,
  "happiness_score": 8,
  "employment_status": "employed"
}
```

**Response:**
```json
{
  "predicted_life_expectancy": 82.5,
  "average_life_expectancy": 79.8,
  "difference_from_average": 2.7,
  "percentile": 75.5,
  "user_age": 34,
  "factors": [...],
  "recommendations": [...]
}
```

## Project Structure

```
backend/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── model/                 # Trained model files
│   ├── model.pkl
│   ├── scaler.pkl
│   ├── feature_info.json
│   └── top_features.json
└── utils/                 # Utility modules
    ├── converter.py       # Feature conversion
    └── predictor.py       # Prediction logic
```

## Development

Set environment variable for development mode:
```bash
export FLASK_ENV=development
python app.py
```

## Testing

Test the API with curl:
```bash
# Health check
curl http://localhost:5000/api/health

# Get questions
curl http://localhost:5000/api/questions

# Make prediction
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d @test_data.json
```
