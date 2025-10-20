import axios from 'axios';
import type { UserData, PredictionResponse, Question } from '../types';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const apiService = {
  /**
   * Health check endpoint
   */
  async healthCheck() {
    const response = await api.get('/api/health');
    return response.data;
  },

  /**
   * Get questionnaire questions
   */
  async getQuestions(): Promise<{ questions: Question[] }> {
    const response = await api.get<{ questions: Question[] }>('/api/questions');
    return response.data;
  },

  /**
   * Submit user data and get life expectancy prediction
   */
  async getPrediction(userData: UserData): Promise<PredictionResponse> {
    const response = await api.post<PredictionResponse>('/api/predict', userData);
    return response.data;
  },
};

export default apiService;
