# Quick Reference Guide - Statistics Finland Health Data

## Deaths Statistics (kuol) - 12 datasets

| File | Title | Period | Size | Key Variables |
|------|-------|---------|------|---------------|
| `12af` | Deaths by sex | 1751-2024 | 3 KB | Year, Sex |
| `12ag` | Deaths by age (1-year) and sex | 1980-2024 | 20 KB | Year, Sex, Age (0-112) |
| `12ah` | Deaths by month | 1945-2024 | 6 KB | Year, Month |
| `12ak` | Deaths by age/sex/area | 1990-2024 | 746 KB | Year, Sex, Age, Area (309 regions) |
| `12al` | Crude death rate | 1751-2024 | 7 KB | Year, Sex |
| `12am` | Life expectancy at birth | 1751-2024 | 1 KB | Year, Sex |
| `12an` | Life expectancy by region | 1992-2023 | 28 KB | Year, Region, Sex |
| `12ap` | Life table | 1986-2023 | 158 KB | Year, Sex, Age (probabilities, survivors) |
| `12aq` | Infant mortality | 1751-2024 | 4 KB | Year, Sex |
| `12as` | **Vital statistics by area/month** | 1990M01-2024M12 | **819 MB** | Area, Month, 21 measures |
| `12at` | Vital statistics and population | 1749-2024 | 16 KB | Year |
| `12au` | Vital statistics by area | 1990-2024 | 942 KB | Year, Area |

## Causes of Death Statistics (ksyyt) - 11 datasets

| File | Title | Period | Size | Key Classifications |
|------|-------|---------|------|-------------------|
| `11ay` | Deaths by cause (time series) | 1971-2023 | 363 KB | 65 cause categories, age-standardized rates |
| `11az` | Deaths by cause/age/sex | 1969-2023 | 346 KB | 65 causes, 25 age groups |
| `11b2` | **Accidental & violent deaths** | 1998-2023 | **1.2 MB** | 141 external causes, alcohol/drug involvement |
| `11bd` | Infant deaths & stillbirths | 1998-2023 | 97 KB | ICD-10 codes, detailed infant mortality |
| `11be` | **Deaths by ICD-10 3-char codes** | 1998-2023 | **4.2 MB** | 1,900+ specific ICD-10 codes |
| `11bf` | Deaths by ICD-10 (monthly) | 1969M01-2023M12 | 1.0 MB | Monthly data, 65 causes |
| `11bx` | Suicide methods | 2005-2023 | 26 KB | Detailed suicide classification |
| `11by` | Deaths by underlying cause | 1921-2023 | 9 KB | Historical long-term series |
| `11c1` | Perinatal deaths | 1975-2023 | 7 KB | Birth-related mortality |
| `12d9` | Drug-related deaths | 2006-2023 | 10 KB | Specific drug categories |
| `13u5` | Deaths by wellbeing county | 1969-2023 | 425 KB | Regional health administration |

## Key Data Characteristics

### Time Coverage
- **Historical**: Some series go back to 1751 (basic death counts)
- **Modern detailed**: Most cause-of-death data from 1969-1998 onwards
- **Current**: Updated through 2023-2024

### Geographic Coverage
- **National**: All datasets include national totals
- **Regional**: Area-specific data available for 309 regions
- **Administrative**: New wellbeing counties (from 2023 reform)

### Demographic Variables
- **Sex**: Total, Males, Females
- **Age**: Various groupings (1-year, 5-year, specific ranges)
- **Time**: Annual, monthly, historical periods

### Cause Classifications
- **Time Series**: 65 standardized categories for long-term trends
- **ICD-10**: Full international classification (1,900+ codes)
- **External Causes**: Detailed accident/violence categorization
- **Special Topics**: Suicide methods, drug deaths, infant mortality

## Largest Files (>100 MB)
1. **`12as` - Vital statistics by area/month** (819 MB): Comprehensive monthly data for 309 areas with 21 different measures
2. **`11be` - ICD-10 3-character deaths** (4.2 MB): Most detailed cause-of-death classification

## Usage Recommendations

### For Health Research
- **Mortality trends**: Use `12af`, `12al`, `12am` for basic trends
- **Age patterns**: Use `12ag`, `12ak` for age-specific analysis  
- **Geographic analysis**: Use `12ak`, `12au`, `13u5` for regional patterns
- **Cause analysis**: Use `11ay`, `11az`, `11be` for detailed causes

### For Public Health
- **Life expectancy**: Use `12am`, `12an`, `12ap`
- **Infant health**: Use `12aq`, `11bd`, `11c1`
- **External causes**: Use `11b2` for accidents/violence
- **Substance abuse**: Use `11b2`, `12d9` for alcohol/drug deaths

### For Demographics
- **Population**: Use `12at`, `12au` for vital statistics
- **Seasonal patterns**: Use `12ah`, `12as` for monthly data
- **Regional differences**: Use area-specific datasets

## Technical Notes
- **Delimiter**: Semicolon (;) 
- **Encoding**: UTF-8
- **Missing values**: ".." or empty
- **Date formats**: YYYY or YYYYMM
