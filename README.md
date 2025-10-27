# Life Expectancy Prediction Project

Project live at: https://healthy-life-webapp.azurewebsites.net/

A machine learning project that predicts life expectancy based on Finnish regional health and demographic data (2013-2021).

## Project Overview

This project uses XGBoost machine learning to predict life expectancy based on lifestyle, health, and socioeconomic factors. It includes:

1. **Data Analysis Pipeline** - Jupyter notebooks for data processing and model training
2. **Web Application** - Full-stack web app for interactive predictions
3. **ML Model** - Trained XGBoost model with 34 features

## Project Structure

```
healthy-life/
├── healthy-life-webapp/    # Production Web Application
│   ├── backend/            # Flask API + ML model
│   ├── frontend/           # React + TypeScript UI
│   └── README.md           # Full webapp documentation
│
├── notebooks/              # Data Science & Development
│   ├── analysis.ipynb      # Model training & evaluation
│   ├── data_processing.ipynb
│   └── import_data.ipynb
│
└── regional_data/          # Raw Data Sources
    ├── thl/                # Finnish Institute for Health and Welfare
    └── tilastokeskus/      # Statistics Finland
```

## Quick Start

### Option 1: Run the Web Application (Recommended)

```bash
cd healthy-life-webapp
docker-compose up -d
```

Visit **http://localhost** to use the application.

👉 **See [healthy-life-webapp/README.md](healthy-life-webapp/README.md) for full documentation.**

### Option 2: Explore the Data Science Notebooks

```bash
# Activate virtual environment
source .venv/bin/activate

# Start Jupyter
cd notebooks
jupyter notebook
```

Open `analysis.ipynb` to see the model training process.

## Data Sources

- **THL (Finnish Institute for Health and Welfare)**: Health indicators, lifestyle factors
- **Statistics Finland (Tilastokeskus)**: Demographics, socioeconomics, education

See `notebooks/data_sources.txt` for direct links.

## Model Details

- **Algorithm**: XGBoost (Extreme Gradient Boosting)
- **Features**: 34 features including income, education, smoking, alcohol, exercise, mental health
- **Target**: Life expectancy (years)
- **Performance**: Trained on regional data from Finnish municipalities (2013-2021)

## Technology Stack

### Web Application
- **Backend**: Flask, Python 3.11, XGBoost, scikit-learn
- **Frontend**: React 18, TypeScript, Vite, Tailwind CSS
- **Deployment**: Docker, Docker Compose, Nginx

### Data Science
- **Analysis**: Jupyter, pandas, numpy, matplotlib, seaborn
- **ML**: XGBoost, scikit-learn
- **Data**: CSV files from Finnish government sources

## Documentation

- **[webapp README](healthy-life-webapp/README.md)** - Web application setup and usage
- **[DOCKER_GUIDE](healthy-life-webapp/DOCKER_GUIDE.md)** - Docker deployment instructions
- **[FEATURE_CONVERSION_GUIDE](healthy-life-webapp/FEATURE_CONVERSION_GUIDE.md)** - Technical explanation of feature engineering

## Important Notes

### Disclaimer
This tool provides **statistical estimates** based on population data and should not be considered medical advice. Individual health outcomes vary significantly based on many factors not captured in this model. Always consult with healthcare professionals for personal health decisions.

### Data Context
The model is trained on **Finnish population data** (2013-2021) and predictions are most accurate for populations with similar demographics and healthcare systems.

### Purpose
This is an **educational project** demonstrating machine learning applications in public health. It aims to raise awareness about factors that influence longevity.



## Links

- **Data Sources**:
  - [THL Sotkanet](https://sotkanet.fi/sotkanet/en/haku)
  - [Statistics Finland](https://pxdata.stat.fi/PXWeb/pxweb/en/StatFin/)

---

**Built with Python, React, XGBoost, and data from Finnish health authorities**

For questions or issues, see the documentation in `healthy-life-webapp/` directory.
