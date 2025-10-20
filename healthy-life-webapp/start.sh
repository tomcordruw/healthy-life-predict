#!/bin/bash

# Life Expectancy Predictor - Quick Start Script

set -e

echo "=========================================="
echo "🏥 Life Expectancy Predictor"
echo "=========================================="
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Docker and Docker Compose are installed"
echo ""

# Ask user which mode to run
echo "Select deployment mode:"
echo "  1) Production (optimized, port 80)"
echo "  2) Development (hot reload, port 5173)"
echo ""
read -p "Enter choice [1-2]: " choice

case $choice in
    1)
        echo ""
        echo "🚀 Starting in PRODUCTION mode..."
        echo ""
        
        # Build and start production
        echo "📦 Building containers..."
        docker compose build
        
        echo ""
        echo "🚀 Starting services..."
        docker compose up -d

        echo ""
        echo "✅ Application started successfully!"
        echo ""
        echo "🌐 Frontend: http://localhost"
        echo "🔧 Backend API: http://localhost:5000"
        echo ""
        echo "📊 View logs: docker-compose logs -f"
        echo "🛑 Stop: docker-compose down"
        ;;
    2)
        echo ""
        echo "🔧 Starting in DEVELOPMENT mode..."
        echo ""
        
        # Build and start development
        echo "📦 Building containers..."
        docker compose -f docker-compose.dev.yml build
        
        echo ""
        echo "🚀 Starting services..."
        docker compose -f docker-compose.dev.yml up -d

        echo ""
        echo "✅ Development environment started!"
        echo ""
        echo "🌐 Frontend: http://localhost:5173"
        echo "🔧 Backend API: http://localhost:5000"
        echo ""
        echo "📊 View logs: docker-compose -f docker-compose.dev.yml logs -f"
        echo "🛑 Stop: docker-compose -f docker-compose.dev.yml down"
        ;;
    *)
        echo "❌ Invalid choice. Exiting."
        exit 1
        ;;
esac

echo ""
echo "=========================================="
echo "Waiting for services to be ready..."
echo "=========================================="

# Wait for backend to be ready
max_attempts=30
attempt=0
while [ $attempt -lt $max_attempts ]; do
    if curl -s http://localhost:5000/api/health > /dev/null 2>&1; then
        echo "✅ Backend is ready!"
        break
    fi
    attempt=$((attempt + 1))
    echo "⏳ Waiting for backend... ($attempt/$max_attempts)"
    sleep 2
done

if [ $attempt -eq $max_attempts ]; then
    echo "⚠️  Backend did not start in time. Check logs with:"
    echo "   docker compose logs backend"
fi

echo ""
echo "=========================================="
echo "🎉 Setup Complete!"
echo "=========================================="
echo ""
echo "Your Life Expectancy Predictor is now running!"
echo ""
