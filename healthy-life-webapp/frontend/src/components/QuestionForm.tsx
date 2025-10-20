import React, { useState, useEffect } from 'react';
import apiService from '../services/api';
import type { UserData, PredictionResponse, Question } from '../types';

interface QuestionFormProps {
  onSubmit: (result: PredictionResponse) => void;
}

const QuestionForm: React.FC<QuestionFormProps> = ({ onSubmit }) => {
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [questions, setQuestions] = useState<Question[]>([]);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  
  const [formData, setFormData] = useState<Partial<UserData>>({
    chronic_conditions: []
  });

  useEffect(() => {
    // Fetch questions from API
    apiService.getQuestions()
      .then(data => {
        setQuestions(data.questions);
        
        // Initialize form data with default values for sliders and scales
        const initialData: Partial<UserData> = { chronic_conditions: [] };
        data.questions.forEach((q: Question) => {
          if ((q.type === 'slider' || q.type === 'scale') && q.default !== undefined) {
            (initialData as any)[q.id] = q.default;
          }
        });
        setFormData(initialData);
        
        setLoading(false);
      })
      .catch(_ => {
        setError('Failed to load questions');
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-16 w-16 border-b-2 border-primary-600 mx-auto"></div>
          <p className="mt-4 text-gray-600">Loading questions...</p>
        </div>
      </div>
    );
  }

  if (error || questions.length === 0) {
    return (
      <div className="min-h-screen flex items-center justify-center px-4">
        <div className="card max-w-md text-center">
          <p className="text-red-600 mb-4">{error || 'No questions available'}</p>
          <button onClick={() => window.location.reload()} className="btn-primary">
            Retry
          </button>
        </div>
      </div>
    );
  }

  const currentQuestion = questions[currentQuestionIndex];
  const progress = ((currentQuestionIndex + 1) / questions.length) * 100;

  const handleNext = () => {
    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else {
      handleSubmit();
    }
  };

  const handleBack = () => {
    if (currentQuestionIndex > 0) {
      setCurrentQuestionIndex(currentQuestionIndex - 1);
    }
  };

  const handleSubmit = async () => {
    setSubmitting(true);
    setError(null);
    
    try {
      const result = await apiService.getPrediction(formData as UserData);
      onSubmit(result);
    } catch (err: any) {
      setError(err.response?.data?.error || 'Failed to get prediction');
      setSubmitting(false);
    }
  };

  const updateFormData = (key: keyof UserData, value: any) => {
    setFormData(prev => ({ ...prev, [key]: value }));
  };

  const renderQuestion = () => {
    const value = formData[currentQuestion.id];
    
    switch (currentQuestion.type) {
      case 'date':
        return (
          <input
            type="date"
            value={value as string || ''}
            max={currentQuestion.max_date}
            onChange={(e) => updateFormData(currentQuestion.id, e.target.value)}
            className="input-field text-center text-lg"
          />
        );
      
      case 'slider':
        const sliderValue = value !== undefined && value !== null ? value : (currentQuestion.default ?? currentQuestion.min);
        return (
          <div className="space-y-4">
            <div className="text-center">
              <span className="text-4xl font-bold text-primary-600">
                {sliderValue}
              </span>
              <span className="text-xl text-gray-600 ml-2">{currentQuestion.unit}</span>
            </div>
            <input
              type="range"
              min={currentQuestion.min}
              max={currentQuestion.max}
              step={currentQuestion.step}
              value={sliderValue as number}
              onChange={(e) => updateFormData(currentQuestion.id, parseFloat(e.target.value))}
              className="w-full h-3 bg-gray-200 rounded-lg appearance-none cursor-pointer"
            />
            <div className="flex justify-between text-sm text-gray-600">
              <span>{currentQuestion.min} {currentQuestion.unit}</span>
              <span>{currentQuestion.max} {currentQuestion.unit}</span>
            </div>
          </div>
        );
      
      case 'radio':
        return (
          <div className="space-y-3">
            {currentQuestion.options?.map(option => (
              <label
                key={option.value}
                className="flex items-center p-4 border-2 border-gray-200 rounded-lg cursor-pointer hover:border-primary-500 transition-colors"
              >
                <input
                  type="radio"
                  name={currentQuestion.id}
                  value={option.value}
                  checked={value === option.value}
                  onChange={(e) => updateFormData(currentQuestion.id, e.target.value)}
                  className="w-5 h-5 text-primary-600"
                />
                <span className="ml-3 text-lg">{option.label}</span>
              </label>
            ))}
          </div>
        );
      
      case 'checkbox':
        const checkedValues = (value as string[]) || [];
        return (
          <div className="space-y-3">
            {currentQuestion.options?.map(option => (
              <label
                key={option.value}
                className="flex items-center p-4 border-2 border-gray-200 rounded-lg cursor-pointer hover:border-primary-500 transition-colors"
              >
                <input
                  type="checkbox"
                  value={option.value}
                  checked={checkedValues.includes(option.value)}
                  onChange={(e) => {
                    let newValues: string[];
                    if (option.value === 'none') {
                      newValues = e.target.checked ? ['none'] : [];
                    } else {
                      newValues = e.target.checked
                        ? [...checkedValues.filter(v => v !== 'none'), option.value]
                        : checkedValues.filter(v => v !== option.value);
                    }
                    updateFormData(currentQuestion.id, newValues);
                  }}
                  className="w-5 h-5 text-primary-600"
                />
                <span className="ml-3 text-lg">{option.label}</span>
              </label>
            ))}
          </div>
        );
      
      case 'scale':
        return (
          <div className="space-y-6">
            <div className="flex justify-center items-center gap-2">
              {Array.from({ length: currentQuestion.max! - currentQuestion.min! + 1 }, (_, i) => {
                const scaleValue = currentQuestion.min! + i;
                const isSelected = value === scaleValue;
                return (
                  <button
                    key={scaleValue}
                    onClick={() => updateFormData(currentQuestion.id, scaleValue)}
                    className={`w-12 h-12 rounded-full font-bold transition-all ${
                      isSelected
                        ? 'bg-blue-600 text-white scale-110 shadow-lg'
                        : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                    }`}
                  >
                    {scaleValue}
                  </button>
                );
              })}
            </div>
            <div className="flex justify-between text-sm text-gray-600">
              <span>{currentQuestion.min_label}</span>
              <span>{currentQuestion.max_label}</span>
            </div>
          </div>
        );
      
      default:
        return null;
    }
  };

  const isAnswered = () => {
    const value = formData[currentQuestion.id];
    if (currentQuestion.type === 'checkbox') {
      return Array.isArray(value) && value.length > 0;
    }
    // For numbers (sliders, scales), 0 is a valid value
    if (currentQuestion.type === 'slider' || currentQuestion.type === 'scale') {
      return value !== undefined && value !== null;
    }
    return value !== undefined && value !== null && value !== '';
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-primary-50 to-blue-100 py-8 px-4">
      {/* Progress Bar */}
      <div className="max-w-4xl mx-auto mb-8">
        <div className="bg-white rounded-full h-3 shadow-inner overflow-hidden">
          <div
            className="bg-gradient-to-r from-blue-500 to-blue-600 h-3 rounded-full transition-all duration-300"
            style={{ width: `${progress}%` }}
          />
        </div>
        <div className="flex justify-between mt-2 text-sm text-gray-600">
          <span>Question {currentQuestionIndex + 1} of {questions.length}</span>
          <span>{Math.round(progress)}% Complete</span>
        </div>
      </div>

      {/* Question Card */}
      <div className="max-w-3xl mx-auto">
        <div className="card space-y-6">
          <h2 className="text-2xl md:text-3xl font-bold text-gray-900">
            {currentQuestion.question}
          </h2>
          
          {currentQuestion.help_text && (
            <p className="text-gray-600 italic">{currentQuestion.help_text}</p>
          )}
          
          <div className="py-4">
            {renderQuestion()}
          </div>
          
          {error && (
            <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg">
              {error}
            </div>
          )}
          
          <div className="flex justify-between pt-4">
            <button
              onClick={handleBack}
              disabled={currentQuestionIndex === 0}
              className="btn-secondary disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <svg className="inline-block mr-2 w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
              </svg>
              Back
            </button>
            
            <button
              onClick={handleNext}
              disabled={!isAnswered() || submitting}
              className="btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {submitting ? (
                <>
                  <svg className="animate-spin inline-block mr-2 h-5 w-5" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                  </svg>
                  Processing...
                </>
              ) : currentQuestionIndex === questions.length - 1 ? (
                <>
                  Get Results
                  <svg className="inline-block ml-2 w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                  </svg>
                </>
              ) : (
                <>
                  Next
                  <svg className="inline-block ml-2 w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                  </svg>
                </>
              )}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default QuestionForm;
