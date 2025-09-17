# Statistics Finland Health Data Documentation

Generated on: 2025-09-16 01:18:57  
Updated on: 2025-09-17 (Reorganized structure)

This document describes the health and mortality datasets downloaded from Statistics Finland (Tilastokeskus) PxWeb API, now organized into logical categories for mortality analysis.

## Overview

The data has been reorganized from the original StatFin structure into thematic categories:
- **mortality_rates/**: Direct probability calculations and life tables
- **deaths_basic/**: Fundamental demographic mortality data
- **deaths_geographic/**: Regional and geographic mortality patterns
- **causes_detailed/**: Specific medical conditions (ICD-10 codes)
- **causes_main/**: Main disease categories and trends
- **causes_external/**: Accidents, violence, and external causes
- **causes_risk_factors/**: Behavioral and lifestyle risk factors
- **causes_specialized/**: Specialized medical data
- **causes_geographic/**: Regional cause-of-death analysis
- **demographics/**: Broader vital statistics

Total datasets: 23 (reorganized into 10 thematic folders)

## Dataset Details by Category

### 🎯 Essential for Mortality Probability Analysis

#### mortality_rates/life_tables_detailed.csv

**Original**: statfin_kuol_pxt_12ap.px  
**Title**: Life table by Year, Sex, Age and Information  
**Period**: 1986-2023 (158 KB)

**Key Features**: 
- **Direct death probabilities** per 1,000 by age and sex
- Survivors of 100,000 born alive
- Life expectancy calculations

**Variables**:
- **Year** (`Vuosi`): 38 categories (1986-2023)
- **Sex** (`Sukupuoli`): Total, Males, Females
- **Age** (`Ikä`): 101 categories (0-100)
- **Information**: Probability of death per mille, Survivors, Life expectancy

**Sample Data**:
```csv
Year,Sex,Age,Probability of death per mille,Survivors of 100,000 born alive,Life expectancy years
1986,Total,0,5.84,100000,74.70
1986,Total,1,0.36,99416,74.14
```

⭐ **PRIMARY FILE for baseline mortality probabilities**

---

#### deaths_basic/deaths_by_detailed_age_sex.csv

**Original**: statfin_kuol_pxt_12ag.px  
**Title**: Deaths by Year, Sex, Age and Information  
**Period**: 1980-2024 (20 KB)

**Key Features**:
- Deaths by single-year age groups (0-112)
- Detailed demographic breakdown
- Long time series for trend analysis

**Variables**:
- **Year** (`Vuosi`): 45 categories (1980-2024)
- **Sex** (`Sukupuoli`): Total, Males, Females  
- **Age** (`Ikä`): 114 categories (0-112 years)

⭐ **KEY for age-specific mortality patterns**

---

#### causes_detailed/deaths_by_icd10_codes.csv

**Original**: statfin_ksyyt_pxt_11be.px  
**Title**: Deaths by Underlying cause of death (ICD-10, 3-character level)  
**Period**: 1998-2023 (4.17 MB)

**Key Features**:
- **1,731 specific ICD-10 medical codes**
- Most detailed disease-specific mortality data
- Age and sex breakdowns for each condition

**Variables**:
- **Underlying cause**: 1,731 ICD-10 3-character codes
- **Age**: 22 categories
- **Year**: 26 categories (1998-2023)
- **Sex**: Total, Males, Females

⭐ **MOST DETAILED disease-specific mortality data**

---

### 🏥 Disease and Medical Conditions

#### causes_main/deaths_by_cause_timeseries.csv

**Original**: statfin_ksyyt_pxt_11ay.px  
**Title**: Deaths/death rates by Sex, Underlying cause of death (time series classification)  
**Period**: 1971-2023 (363 KB)

**Key Features**:
- 65 main disease categories
- Age-standardized death rates
- Long-term trends (50+ years)
- Annual change percentages

**Variables**:
- **Sex**: Total, Males, Females
- **Underlying cause**: 65 categories (time series classification)
- **Year**: 53 categories (1971-2023)
- **Information**: Deaths, age-standardized rates, crude rates, annual changes

⭐ **KEY for major disease category analysis**

---

#### causes_main/deaths_by_cause_age_sex.csv

**Original**: statfin_ksyyt_pxt_11az.px  
**Title**: Deaths by Underlying cause of death, Age, Sex, Year  
**Period**: 1969-2023 (346 KB)

**Key Features**:
- 65 cause categories with age breakdowns
- Historical perspective (55 years)
- 25 age groups for detailed analysis

---

### 🚗 External Causes and Risk Factors

#### causes_external/accidents_violence_detailed.csv

**Original**: statfin_ksyyt_pxt_11b2.px  
**Title**: Accidental and violent deaths by Accidents and violence classification  
**Period**: 1998-2023 (1.2 MB)

**Key Features**:
- **141 specific external cause categories**
- Alcohol and drug involvement data
- Detailed accident and violence classifications

**Variables**:
- **External causes**: 141 categories
- **Age**: 22 categories
- **Year**: 26 categories (1998-2023)
- **Information**: Total deaths, alcohol/drug involvement

⭐ **KEY for accident and violence risk analysis**

---

#### causes_risk_factors/alcohol_related_deaths.csv

**Original**: statfin_ksyyt_pxt_11bx.px  
**Title**: Alcohol-related deaths by classification  
**Period**: 2005-2023 (26 KB)

**Key Features**:
- 14 alcohol-related death categories
- Age-specific alcohol mortality risks

⭐ **ALCOHOL risk factor analysis**

---

#### causes_risk_factors/drug_related_deaths.csv

**Original**: statfin_ksyyt_pxt_12d9.px  
**Title**: Drug-related deaths by Drug classification  
**Period**: 2006-2023 (10 KB)

**Key Features**:
- 5 drug categories
- Disorders, accidental, intentional poisoning

⭐ **DRUG risk factor analysis**

---

#### causes_risk_factors/suicide_deaths.csv

**Original**: statfin_ksyyt_pxt_11by.px  
**Title**: Suicides by Age, Year, Sex  
**Period**: 1921-2023 (9 KB)

**Key Features**:
- 103 years of suicide data
- Age-specific suicide risks
- Historical trends over century

---

### 🗺️ Geographic and Regional Analysis

#### deaths_geographic/deaths_by_region_age_sex.csv

**Original**: statfin_kuol_pxt_12ak.px  
**Title**: Deaths by Year, Area, Sex, Age  
**Period**: 1990-2024 (746 KB)

**Key Features**:
- **309 geographic regions**
- Age groups and sex breakdowns
- Regional mortality differences

**Variables**:
- **Year**: 35 categories (1990-2024)
- **Area**: 309 categories (municipalities/regions)
- **Sex**: Total, Males, Females
- **Age**: 22 categories

⭐ **KEY for regional mortality analysis**

---

### 📊 Additional Reference Data

#### mortality_rates/life_expectancy_national.csv
**Original**: statfin_kuol_pxt_12am.px - National life expectancy trends

#### mortality_rates/life_expectancy_regional.csv  
**Original**: statfin_kuol_pxt_12an.px - Regional life expectancy variations

#### demographics/vital_statistics_regional.csv
**Original**: statfin_kuol_pxt_12au.px - Broader demographic context