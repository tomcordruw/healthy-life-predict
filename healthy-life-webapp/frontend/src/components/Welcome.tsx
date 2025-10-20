import React from 'react';

interface WelcomeProps {
  onStart: () => void;
}

const Welcome: React.FC<WelcomeProps> = ({ onStart }) => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-primary-50 to-blue-100 px-4">
      <div className="max-w-4xl w-full">
        <div className="card text-center space-y-6">
          {/* Icon */}
          <div className="flex justify-center">
            <div className="w-20 h-20 bg-primary-600 rounded-full flex items-center justify-center">
              <svg className="w-12 h-12 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
          </div>

          {/* Title */}
          <div>
            <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
              Life Expectancy Predictor
            </h1>
            <p className="text-xl text-gray-600">
              Discover your predicted life expectancy based on lifestyle and health factors
            </p>
          </div>

          {/* Features */}
          <div className="grid md:grid-cols-3 gap-6 py-8">
            <div className="space-y-2">
              <div className="text-3xl">🧬</div>
              <h3 className="font-semibold text-gray-900">Science-Based</h3>
              <p className="text-sm text-gray-600">
                Powered by machine learning and real health data
              </p>
            </div>
            <div className="space-y-2">
              <div className="text-3xl">⚡</div>
              <h3 className="font-semibold text-gray-900">Quick & Easy</h3>
              <p className="text-sm text-gray-600">
                Just 10 simple questions
              </p>
            </div>
            <div className="space-y-2">
              <div className="text-3xl">🎯</div>
              <h3 className="font-semibold text-gray-900">Actionable Insights</h3>
              <p className="text-sm text-gray-600">
                Get personalized recommendations to improve your health
              </p>
            </div>
          </div>

          {/* CTA Button */}
          <div className="pt-4">
            <button 
              onClick={onStart}
              className="btn-primary text-lg px-12 py-4 transform hover:scale-105"
            >
              Start Assessment
              <svg className="inline-block ml-2 w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
              </svg>
            </button>
          </div>

          {/* Disclaimer */}
          <div className="text-xs text-gray-500 pt-4">
            <p>
              * This tool provides estimates based on statistical models and should not be considered medical advice.
              Always consult with healthcare professionals for personal health decisions.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Welcome;
