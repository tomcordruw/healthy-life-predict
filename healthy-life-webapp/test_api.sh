#!/bin/bash

# Test script for the Life Expectancy Prediction Web App

echo "=================================="
echo "🧪 Testing Backend API"
echo "=================================="

# Test 1: Health Check
echo -e "\n1. Testing health check endpoint..."
curl -s http://localhost:5000/api/health | python3 -m json.tool

# Test 2: Questions Endpoint
echo -e "\n\n2. Testing questions endpoint..."
curl -s http://localhost:5000/api/questions | python3 -m json.tool | head -n 20
echo "... (output truncated)"

# Test 3: Prediction Endpoint
echo -e "\n\n3. Testing prediction endpoint..."
curl -s -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
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
  }' | python3 -m json.tool

echo -e "\n\n=================================="
echo "✅ Backend API tests complete!"
echo "=================================="
echo -e "\nIf you see errors, make sure:"
echo "  1. Backend is running (python backend/app.py)"
echo "  2. Port 5000 is available"
echo "  3. All dependencies are installed"
