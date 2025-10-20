# Life Expectancy Prediction - Web Application

A modern web application that predicts life expectancy based on lifestyle and health factors using machine learning.

## 🚀 Quick Start

### Option 1: Docker (Recommended) 🐳

**Prerequisites**: Docker and Docker Compose

```bash
# Build and start the application
docker-compose up -d

```

Visit:
- **Frontend**: http://localhost
- **Backend API**: http://localhost:5000

### Option 2: Manual Setup

**Prerequisites**: Python 3.8+, Node.js 18+, npm

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Start the Flask server:
```bash
python app.py
```

The API will run on `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The app will run on `http://localhost:5173`

## 📁 Project Structure

```
healthy-life-webapp/
├── backend/                  # Flask API
│   ├── app.py               # Main Flask application
│   ├── requirements.txt     # Python dependencies
│   ├── model/              # Trained ML model files
│   │   ├── model.pkl
│   │   ├── scaler.pkl
│   │   ├── feature_info.json
│   │   └── top_features.json
│   └── utils/              # Utility modules
│       ├── converter.py    # Feature conversion
│       └── predictor.py    # Prediction logic
│
└── frontend/               # React + TypeScript
    ├── src/
    │   ├── components/    # React components
    │   │   ├── Welcome.tsx
    │   │   ├── QuestionForm.tsx
    │   │   └── ResultDisplay.tsx
    │   ├── services/      # API service
    │   │   └── api.ts
    │   ├── types/         # TypeScript types
    │   │   └── index.ts
    │   ├── App.tsx        # Main app component
    │   └── main.tsx       # Entry point
    ├── package.json
    └── tailwind.config.js
```

## 🎯 Features

- **Interactive Questionnaire**: 10 simple questions about lifestyle and health
- **Real-time Prediction**: Instant life expectancy calculation using XGBoost ML model
- **Visual Results**: Beautiful charts and cards showing predicted life expectancy
- **Top 10 Factors**: Identifies which factors positively or negatively impact your life expectancy
- **Personalized Recommendations**: Actionable advice to improve health outcomes
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices

## 🛠️ Technology Stack

### Backend
- **Flask**: Lightweight Python web framework
- **XGBoost**: Machine learning model for predictions
- **scikit-learn**: Data preprocessing and scaling
- **Flask-CORS**: Cross-origin resource sharing

### Frontend
- **React 18**: UI library
- **TypeScript**: Type-safe JavaScript
- **Vite**: Fast build tool and dev server
- **Tailwind CSS**: Utility-first CSS framework
- **Axios**: HTTP client for API calls
- **Recharts**: Data visualization library

## 📊 How It Works

1. **User Input**: User answers 10 questions about their lifestyle, health, and demographics
2. **Feature Conversion**: Responses are converted to 34 model features using population statistics
3. **ML Prediction**: XGBoost model predicts life expectancy based on features
4. **Factor Analysis**: Top 10 influential factors are identified and explained
5. **Results Display**: User sees their predicted life expectancy, comparison to average, and personalized recommendations

## 🔒 Privacy

- All data is processed in real-time
- No personal information is stored on servers
- Calculations happen locally or in temporary API calls
- No tracking or analytics

## 🚦 API Endpoints

- `GET /` - API information
- `GET /api/health` - Health check
- `GET /api/questions` - Get questionnaire questions
- `POST /api/predict` - Submit data and get prediction

## 🧪 Development

### Run Backend in Development Mode
```bash
cd backend
export FLASK_ENV=development
python app.py
```

### Run Frontend in Development Mode
```bash
cd frontend
npm run dev
```

### Build Frontend for Production
```bash
cd frontend
npm run build
```