# Feature Conversion Guide: From Questionnaire to Machine Learning Model

## Table of Contents
1. [Overview](#overview)
2. [Conversion Philosophy](#conversion-philosophy)
3. [Detailed Feature Mappings](#detailed-feature-mappings)
4. [Motivation and Rationale](#motivation-and-rationale)
5. [Technical Implementation](#technical-implementation)
6. [Limitations and Assumptions](#limitations-and-assumptions)

---

## Overview

This document explains how user responses from the questionnaire are converted into numerical features that the XGBoost machine learning model uses to predict life expectancy. The conversion process bridges the gap between user-friendly questions and the statistical features derived from population-level health data.

### The Challenge

The machine learning model was trained on **regional population data** from Finnish municipalities (2013-2021), where each data point represents aggregate statistics for thousands of people. However, we want to predict life expectancy for **individual users** based on their personal responses. This creates a fundamental challenge: how do we map individual characteristics to population-level features?

### The Solution

Our conversion strategy uses **feature engineering** to estimate what the population-level statistics would be for a region where everyone has similar characteristics to the user. This is not perfect, but it provides a reasonable approximation that allows us to leverage population-level patterns for individual predictions.

---

## Conversion Philosophy

### Core Principles

1. **Population Proxy Approach**: We estimate population statistics as if the user lived in a region where their characteristics are typical
2. **Evidence-Based Scaling**: Conversion factors are based on real-world relationships found in epidemiological research
3. **Conservative Estimates**: When uncertain, we default to median population values to avoid over-prediction
4. **Correlation Preservation**: We maintain the statistical relationships observed in the training data

### Why Not Just Use Individual Values?

The model expects features like "percentage of daily smokers in the region" (0-30%), not "does this person smoke" (yes/no). Direct substitution doesn't work because:
- The model learned relationships at the population level
- Feature scales and distributions would be completely different
- Statistical interactions between features would break down

---

## Detailed Feature Mappings

### 1. Age-Related Features
**Model Features**: `Average age, both sexes`, `Average age, men`, `Average age, women`  
**Feature Importance**: ~0.010 (moderate)

#### Question:
- **What is your date of birth?**

#### Conversion:
```python
age = today.year - birth.year
features['Average age, both sexes'] = float(age)
features['Average age, men'] = float(age)
features['Average age, women'] = float(age)
```

#### Motivation:
Age is the most straightforward conversion. We use the user's actual age directly as a proxy for the "average age" in their demographic context. This is reasonable because age-related health risks are highly individual.

---

### 2. Income and Financial Security
**Model Features**: `1. EARNED INCOME, mean`, `Disposable cash income, median`  
**Feature Importance**: 0.614 (HIGHEST - most important factor!)

#### Question:
- **What is your annual income (before taxes)?** (€10,000 - €100,000)

#### Conversion:
```python
income = user_data['income']
features['1. EARNED INCOME, mean'] = float(income)
features['Disposable cash income, median'] = float(income * 1.15)
```

#### Motivation:
Income is the single strongest predictor of life expectancy in our model. The conversion is direct for earned income. Disposable income is estimated as 115% of earned income, based on typical Finnish tax structures where disposable income is slightly higher due to various benefits and deductions.

**Why Income Matters**:
- Access to quality healthcare and nutrition
- Ability to live in safer neighborhoods
- Lower stress levels
- Better health literacy and preventive care
- Access to fitness facilities and healthy food options

---

### 3. Education Level
**Model Features**: 
- `Share of persons aged 15 or over with tertiary level qualification, %`
- `Share of persons aged 15 or over with at least upper secondary qualification, %`
- `Share of persons aged 15 or over without upper secondary qualification, %, %`

**Feature Importance**: 0.028 (low-moderate)

#### Question:
- **What is your highest level of education?**
  - Less than high school → 10%
  - High school diploma → 20%
  - Bachelor's degree → 35%
  - Master's degree or higher → 50%

#### Conversion:
```python
education_map = {
    'none': 10.0,         # Low tertiary education region
    'high_school': 20.0,  # Below average
    'bachelor': 35.0,     # Above average
    'master_plus': 50.0   # High education region
}
tertiary_pct = education_map[education]
```

#### Motivation:
Education percentages represent what proportion of the population in a "typical" region has tertiary education. We map individual education to population percentages based on Finnish educational distribution data:
- ~10%: Regions with low educational attainment
- ~27%: National median
- ~50%: Urban areas with universities

**Why Education Matters**:
- Health literacy and awareness
- Better health-related decision making
- Higher income correlation
- Access to information and resources
- Social networks that promote healthy behaviors

---

### 4. Smoking Habits
**Model Feature**: `daily_smokers` (percentage of daily smokers in population)  
**Feature Importance**: 0.027 (moderate)

#### Question:
- **Do you smoke?**
  - Never / Not currently → 5%
  - Occasionally → 12%
  - Daily → 25%

#### Conversion:
```python
smoking_map = {
    'never': 5.0,      # Low smoking region (healthy lifestyle area)
    'occasional': 12.0, # Near median (13.6% national median)
    'daily': 25.0       # High smoking region
}
```

#### Motivation:
We map personal smoking status to regional smoking prevalence. A daily smoker likely lives in or represents characteristics of a region where smoking is more common (25%), while non-smokers represent healthier regions (5%). The national median is 13.6%.

**Why Smoking Matters**:
- Single most preventable cause of premature death
- Increases risk of cancer, heart disease, stroke
- Reduces lung capacity and immune function
- Accelerates aging processes

---

### 5. Alcohol Consumption
**Model Features**: `alcohol_sales` (liters per capita), `binge_drinking` (%)  
**Feature Importance**: 0.035 for sales, 0.018 for binge drinking

#### Question:
- **How many alcoholic drinks do you consume per week?** (0-30)

#### Conversion:
```python
alcohol_units = user_data['alcohol_units']
features['alcohol_sales'] = alcohol_units * 0.5        # Scale to regional sales
features['binge_drinking'] = min(alcohol_units * 1.5, 25.0)  # Binge percentage
```

#### Motivation:
- **Alcohol sales**: Scaled down by 0.5 to convert weekly personal consumption to annual regional per-capita sales (in liters)
- **Binge drinking**: Higher multiplier (1.5x) because people who drink more are more likely to engage in binge drinking. Capped at 25% (maximum observed in data)

**Epidemiological Basis**:
- 0 drinks/week → 0 L/capita, 0% binge drinking (very healthy region)
- 5 drinks/week → 2.5 L/capita, 7.5% binge drinking (near median)
- 20 drinks/week → 10 L/capita, 25% binge drinking (high-risk region)

---

### 6. Physical Activity
**Model Feature**: `physical_activity` (percentage engaging in regular activity)  
**Feature Importance**: 0.0009 (very low, surprisingly!)

#### Question:
- **How many days per week do you exercise for at least 30 minutes?** (0-7)

#### Conversion:
```python
exercise_days = user_data['exercise_days']
features['physical_activity'] = (exercise_days / 7.0) * 40
```

#### Motivation:
Converts weekly exercise frequency to a percentage (0-40%). The scaling assumes:
- 0 days → 0% (inactive region)
- 3.5 days → 20% (median activity level)
- 7 days → 40% (highly active region)

**Note**: Despite low importance in our model, extensive research shows physical activity strongly impacts health. The low importance may reflect:
- Physical activity is correlated with other factors (income, education)
- Regional data may not capture individual variation well
- Finnish population is generally active (high baseline)

---

### 7. Chronic Health Conditions
**Model Feature**: `disability_ratio` (percentage with disability benefits)  
**Feature Importance**: 0.056 (moderate)

#### Question:
- **Do you have any of these chronic health conditions?** (checkboxes)
  - Diabetes, Heart disease, High blood pressure, Respiratory disease, Arthritis, Cancer, Other

#### Conversion:
```python
chronic_conditions = user_data['chronic_conditions']
features['disability_ratio'] = min(len(chronic_conditions) * 3.0, 20.0)
```

#### Motivation:
Each chronic condition adds 3 percentage points to the disability ratio, capped at 20% (max observed):
- 0 conditions → 0% (healthy region)
- 2-3 conditions → 6-9% (near median of 8.3%)
- 6+ conditions → 20% (maximum disability rate)

The 3% per condition factor is based on:
- Finnish disability benefit statistics
- Disease burden in the population
- Overlap between multiple conditions

---

### 8. Mental Health and Well-being
**Model Features**: `mental_health`, `severe_mental_strain` (%)  
**Feature Importance**: 0.003 for mental_health, 0.002 for severe_mental_strain

#### Question:
- **How would you rate your mental and emotional well-being?** (1-10 scale)

#### Conversion:
```python
mental_health_score = user_data['mental_health_score']  # User: 1=poor, 10=excellent
features['mental_health'] = (11 - mental_health_score) * 15      # Model: higher=worse
features['severe_mental_strain'] = (11 - mental_health_score) * 2  # Percentage
```

#### Motivation:
**IMPORTANT**: The model features have a **negative correlation** with life expectancy (higher values = worse outcomes). Therefore:
- User score of 10 (excellent) → mental_health = 15 (low strain)
- User score of 5 (moderate) → mental_health = 90 (medium strain)
- User score of 1 (poor) → mental_health = 150 (high strain)

The inversion formula `(11 - score)` converts from "higher is better" (user perspective) to "higher is worse" (model perspective).

**Scaling Factors**:
- Mental health: Multiplied by 15 to match the model's training range (15-150)
- Severe strain: Multiplied by 2 to represent percentage of population with severe strain (2-20%)

---

### 9. Life Satisfaction and Happiness
**Model Feature**: `percentage_happy` (% satisfied with life)  
**Feature Importance**: 0.004 (low)

#### Question:
- **Overall, how satisfied are you with your life?** (1-10 scale)

#### Conversion:
```python
happiness_score = user_data['happiness_score']
features['percentage_happy'] = (happiness_score / 10.0) * 80
```

#### Motivation:
Linear scaling from user score (1-10) to population percentage (0-80%):
- Score of 5 → 40% happy (below median)
- Score of 7 → 56% happy (near median of 52%)
- Score of 10 → 80% happy (very satisfied region)

The 80% cap reflects that even in the happiest regions, not everyone reports being satisfied.

---

### 10. Employment Status
**Model Feature**: `work_until_retired` (average years until retirement)  
**Feature Importance**: 0.001 (low)

#### Question:
- **What is your current employment status?**
  - Employed / Unemployed / Retired / Student

#### Conversion:
```python
retirement_age = 65  # Finnish retirement age

if employment_status == 'retired':
    features['work_until_retired'] = 0
elif employment_status == 'employed':
    features['work_until_retired'] = max(retirement_age - age, 0)
else:  # unemployed, student
    features['work_until_retired'] = 30  # Average working years remaining
```

#### Motivation:
- **Retired**: 0 years (already retired)
- **Employed**: Calculate remaining working years until age 65
- **Unemployed/Student**: Use 30 as a placeholder (median in training data is 27.75)

**Why Employment Matters**:
- Social engagement and purpose
- Financial security
- Structured routine
- Social connections
- Mental stimulation

---

### 11. Derived Features

Several features are derived from combinations of user inputs:

#### Obesity Rate
```python
base_obesity = 20.0  # National median
exercise_factor = (7 - exercise_days) * 1.0
features['obesity_rate'] = min(base_obesity + exercise_factor, 35.0)
```

**Rationale**: Less exercise correlates with higher obesity. Each day of inactivity adds ~1% to obesity rate.

---

## Motivation and Rationale

### Why This Approach?

#### 1. Preserving Statistical Relationships
The model learned that in regions where:
- Income is high
- Education is high
- Smoking is low
- People exercise more

...life expectancy tends to be higher. Our conversion preserves these relationships by mapping individual characteristics to corresponding regional characteristics.

#### 2. Evidence-Based Scaling
Conversion factors are based on:
- **Finnish national statistics** (THL, Statistics Finland)
- **Epidemiological research** linking individual behaviors to population health
- **Regional health data patterns** observed during model training

#### 3. Avoiding Extrapolation
We use medians for features that can't be reasonably estimated from individual data (e.g., population density, healthcare worker availability). This prevents the model from making predictions based on unrealistic feature combinations.

### Theoretical Foundation

This approach is based on **ecological inference** - using population-level data to make individual-level predictions. While not perfect, it's justified because:

1. **Contextual Effects**: Individual health is influenced by community characteristics
2. **Behavioral Clustering**: People with similar characteristics tend to live in similar areas
3. **Resource Availability**: Regional resources (healthcare, education) are shared by individuals in that region

---

## Technical Implementation

### Feature Vector Generation

The conversion process follows these steps:

```python
def get_feature_vector(user_data):
    # 1. Calculate derived values (age, etc.)
    age = calculate_age(user_data['birth_date'])
    
    # 2. Initialize with population medians
    features = feature_medians.copy()
    
    # 3. Override with user-specific conversions
    features['1. EARNED INCOME, mean'] = user_data['income']
    features['daily_smokers'] = smoking_map[user_data['smoking']]
    # ... (continue for all mapped features)
    
    # 4. Keep medians for non-mappable features
    # (population density, healthcare access, etc. stay at median)
    
    # 5. Return ordered vector matching model's expected input
    return [features[name] for name in feature_names]
```

### Validation

We validate conversions by:
1. **Range checking**: Ensuring converted values fall within training data ranges
2. **Correlation preservation**: Verifying that converted features maintain expected relationships
3. **Sanity testing**: Comparing predictions for known scenarios to expected outcomes

---

## Limitations and Assumptions

### 1. Ecological Fallacy
**Issue**: Population-level relationships don't always hold for individuals  
**Mitigation**: Focus on well-established individual-level risk factors (smoking, income, education)

### 2. Linear Scaling Assumptions
**Issue**: Relationships may not be perfectly linear (e.g., 2x alcohol ≠ 2x risk)  
**Mitigation**: Use caps and non-linear scaling where research supports it

### 3. Missing Individual Factors
**Issue**: Genetics, family history, specific medical conditions not captured  
**Mitigation**: Clear disclaimers; emphasize educational purpose

### 4. Cultural Context
**Issue**: Model trained on Finnish data may not generalize to other populations  
**Mitigation**: Document data source; target Finnish users primarily

### 5. Temporal Assumptions
**Issue**: Current behaviors may not reflect lifetime patterns  
**Mitigation**: Interpret as "current trajectory" prediction, not destiny

### 6. Feature Interactions
**Issue**: Complex interactions between features may not be perfectly preserved  
**Mitigation**: XGBoost model captures non-linear interactions during training

### 7. Unmapped Features
**Issue**: Some model features (population density, healthcare access) use median values  
**Impact**: These represent "average" conditions; predictions assume typical Finnish context

---

## Conclusion

This conversion approach balances practical constraints (individual questionnaire → population model) with scientific rigor. While imperfect, it provides reasonable estimates that:

1. **Educate users** about factors influencing longevity
2. **Preserve statistical relationships** learned by the model
3. **Generate plausible predictions** based on established health research
4. **Acknowledge limitations** through appropriate disclaimers

The goal is not perfect individual prediction (which is impossible), but rather to demonstrate how lifestyle and socioeconomic factors collectively influence life expectancy based on population-level patterns.

---

## References and Further Reading

### Data Sources
- **THL (Finnish Institute for Health and Welfare)**: https://sotkanet.fi/sotkanet/en/haku
- **Statistics Finland**: https://pxdata.stat.fi/PXWeb/pxweb/en/StatFin/

### Methodological Background
- Regional health indicators methodology (THL)
- Ecological inference in epidemiology
- XGBoost for survival prediction
- Population health determinants research

### Related Documentation
- `README.md` - Project overview
- `backend/utils/converter.py` - Implementation code
- `backend/model/feature_info.json` - Feature specifications
- `FEATURE_CONVERSION_GUIDE.md` - This document
