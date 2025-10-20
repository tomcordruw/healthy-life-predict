import { useState } from 'react';
import './App.css';
import Welcome from './components/Welcome';
import QuestionForm from './components/QuestionForm';
import ResultDisplay from './components/ResultDisplay';
import type { PredictionResponse } from './types';

type AppStep = 'welcome' | 'questionnaire' | 'results';

function App() {
  const [currentStep, setCurrentStep] = useState<AppStep>('welcome');
  const [predictionResult, setPredictionResult] = useState<PredictionResponse | null>(null);

  const handleStart = () => {
    setCurrentStep('questionnaire');
  };

  const handleSubmit = (result: PredictionResponse) => {
    setPredictionResult(result);
    setCurrentStep('results');
  };

  const handleRestart = () => {
    setPredictionResult(null);
    setCurrentStep('welcome');
  };

  return (
    <div className="App">
      {currentStep === 'welcome' && (
        <Welcome onStart={handleStart} />
      )}
      
      {currentStep === 'questionnaire' && (
        <QuestionForm onSubmit={handleSubmit} />
      )}
      
      {currentStep === 'results' && predictionResult && (
        <ResultDisplay 
          result={predictionResult} 
          onRestart={handleRestart}
        />
      )}
    </div>
  );
}

export default App;
