import React from 'react';
import type { PredictionResponse } from '../types';

interface ResultDisplayProps {
  result: PredictionResponse;
  onRestart: () => void;
}

const ResultDisplay: React.FC<ResultDisplayProps> = ({ result, onRestart }) => {
  const positiveFactors = result.factors.filter(f => f.impact_direction === 'positive');
  const negativeFactors = result.factors.filter(f => f.impact_direction === 'negative');
  const [showExplanation, setShowExplanation] = React.useState(false);

  return (
    <div className="min-h-screen bg-gradient-to-br from-primary-50 to-blue-100 py-12 px-4">
      <div className="max-w-6xl mx-auto space-y-8">
        {/* Main Result Card */}
        <div className="card text-center space-y-6">
          <h1 className="text-3xl md:text-4xl font-bold text-gray-900">
            Your Life Expectancy Prediction
          </h1>
          
          <div className="py-8">
            <div className="inline-block">
              <div className="text-7xl md:text-8xl font-bold text-primary-600">
                {result.predicted_life_expectancy}
              </div>
              <div className="text-2xl text-gray-600 mt-2">years</div>
            </div>
          </div>
          
          <div className="grid md:grid-cols-3 gap-6 text-center">
            <div className="p-4 bg-gray-50 rounded-lg">
              <div className="text-sm text-gray-600 mb-1">Population Average</div>
              <div className="text-3xl font-bold text-gray-800">
                {result.average_life_expectancy}
              </div>
              <div className="text-sm text-gray-600">years</div>
            </div>
            
            <div className="p-4 bg-blue-50 rounded-lg">
              <div className="text-sm text-gray-600 mb-1">Difference</div>
              <div className={`text-3xl font-bold ${
                result.difference_from_average >= 0 ? 'text-green-600' : 'text-red-600'
              }`}>
                {result.difference_from_average >= 0 ? '+' : ''}{result.difference_from_average}
              </div>
              <div className="text-sm text-gray-600">years</div>
            </div>
            
            <div className="p-4 bg-green-50 rounded-lg">
              <div className="text-sm text-gray-600 mb-1">Percentile</div>
              <div className="text-3xl font-bold text-green-600">
                {result.percentile}th
              </div>
              <div className="text-sm text-gray-600">percentile</div>
            </div>
          </div>
        </div>

        {/* Positive Factors */}
        {positiveFactors.length > 0 && (
          <div className="card">
            <h2 className="text-2xl font-bold text-green-700 mb-6 flex items-center">
              Factors Working in Your Favor ({positiveFactors.length})
            </h2>
            <div className="grid md:grid-cols-2 gap-4">
              {positiveFactors.map((factor, index) => (
                <div key={index} className="p-4 bg-green-50 border border-green-200 rounded-lg">
                  <h3 className="font-semibold text-gray-900 mb-2">{factor.feature}</h3>
                  <p className="text-sm text-gray-700">{factor.message}</p>
                  <div className="mt-2 text-xs text-gray-600">
                    Importance: {(factor.importance * 100).toFixed(1)}%
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Negative Factors */}
        {negativeFactors.length > 0 && (
          <div className="card">
            <h2 className="text-2xl font-bold text-red-700 mb-6 flex items-center">
              Areas for Improvement ({negativeFactors.length})
            </h2>
            <div className="grid md:grid-cols-2 gap-4">
              {negativeFactors.map((factor, index) => (
                <div key={index} className="p-4 bg-red-50 border border-red-200 rounded-lg">
                  <h3 className="font-semibold text-gray-900 mb-2">{factor.feature}</h3>
                  <p className="text-sm text-gray-700">{factor.message}</p>
                  <div className="mt-2 text-xs text-gray-600">
                    Importance: {(factor.importance * 100).toFixed(1)}%
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* How This Works - Collapsible Section */}
        <div className="card">
          <button
            onClick={() => setShowExplanation(!showExplanation)}
            className="w-full flex items-center justify-between text-left"
          >
            <h2 className="text-2xl font-bold text-gray-800 flex items-center">
              How This Prediction Works
            </h2>
            <svg
              className={`w-6 h-6 transition-transform ${showExplanation ? 'rotate-180' : ''}`}
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
            </svg>
          </button>

          {showExplanation && (
            <div className="mt-6 space-y-6 text-gray-700">
              {/* Overview */}
              <div>
                <h3 className="text-xl font-semibold text-gray-900 mb-3">Overview</h3>
                <p className="mb-2">
                  This life expectancy prediction tool uses machine learning to analyze how various lifestyle, 
                  socioeconomic, and health factors influence longevity based on comprehensive Finnish population data.
                </p>
              </div>

              {/* Machine Learning Model */}
              <div className="bg-blue-50 p-4 rounded-lg">
                <h3 className="text-xl font-semibold text-gray-900 mb-3">Machine Learning Model</h3>
                <ul className="list-disc list-inside space-y-2">
                  <li><strong>Algorithm:</strong> XGBoost (Extreme Gradient Boosting) - A powerful ensemble learning method 
                  that combines multiple decision trees to make accurate predictions</li>
                  <li><strong>Training Data:</strong> Regional health and demographic data from Finnish municipalities 
                  covering the years 2013-2021</li>
                  <li><strong>Features Analyzed:</strong> Over 20 different factors including income, education, health behaviors, 
                  employment, and chronic conditions</li>
                  <li><strong>Validation:</strong> The model is tested against historical data to ensure accurate predictions</li>
                </ul>
              </div>

              {/* Data Sources */}
              <div className="bg-green-50 p-4 rounded-lg">
                <h3 className="text-xl font-semibold text-gray-900 mb-3">Data Sources</h3>
                <p className="mb-3">Our model is built using authoritative Finnish health and statistics data:</p>
                <ul className="list-disc list-inside space-y-2">
                  <li>
                    <strong>THL (Finnish Institute for Health and Welfare):</strong> Health indicators including smoking rates, 
                    alcohol consumption, physical activity, mental health metrics, healthcare access, and chronic disease prevalence
                    <br />
                    <a 
                      href="https://sotkanet.fi/sotkanet/en/haku" 
                      target="_blank" 
                      rel="noopener noreferrer"
                      className="text-blue-600 hover:underline text-sm"
                    >
                      sotkanet.fi →
                    </a>
                  </li>
                  <li>
                    <strong>Statistics Finland (Tilastokeskus):</strong> Demographic and socioeconomic data including age distribution, 
                    education levels, employment status, income statistics, and regional population characteristics
                    <br />
                    <a 
                      href="https://pxdata.stat.fi/PXWeb/pxweb/en/StatFin/" 
                      target="_blank" 
                      rel="noopener noreferrer"
                      className="text-blue-600 hover:underline text-sm"
                    >
                      stat.fi →
                    </a>
                  </li>
                </ul>
              </div>

              {/* Key Factors */}
              <div className="bg-purple-50 p-4 rounded-lg">
                <h3 className="text-xl font-semibold text-gray-900 mb-3">Key Factors Analyzed</h3>
                <div className="grid md:grid-cols-2 gap-4">
                  <div>
                    <h4 className="font-semibold mb-2">Lifestyle Factors:</h4>
                    <ul className="list-disc list-inside space-y-1 text-sm">
                      <li>Smoking status</li>
                      <li>Alcohol consumption</li>
                      <li>Physical activity levels</li>
                      <li>Mental well-being</li>
                    </ul>
                  </div>
                  <div>
                    <h4 className="font-semibold mb-2">Health Factors:</h4>
                    <ul className="list-disc list-inside space-y-1 text-sm">
                      <li>Chronic health conditions</li>
                      <li>Healthcare access</li>
                      <li>Age and demographics</li>
                    </ul>
                  </div>
                  <div>
                    <h4 className="font-semibold mb-2">Socioeconomic Factors:</h4>
                    <ul className="list-disc list-inside space-y-1 text-sm">
                      <li>Income level</li>
                      <li>Education attainment</li>
                      <li>Employment status</li>
                    </ul>
                  </div>
                  <div>
                    <h4 className="font-semibold mb-2">Psychological Factors:</h4>
                    <ul className="list-disc list-inside space-y-1 text-sm">
                      <li>Life satisfaction</li>
                      <li>Happiness levels</li>
                      <li>Mental health status</li>
                    </ul>
                  </div>
                </div>
              </div>

              {/* How to Interpret */}
              <div className="bg-yellow-50 p-4 rounded-lg">
                <h3 className="text-xl font-semibold text-gray-900 mb-3">How to Interpret Your Results</h3>
                <ul className="space-y-2">
                  <li>
                    <strong>Predicted Life Expectancy:</strong> Based on your current lifestyle and demographic factors, 
                    this is the estimated age you might reach. This is a statistical estimate, not a certainty.
                  </li>
                  <li>
                    <strong>Population Average:</strong> The average life expectancy for the Finnish population based 
                    on historical data.
                  </li>
                  <li>
                    <strong>Percentile:</strong> Your ranking compared to others. For example, 75th percentile means 
                    your predicted life expectancy is higher than 75% of the population.
                  </li>
                  <li>
                    <strong>Factor Importance:</strong> Shows how strongly each factor influences the prediction. 
                    Higher percentages mean greater impact on your life expectancy.
                  </li>
                </ul>
              </div>

              {/* Limitations */}
              <div className="bg-red-50 p-4 rounded-lg">
                <h3 className="text-xl font-semibold text-gray-900 mb-3">Important Limitations</h3>
                <ul className="list-disc list-inside space-y-2 text-sm">
                  <li>This is a <strong>statistical prediction</strong> based on population trends, not a medical diagnosis or guarantee</li>
                  <li>Individual variation is enormous - genetics, unexpected events, and medical advances all play significant roles</li>
                  <li>The model is trained on Finnish data and may not generalize perfectly to other populations</li>
                  <li>Life expectancy is influenced by factors we don't measure (genetics, environmental exposures, specific medical conditions)</li>
                  <li>Small lifestyle changes can significantly impact outcomes - predictions can change over time</li>
                  <li><strong>This tool is for educational purposes only</strong> and should not replace medical advice from healthcare professionals</li>
                </ul>
              </div>

              {/* About the Project */}
              <div className="border-t pt-4">
                <h3 className="text-lg font-semibold text-gray-900 mb-2">About This Project</h3>
                <p className="text-sm">
                  This prediction tool was developed as an educational project to demonstrate how machine learning 
                  can be applied to public health data. It aims to raise awareness about the factors that influence 
                  longevity and empower individuals to make informed health decisions.
                </p>
              </div>
            </div>
          )}
        </div>

        {/* Action Buttons */}
        <div className="card text-center space-y-4">
          <button
            onClick={onRestart}
            className="btn-primary"
          >
            Take Assessment Again
          </button>
          
          <p className="text-sm text-gray-600">
            Share these results with your healthcare provider to discuss personalized health strategies.
          </p>
        </div>

        {/* Disclaimer */}
        <div className="text-center text-xs text-gray-500 pb-8">
          <p>
            * This prediction is based on statistical models and population data. Individual outcomes vary significantly.
            This tool is for informational purposes only and does not constitute medical advice.
          </p>
        </div>
      </div>
    </div>
  );
};

export default ResultDisplay;
