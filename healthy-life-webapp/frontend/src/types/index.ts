// Type definitions for the Life Expectancy Prediction App

export interface UserData {
  birth_date: string;
  income: number;
  education: 'none' | 'high_school' | 'bachelor' | 'master_plus';
  smoking: 'never' | 'occasional' | 'daily';
  alcohol_units: number;
  exercise_days: number;
  chronic_conditions: string[];
  mental_health_score: number;
  happiness_score: number;
  employment_status: 'employed' | 'unemployed' | 'retired' | 'student';
}

export interface Factor {
  feature: string;
  raw_feature_name: string;
  importance: number;
  correlation: number;
  effect: string;
  impact_direction: 'positive' | 'negative';
  your_value: number;
  average_value: number;
  percentage_difference: number;
  message: string;
  is_favorable: boolean;
}

export interface PredictionResponse {
  predicted_life_expectancy: number;
  average_life_expectancy: number;
  difference_from_average: number;
  percentile: number;
  user_age: number;
  factors: Factor[];
  recommendations: string[];
}

export interface Question {
  id: keyof UserData;
  question: string;
  type: 'date' | 'slider' | 'radio' | 'checkbox' | 'scale';
  required: boolean;
  min?: number;
  max?: number;
  step?: number;
  default?: number | string;
  unit?: string;
  options?: { value: string; label: string }[];
  min_label?: string;
  max_label?: string;
  help_text?: string;
  max_date?: string;
}
