# Statistics Finland Health Data Documentation

Generated on: 2025-09-16 01:18:57

This document describes the health and mortality datasets downloaded from Statistics Finland (Tilastokeskus) PxWeb API.

## Overview

The data is organized into two main categories:
- **Deaths (kuol)**: General death statistics and demographics
- **Causes of Death (ksyyt)**: Detailed cause-of-death statistics with ICD-10 classifications

Total datasets: 23

## Dataset Details

### Deaths Statistics (kuol)

#### statfin_kuol_pxt_12af.px

**Title**: Deaths by Year, Sex and Information

**File**: `statfin_kuol_pxt_12af.csv` (0.0 MB)

**Description**: 
Statistical table 12af from Statistics Finland.

**Variables**:
- **Year** (`Vuosi`): 274 categories
  - Time dimension: 1751 to 2024
- **Sex** (`Sukupuoli`): 3 categories
  - Values: Total, Males, Females
- **Information** (`Tiedot`): 1 categories
  - Values: Deaths

**Data Structure**:
- Columns: 1
- Sample row count: 274+
- Headers: Year,"Total Deaths"

**Sample Data**:
```
Year,"Total Deaths"
1751,10475
1752,11400
```

---

#### statfin_kuol_pxt_12ag.px

**Title**: Deaths by Year, Sex, Age and Information

**File**: `statfin_kuol_pxt_12ag.csv` (0.02 MB)

**Description**: 
Statistical table 12ag from Statistics Finland.

**Variables**:
- **Year** (`Vuosi`): 45 categories
  - Time dimension: 1980 to 2024
- **Sex** (`Sukupuoli`): 3 categories
  - Values: Total, Males, Females
- **Age** (`Ikä`): 114 categories
- **Information** (`Tiedot`): 1 categories
  - Values: Deaths

**Data Structure**:
- Columns: 1
- Sample row count: 45+
- Headers: Year,"Sex","Total Deaths","0 Deaths","1 Deaths","2 Deaths","3 Deaths","4 Deaths","5 Deaths","6 Deaths","7 Deaths","8 Deaths","9 Deaths","10 Deaths","11 Deaths","12 Deaths","13 Deaths","14 Deaths","15 Deaths","16 Deaths","17 Deaths","18 Deaths","19 Deaths","20 Deaths","21 Deaths","22 Deaths","23 Deaths","24 Deaths","25 Deaths","26 Deaths","27 Deaths","28 Deaths","29 Deaths","30 Deaths","31 Deaths","32 Deaths","33 Deaths","34 Deaths","35 Deaths","36 Deaths","37 Deaths","38 Deaths","39 Deaths","40 Deaths","41 Deaths","42 Deaths","43 Deaths","44 Deaths","45 Deaths","46 Deaths","47 Deaths","48 Deaths","49 Deaths","50 Deaths","51 Deaths","52 Deaths","53 Deaths","54 Deaths","55 Deaths","56 Deaths","57 Deaths","58 Deaths","59 Deaths","60 Deaths","61 Deaths","62 Deaths","63 Deaths","64 Deaths","65 Deaths","66 Deaths","67 Deaths","68 Deaths","69 Deaths","70 Deaths","71 Deaths","72 Deaths","73 Deaths","74 Deaths","75 Deaths","76 Deaths","77 Deaths","78 Deaths","79 Deaths","80 Deaths","81 Deaths","82 Deaths","83 Deaths","84 Deaths","85 Deaths","86 Deaths","87 Deaths","88 Deaths","89 Deaths","90 Deaths","91 Deaths","92 Deaths","93 Deaths","94 Deaths","95 Deaths","96 Deaths","97 Deaths","98 Deaths","99 Deaths","100 Deaths","101 Deaths","102 Deaths","103 Deaths","104 Deaths","105 Deaths","106 Deaths","107 Deaths","108 Deaths","109 Deaths","110 Deaths","111 Deaths","112 Deaths"

**Sample Data**:
```
Year,"Sex","Total Deaths","0 Deaths","1 Deaths","2 Deaths","3 Deaths","4 Deaths","5 Deaths","6 Deaths","7 Deaths","8 Deaths","9 Deaths","10 Deaths","11 Deaths","12 Deaths","13 Deaths","14 Deaths","15 Deaths","16 Deaths","17 Deaths","18 Deaths","19 Deaths","20 Deaths","21 Deaths","22 Deaths","23 Deaths","24 Deaths","25 Deaths","26 Deaths","27 Deaths","28 Deaths","29 Deaths","30 Deaths","31 Deaths","32 Deaths","33 Deaths","34 Deaths","35 Deaths","36 Deaths","37 Deaths","38 Deaths","39 Deaths","40 Deaths","41 Deaths","42 Deaths","43 Deaths","44 Deaths","45 Deaths","46 Deaths","47 Deaths","48 Deaths","49 Deaths","50 Deaths","51 Deaths","52 Deaths","53 Deaths","54 Deaths","55 Deaths","56 Deaths","57 Deaths","58 Deaths","59 Deaths","60 Deaths","61 Deaths","62 Deaths","63 Deaths","64 Deaths","65 Deaths","66 Deaths","67 Deaths","68 Deaths","69 Deaths","70 Deaths","71 Deaths","72 Deaths","73 Deaths","74 Deaths","75 Deaths","76 Deaths","77 Deaths","78 Deaths","79 Deaths","80 Deaths","81 Deaths","82 Deaths","83 Deaths","84 Deaths","85 Deaths","86 Deaths","87 Deaths","88 Deaths","89 Deaths","90 Deaths","91 Deaths","92 Deaths","93 Deaths","94 Deaths","95 Deaths","96 Deaths","97 Deaths","98 Deaths","99 Deaths","100 Deaths","101 Deaths","102 Deaths","103 Deaths","104 Deaths","105 Deaths","106 Deaths","107 Deaths","108 Deaths","109 Deaths","110 Deaths","111 Deaths","112 Deaths"
1980,"Total",44398,481,37,21,20,18,16,15,16,11,12,15,17,13,13,19,31,48,45,53,52,59,76,56,69,78,83,76,80,88,97,86,111,132,121,139,100,113,100,118,124,131,151,153,149,187,204,167,214,216,261,357,361,358,422,470,462,522,533,585,619,636,590,728,724,786,915,993,1093,1172,1283,1317,1392,1478,1518,1496,1553,1454,1441,1370,1402,1380,1432,1290,1166,1080,955,831,713,642,534,386,314,301,209,163,95,76,43,26,14,15,6,1,3,1,0,0,0,0,0,0,0,0
1981,"Total",44404,412,39,17,19,11,19,13,14,24,18,14,18,17,17,21,35,34,41,58,53,44,50,47,58,72,76,77,79,88,94,94,99,125,142,153,127,102,117,106,105,126,142,175,152,150,212,201,223,232,254,339,341,380,411,444,494,484,564,586,624,655,697,587,751,830,856,931,1017,1151,1262,1293,1372,1440,1489,1471,1519,1517,1467,1405,1449,1430,1410,1367,1195,1088,1043,838,661,623,569,433,333,288,227,163,94,73,52,39,15,4,6,6,1,3,1,0,0,0,0,0,0,0
```

---

#### statfin_kuol_pxt_12ah.px

**Title**: Deaths by Year, Month of occurrence and Information

**File**: `statfin_kuol_pxt_12ah.csv` (0.01 MB)

**Description**: 
Statistical table 12ah from Statistics Finland.

**Variables**:
- **Year** (`Vuosi`): 80 categories
  - Time dimension: 1945 to 2024
- **Month of occurrence** (`Tapahtumakuukausi`): 13 categories
- **Information** (`Tiedot`): 1 categories
  - Values: Deaths

**Data Structure**:
- Columns: 1
- Sample row count: 80+
- Headers: Year,"Months total Deaths","January Deaths","February Deaths","March Deaths","April Deaths","May Deaths","June Deaths","July Deaths","August Deaths","September Deaths","October Deaths","November Deaths","December Deaths"

**Sample Data**:
```
Year,"Months total Deaths","January Deaths","February Deaths","March Deaths","April Deaths","May Deaths","June Deaths","July Deaths","August Deaths","September Deaths","October Deaths","November Deaths","December Deaths"
1945,49046,4660,4495,4680,4196,4143,3839,3734,3603,3681,3921,3733,4361
1946,44748,4346,4040,4435,4077,3870,3538,3242,3046,3109,3631,3621,3793
```

---

#### statfin_kuol_pxt_12ak.px

**Title**: Deaths by Year, Area, Sex, Age and Information

**File**: `statfin_kuol_pxt_12ak.csv` (0.73 MB)

**Description**: 
Statistical table 12ak from Statistics Finland.

**Variables**:
- **Year** (`Vuosi`): 35 categories
  - Time dimension: 1990 to 2024
- **Area** (`Alue`): 309 categories
- **Sex** (`Sukupuoli`): 3 categories
  - Values: Total, Males, Females
- **Age** (`Ikä`): 22 categories
- **Information** (`Tiedot`): 1 categories
  - Values: Deaths

**Data Structure**:
- Columns: 1
- Sample row count: 1,002+
- Headers: Year,"Area","Total Total Deaths","Total 0 Deaths","Total 1 - 4 Deaths","Total 5 - 9 Deaths","Total 10 - 14 Deaths","Total 15 - 19 Deaths","Total 20 - 24 Deaths","Total 25 - 29 Deaths","Total 30 - 34 Deaths","Total 35 - 39 Deaths","Total 40 - 44 Deaths","Total 45 - 49 Deaths","Total 50 - 54 Deaths","Total 55 - 59 Deaths","Total 60 - 64 Deaths","Total 65 - 69 Deaths","Total 70 - 74 Deaths","Total 75 - 79 Deaths","Total 80 - 84 Deaths","Total 85 - 89 Deaths","Total 90 - 94 Deaths","Total 95 - Deaths"

**Sample Data**:
```
Year,"Area","Total Total Deaths","Total 0 Deaths","Total 1 - 4 Deaths","Total 5 - 9 Deaths","Total 10 - 14 Deaths","Total 15 - 19 Deaths","Total 20 - 24 Deaths","Total 25 - 29 Deaths","Total 30 - 34 Deaths","Total 35 - 39 Deaths","Total 40 - 44 Deaths","Total 45 - 49 Deaths","Total 50 - 54 Deaths","Total 55 - 59 Deaths","Total 60 - 64 Deaths","Total 65 - 69 Deaths","Total 70 - 74 Deaths","Total 75 - 79 Deaths","Total 80 - 84 Deaths","Total 85 - 89 Deaths","Total 90 - 94 Deaths","Total 95 - Deaths"
1990,"WHOLE COUNTRY",50058,370,67,68,64,231,375,351,520,753,1254,1222,1640,2225,3564,4884,5891,8136,8863,6247,2689,644
1990,"Akaa",191,1,0,0,0,0,0,4,2,2,2,4,5,11,8,17,21,35,43,25,10,1
```

---

#### statfin_kuol_pxt_12al.px

**Title**: Crude death rate by Year and Information

**File**: `statfin_kuol_pxt_12al.csv` (0.01 MB)

**Description**: 
Statistical table 12al from Statistics Finland.

**Variables**:
- **Year** (`Vuosi`): 274 categories
  - Time dimension: 1751 to 2024
- **Information** (`Tiedot`): 3 categories
  - Values: Crude death rate, per mille, Deaths, Mean population

**Data Structure**:
- Columns: 1
- Sample row count: 274+
- Headers: Year,"Crude death rate, per mille","Deaths","Mean population"

**Sample Data**:
```
Year,"Crude death rate, per mille","Deaths","Mean population"
1751,24.6,10475,425700.0
1752,26.3,11400,433750.0
```

---

#### statfin_kuol_pxt_12am.px

**Title**: Life expectancy at birth by Year, Sex and Information

**File**: `statfin_kuol_pxt_12am.csv` (0.0 MB)

**Description**: 
Statistical table 12am from Statistics Finland.

**Variables**:
- **Year** (`Vuosi`): 79 categories
  - Time dimension: 1751 to 2024
- **Sex** (`Sukupuoli`): 3 categories
  - Values: Total, Males, Females
- **Information** (`Tiedot`): 1 categories
  - Values: Life expectancy at birth, years

**Data Structure**:
- Columns: 1
- Sample row count: 79+
- Headers: Year,"Total Life expectancy at birth, years"

**Sample Data**:
```
Year,"Total Life expectancy at birth, years"
1751-1760,.
1761-1770,.
```

---

#### statfin_kuol_pxt_12an.px

**Title**: Life expectancy at birth by Year, Region, Sex and Information

**File**: `statfin_kuol_pxt_12an.csv` (0.03 MB)

**Description**: 
Statistical table 12an from Statistics Finland.

**Variables**:
- **Year** (`Vuosi`): 32 categories
  - Time dimension: 1992 to 2023
- **Region** (`Maakunta`): 22 categories
- **Sex** (`Sukupuoli`): 3 categories
  - Values: Total, Males, Females
- **Information** (`Tiedot`): 1 categories
  - Values: Life expectancy at birth, years

**Data Structure**:
- Columns: 1
- Sample row count: 704+
- Headers: Year,"Region","Total Life expectancy at birth, years"

**Sample Data**:
```
Year,"Region","Total Life expectancy at birth, years"
1990-1992,"WHOLE COUNTRY",75.34
1990-1992,"MA1 MAINLAND FINLAND",75.32
```

---

#### statfin_kuol_pxt_12ap.px

**Title**: Life table by Year, Sex, Age and Information

**File**: `statfin_kuol_pxt_12ap.csv` (0.15 MB)

**Description**: 
Statistical table 12ap from Statistics Finland.

**Variables**:
- **Year** (`Vuosi`): 38 categories
  - Time dimension: 1986 to 2023
- **Sex** (`Sukupuoli`): 3 categories
  - Values: Total, Males, Females
- **Age** (`Ikä`): 101 categories
- **Information** (`Tiedot`): 3 categories
  - Values: Probability of death, per mille, Survivors of 100,000 born alive, Life expectancy, years

**Data Structure**:
- Columns: 1
- Sample row count: 1,002+
- Headers: Year,"Sex","Age","Probability of death, per mille","Survivors of 100,000 born alive","Life expectancy, years"

**Sample Data**:
```
Year,"Sex","Age","Probability of death, per mille","Survivors of 100,000 born alive","Life expectancy, years"
1986,"Total","0",5.84,100000,74.70
1986,"Total","1",0.36,99416,74.14
```

---

#### statfin_kuol_pxt_12aq.px

**Title**: Infant mortality by Year, Sex and Information

**File**: `statfin_kuol_pxt_12aq.csv` (0.0 MB)

**Description**: 
Statistical table 12aq from Statistics Finland.

**Variables**:
- **Year** (`Vuosi`): 274 categories
  - Time dimension: 1751 to 2024
- **Sex** (`Sukupuoli`): 3 categories
  - Values: Total, Males, Females
- **Information** (`Tiedot`): 2 categories
  - Values: Infant mortality, per mille, Infant deaths

**Data Structure**:
- Columns: 1
- Sample row count: 274+
- Headers: Year,"Total Infant mortality, per mille","Total Infant deaths"

**Sample Data**:
```
Year,"Total Infant mortality, per mille","Total Infant deaths"
1751,206.5,.
1752,224.8,.
```

---

#### statfin_kuol_pxt_12as.px

**Title**: Vital statistics by Area, Information and Month

**File**: `statfin_kuol_pxt_12as.csv` (819.09 MB)

**Description**: 
Statistical table 12as from Statistics Finland.

**Variables**:
- **Area** (`Alue`): 309 categories
- **Information** (`Tiedot`): 21 categories
- **Month** (`Kuukausi`): 420 categories
  - Time dimension: 1990M01 to 2024M12

**Data Structure**:
- Columns: 1
- Sample row count: 1,002+
- Headers: Area,"Information","1990M01","1990M02","1990M03","1990M04","1990M05","1990M06","1990M07","1990M08"

**Sample Data**:
```
Area,"Information","1990M01","1990M02","1990M03","1990M04","1990M05","1990M06","1990M07","1990M08"
WHOLE COUNTRY,"Live births",5353,5058,5958,5528,5792,5595,5674,5617
WHOLE COUNTRY,"Deaths",5105,4072,4201,3922,4074,4142,4082,3895
```

---

#### statfin_kuol_pxt_12at.px

**Title**: Vital statistics by Year and Information

**File**: `statfin_kuol_pxt_12at.csv` (0.02 MB)

**Description**: 
Statistical table 12at from Statistics Finland.

**Variables**:
- **Year** (`Vuosi`): 276 categories
- **Information** (`Tiedot`): 11 categories

**Data Structure**:
- Columns: 1
- Sample row count: 276+
- Headers: Year,"Live births","Deaths","Natural increase","Intermunicipal migration","Immigration to Finland","Emigration from Finland","Net migration","Marriages","Divorces","Total change","Population"

**Sample Data**:
```
Year,"Live births","Deaths","Natural increase","Intermunicipal migration","Immigration to Finland","Emigration from Finland","Net migration","Marriages","Divorces","Total change","Population"
1749,16700,11600,5100,.,.,.,.,3900,.,.,410400
1750,17800,11300,6500,.,.,.,.,4700,.,11137,421537
```

---

#### statfin_kuol_pxt_12au.px

**Title**: Vital statistics by Year, Area and Information

**File**: `statfin_kuol_pxt_12au.csv` (0.92 MB)

**Description**: 
Statistical table 12au from Statistics Finland.

**Variables**:
- **Year** (`Vuosi`): 35 categories
  - Time dimension: 1990 to 2024
- **Area** (`Alue`): 309 categories
- **Information** (`Tiedot`): 21 categories

**Data Structure**:
- Columns: 1
- Sample row count: 1,002+
- Headers: Year,"Area","Live births","Deaths","Natural increase","Intermunicipal in-migration","Intermunicipal out-migration","Intermunicipal net migration","Intramunicipal migration","Immigration to Finland","Immigration to Finland from Nordic countries","Immigration to Finland from EU countries","Emigration from Finland","Emigration from Finland to Nordic countries","Emigration from Finland to EU countries","Net migration","Total net migration","Marriages","Divorces","Population increase","Population correction","Total change","Population"

**Sample Data**:
```
Year,"Area","Live births","Deaths","Natural increase","Intermunicipal in-migration","Intermunicipal out-migration","Intermunicipal net migration","Intramunicipal migration","Immigration to Finland","Immigration to Finland from Nordic countries","Immigration to Finland from EU countries","Emigration from Finland","Emigration from Finland to Nordic countries","Emigration from Finland to EU countries","Net migration","Total net migration","Marriages","Divorces","Population increase","Population correction","Total change","Population"
1990,"WHOLE COUNTRY",65549,50058,15491,173897,173897,0,392677,13558,6571,7688,6477,4464,5237,7081,7081,25815,13170,22572,1523,24095,4998478
1990,"Akaa",206,191,15,572,527,45,1234,67,20,52,28,23,23,39,84,68,51,99,12,111,16048
```

---


### Causes of Death Statistics (ksyyt)

#### statfin_ksyyt_pxt_11ay.px

**Title**: Deaths/deaths rates by Sex, Underlying cause of death (time series classification), Year and Information

**File**: `statfin_ksyyt_pxt_11ay.csv` (0.35 MB)

**Description**: 
Statistical table 11ay from Statistics Finland.

**Variables**:
- **Sex** (`Sukupuoli`): 3 categories
  - Values: Total, Males, Females
- **Underlying cause of death (time series classification)** (`Tilaston peruskuolemansyy (aikasarjaluokitus)`): 65 categories
- **Year** (`Vuosi`): 53 categories
  - Time dimension: 1971 to 2023
- **Information** (`Tiedot`): 8 categories
  - Values: Deaths, whole population, Age-standardised death rate, whole population (1/100 000), Crude death rate, whole population (1/100 000), Age-standardised death rate, whole population, annual change (%), Deaths, aged 15-64...

**Data Structure**:
- Columns: 1
- Sample row count: 1,002+
- Headers: Sex,"Underlying cause of death (time series classification)","Year","Deaths, whole population","Age-standardised death rate, whole population (1/100 000)","Crude death rate, whole population (1/100 000)","Age-standardised death rate, whole population, annual change (%)","Deaths, aged 15-64","Age-standardised death rate, aged 15-64 (1/100 000)","Crude death rate, aged 15-64 (1/100 000)","Age-standardised death rate, aged 15-64, annual change (%)"

**Sample Data**:
```
Sex,"Underlying cause of death (time series classification)","Year","Deaths, whole population","Age-standardised death rate, whole population (1/100 000)","Crude death rate, whole population (1/100 000)","Age-standardised death rate, whole population, annual change (%)","Deaths, aged 15-64","Age-standardised death rate, aged 15-64 (1/100 000)","Crude death rate, aged 15-64 (1/100 000)","Age-standardised death rate, aged 15-64, annual change (%)"
Total,"00-54 Total","1971",45876,2259.7,994.7,..,15696,611.2,511.2,..
Total,"00-54 Total","1972",43958,2131.2,947.4,-5.7,14884,574.8,479.5,-6.0
```

---

#### statfin_ksyyt_pxt_11az.px

**Title**: Deaths by Underlying cause of death (time series classification), Age, Sex, Year and Information

**File**: `statfin_ksyyt_pxt_11az.csv` (0.34 MB)

**Description**: 
Statistical table 11az from Statistics Finland.

**Variables**:
- **Underlying cause of death (time series classification)** (`Tilaston peruskuolemansyy (aikasarjaluokitus)`): 65 categories
- **Age** (`Ikä`): 25 categories
- **Sex** (`Sukupuoli`): 3 categories
  - Values: Total, Males, Females
- **Year** (`Vuosi`): 55 categories
  - Time dimension: 1969 to 2023
- **Information** (`Tiedot`): 1 categories
  - Values: Deaths

**Data Structure**:
- Columns: 1
- Sample row count: 1,002+
- Headers: Underlying cause of death (time series classification),"Age","Total 1969 Deaths","Total 1970 Deaths","Total 1971 Deaths","Total 1972 Deaths","Total 1973 Deaths","Total 1974 Deaths","Total 1975 Deaths","Total 1976 Deaths","Total 1977 Deaths","Total 1978 Deaths","Total 1979 Deaths","Total 1980 Deaths","Total 1981 Deaths","Total 1982 Deaths","Total 1983 Deaths","Total 1984 Deaths","Total 1985 Deaths","Total 1986 Deaths","Total 1987 Deaths","Total 1988 Deaths","Total 1989 Deaths","Total 1990 Deaths","Total 1991 Deaths","Total 1992 Deaths","Total 1993 Deaths","Total 1994 Deaths","Total 1995 Deaths","Total 1996 Deaths","Total 1997 Deaths","Total 1998 Deaths","Total 1999 Deaths","Total 2000 Deaths","Total 2001 Deaths","Total 2002 Deaths","Total 2003 Deaths","Total 2004 Deaths","Total 2005 Deaths","Total 2006 Deaths","Total 2007 Deaths","Total 2008 Deaths","Total 2009 Deaths","Total 2010 Deaths","Total 2011 Deaths","Total 2012 Deaths","Total 2013 Deaths","Total 2014 Deaths","Total 2015 Deaths","Total 2016 Deaths","Total 2017 Deaths","Total 2018 Deaths","Total 2019 Deaths","Total 2020 Deaths","Total 2021 Deaths","Total 2022 Deaths","Total 2023 Deaths"

**Sample Data**:
```
Underlying cause of death (time series classification),"Age","Total 1969 Deaths","Total 1970 Deaths","Total 1971 Deaths","Total 1972 Deaths","Total 1973 Deaths","Total 1974 Deaths","Total 1975 Deaths","Total 1976 Deaths","Total 1977 Deaths","Total 1978 Deaths","Total 1979 Deaths","Total 1980 Deaths","Total 1981 Deaths","Total 1982 Deaths","Total 1983 Deaths","Total 1984 Deaths","Total 1985 Deaths","Total 1986 Deaths","Total 1987 Deaths","Total 1988 Deaths","Total 1989 Deaths","Total 1990 Deaths","Total 1991 Deaths","Total 1992 Deaths","Total 1993 Deaths","Total 1994 Deaths","Total 1995 Deaths","Total 1996 Deaths","Total 1997 Deaths","Total 1998 Deaths","Total 1999 Deaths","Total 2000 Deaths","Total 2001 Deaths","Total 2002 Deaths","Total 2003 Deaths","Total 2004 Deaths","Total 2005 Deaths","Total 2006 Deaths","Total 2007 Deaths","Total 2008 Deaths","Total 2009 Deaths","Total 2010 Deaths","Total 2011 Deaths","Total 2012 Deaths","Total 2013 Deaths","Total 2014 Deaths","Total 2015 Deaths","Total 2016 Deaths","Total 2017 Deaths","Total 2018 Deaths","Total 2019 Deaths","Total 2020 Deaths","Total 2021 Deaths","Total 2022 Deaths","Total 2023 Deaths"
00-54 Total,"Total",45966,44119,45876,43958,43411,44673,43866,44857,44264,43817,43857,44511,44528,43584,45517,45176,48347,47306,47988,49092,49132,50091,49319,49856,51033,47946,49326,49161,49142,49237,49368,49316,48504,49389,49033,47757,47751,48105,49093,49090,49904,50910,50568,51737,51478,52409,52302,53964,53670,54523,53962,55498,57632,63172,61301
00-54 Total,"0 - 14",1562,1399,1310,1218,1093,1115,1076,942,907,805,766,723,679,624,624,641,614,531,574,578,579,565,567,532,455,455,419,405,414,364,372,331,294,280,309,353,313,269,272,265,241,230,239,239,176,212,163,185,182,167,165,145,161,168,157
```

---

#### statfin_ksyyt_pxt_11b2.px

**Title**: Accidental and violent deaths by Accidents and violence (classification of external causes), Age, Year, Sex and Information

**File**: `statfin_ksyyt_pxt_11b2.csv` (1.2 MB)

**Description**: 
Statistical table 11b2 from Statistics Finland.

**Variables**:
- **Accidents and violence (classification of external causes)** (`Tapaturmat ja väkivalta (ulkoisten syiden luokitus)`): 141 categories
- **Age** (`Ikä`): 22 categories
- **Year** (`Vuosi`): 26 categories
  - Time dimension: 1998 to 2023
- **Sex** (`Sukupuoli`): 3 categories
  - Values: Total, Males, Females
- **Information** (`Tiedot`): 5 categories
  - Values: Total accidental and violent deaths, Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total, Deaths accompanied by alcohol intoxication from accidents and violence, Deaths accompanied by alcohol and drug intoxication from accidents and violence, Deaths accompanied by drug intoxication from accidents and violence

**Data Structure**:
- Columns: 1
- Sample row count: 1,002+
- Headers: Accidents and violence (classification of external causes),"Age","1998 Total Total accidental and violent deaths","1998 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","1998 Total Deaths accompanied by alcohol intoxication from accidents and violence","1998 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","1998 Total Deaths accompanied by drug intoxication from accidents and violence","1999 Total Total accidental and violent deaths","1999 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","1999 Total Deaths accompanied by alcohol intoxication from accidents and violence","1999 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","1999 Total Deaths accompanied by drug intoxication from accidents and violence","2000 Total Total accidental and violent deaths","2000 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2000 Total Deaths accompanied by alcohol intoxication from accidents and violence","2000 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2000 Total Deaths accompanied by drug intoxication from accidents and violence","2001 Total Total accidental and violent deaths","2001 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2001 Total Deaths accompanied by alcohol intoxication from accidents and violence","2001 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2001 Total Deaths accompanied by drug intoxication from accidents and violence","2002 Total Total accidental and violent deaths","2002 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2002 Total Deaths accompanied by alcohol intoxication from accidents and violence","2002 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2002 Total Deaths accompanied by drug intoxication from accidents and violence","2003 Total Total accidental and violent deaths","2003 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2003 Total Deaths accompanied by alcohol intoxication from accidents and violence","2003 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2003 Total Deaths accompanied by drug intoxication from accidents and violence","2004 Total Total accidental and violent deaths","2004 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2004 Total Deaths accompanied by alcohol intoxication from accidents and violence","2004 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2004 Total Deaths accompanied by drug intoxication from accidents and violence","2005 Total Total accidental and violent deaths","2005 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2005 Total Deaths accompanied by alcohol intoxication from accidents and violence","2005 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2005 Total Deaths accompanied by drug intoxication from accidents and violence","2006 Total Total accidental and violent deaths","2006 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2006 Total Deaths accompanied by alcohol intoxication from accidents and violence","2006 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2006 Total Deaths accompanied by drug intoxication from accidents and violence","2007 Total Total accidental and violent deaths","2007 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2007 Total Deaths accompanied by alcohol intoxication from accidents and violence","2007 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2007 Total Deaths accompanied by drug intoxication from accidents and violence","2008 Total Total accidental and violent deaths","2008 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2008 Total Deaths accompanied by alcohol intoxication from accidents and violence","2008 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2008 Total Deaths accompanied by drug intoxication from accidents and violence","2009 Total Total accidental and violent deaths","2009 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2009 Total Deaths accompanied by alcohol intoxication from accidents and violence","2009 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2009 Total Deaths accompanied by drug intoxication from accidents and violence","2010 Total Total accidental and violent deaths","2010 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2010 Total Deaths accompanied by alcohol intoxication from accidents and violence","2010 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2010 Total Deaths accompanied by drug intoxication from accidents and violence","2011 Total Total accidental and violent deaths","2011 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2011 Total Deaths accompanied by alcohol intoxication from accidents and violence","2011 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2011 Total Deaths accompanied by drug intoxication from accidents and violence","2012 Total Total accidental and violent deaths","2012 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2012 Total Deaths accompanied by alcohol intoxication from accidents and violence","2012 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2012 Total Deaths accompanied by drug intoxication from accidents and violence","2013 Total Total accidental and violent deaths","2013 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2013 Total Deaths accompanied by alcohol intoxication from accidents and violence","2013 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2013 Total Deaths accompanied by drug intoxication from accidents and violence","2014 Total Total accidental and violent deaths","2014 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2014 Total Deaths accompanied by alcohol intoxication from accidents and violence","2014 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2014 Total Deaths accompanied by drug intoxication from accidents and violence","2015 Total Total accidental and violent deaths","2015 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2015 Total Deaths accompanied by alcohol intoxication from accidents and violence","2015 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2015 Total Deaths accompanied by drug intoxication from accidents and violence","2016 Total Total accidental and violent deaths","2016 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2016 Total Deaths accompanied by alcohol intoxication from accidents and violence","2016 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2016 Total Deaths accompanied by drug intoxication from accidents and violence","2017 Total Total accidental and violent deaths","2017 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2017 Total Deaths accompanied by alcohol intoxication from accidents and violence","2017 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2017 Total Deaths accompanied by drug intoxication from accidents and violence","2018 Total Total accidental and violent deaths","2018 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2018 Total Deaths accompanied by alcohol intoxication from accidents and violence","2018 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2018 Total Deaths accompanied by drug intoxication from accidents and violence","2019 Total Total accidental and violent deaths","2019 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2019 Total Deaths accompanied by alcohol intoxication from accidents and violence","2019 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2019 Total Deaths accompanied by drug intoxication from accidents and violence","2020 Total Total accidental and violent deaths","2020 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2020 Total Deaths accompanied by alcohol intoxication from accidents and violence","2020 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2020 Total Deaths accompanied by drug intoxication from accidents and violence","2021 Total Total accidental and violent deaths","2021 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2021 Total Deaths accompanied by alcohol intoxication from accidents and violence","2021 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2021 Total Deaths accompanied by drug intoxication from accidents and violence","2022 Total Total accidental and violent deaths","2022 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2022 Total Deaths accompanied by alcohol intoxication from accidents and violence","2022 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2022 Total Deaths accompanied by drug intoxication from accidents and violence","2023 Total Total accidental and violent deaths","2023 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2023 Total Deaths accompanied by alcohol intoxication from accidents and violence","2023 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2023 Total Deaths accompanied by drug intoxication from accidents and violence"

**Sample Data**:
```
Accidents and violence (classification of external causes),"Age","1998 Total Total accidental and violent deaths","1998 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","1998 Total Deaths accompanied by alcohol intoxication from accidents and violence","1998 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","1998 Total Deaths accompanied by drug intoxication from accidents and violence","1999 Total Total accidental and violent deaths","1999 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","1999 Total Deaths accompanied by alcohol intoxication from accidents and violence","1999 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","1999 Total Deaths accompanied by drug intoxication from accidents and violence","2000 Total Total accidental and violent deaths","2000 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2000 Total Deaths accompanied by alcohol intoxication from accidents and violence","2000 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2000 Total Deaths accompanied by drug intoxication from accidents and violence","2001 Total Total accidental and violent deaths","2001 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2001 Total Deaths accompanied by alcohol intoxication from accidents and violence","2001 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2001 Total Deaths accompanied by drug intoxication from accidents and violence","2002 Total Total accidental and violent deaths","2002 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2002 Total Deaths accompanied by alcohol intoxication from accidents and violence","2002 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2002 Total Deaths accompanied by drug intoxication from accidents and violence","2003 Total Total accidental and violent deaths","2003 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2003 Total Deaths accompanied by alcohol intoxication from accidents and violence","2003 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2003 Total Deaths accompanied by drug intoxication from accidents and violence","2004 Total Total accidental and violent deaths","2004 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2004 Total Deaths accompanied by alcohol intoxication from accidents and violence","2004 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2004 Total Deaths accompanied by drug intoxication from accidents and violence","2005 Total Total accidental and violent deaths","2005 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2005 Total Deaths accompanied by alcohol intoxication from accidents and violence","2005 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2005 Total Deaths accompanied by drug intoxication from accidents and violence","2006 Total Total accidental and violent deaths","2006 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2006 Total Deaths accompanied by alcohol intoxication from accidents and violence","2006 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2006 Total Deaths accompanied by drug intoxication from accidents and violence","2007 Total Total accidental and violent deaths","2007 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2007 Total Deaths accompanied by alcohol intoxication from accidents and violence","2007 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2007 Total Deaths accompanied by drug intoxication from accidents and violence","2008 Total Total accidental and violent deaths","2008 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2008 Total Deaths accompanied by alcohol intoxication from accidents and violence","2008 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2008 Total Deaths accompanied by drug intoxication from accidents and violence","2009 Total Total accidental and violent deaths","2009 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2009 Total Deaths accompanied by alcohol intoxication from accidents and violence","2009 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2009 Total Deaths accompanied by drug intoxication from accidents and violence","2010 Total Total accidental and violent deaths","2010 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2010 Total Deaths accompanied by alcohol intoxication from accidents and violence","2010 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2010 Total Deaths accompanied by drug intoxication from accidents and violence","2011 Total Total accidental and violent deaths","2011 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2011 Total Deaths accompanied by alcohol intoxication from accidents and violence","2011 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2011 Total Deaths accompanied by drug intoxication from accidents and violence","2012 Total Total accidental and violent deaths","2012 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2012 Total Deaths accompanied by alcohol intoxication from accidents and violence","2012 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2012 Total Deaths accompanied by drug intoxication from accidents and violence","2013 Total Total accidental and violent deaths","2013 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2013 Total Deaths accompanied by alcohol intoxication from accidents and violence","2013 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2013 Total Deaths accompanied by drug intoxication from accidents and violence","2014 Total Total accidental and violent deaths","2014 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2014 Total Deaths accompanied by alcohol intoxication from accidents and violence","2014 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2014 Total Deaths accompanied by drug intoxication from accidents and violence","2015 Total Total accidental and violent deaths","2015 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2015 Total Deaths accompanied by alcohol intoxication from accidents and violence","2015 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2015 Total Deaths accompanied by drug intoxication from accidents and violence","2016 Total Total accidental and violent deaths","2016 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2016 Total Deaths accompanied by alcohol intoxication from accidents and violence","2016 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2016 Total Deaths accompanied by drug intoxication from accidents and violence","2017 Total Total accidental and violent deaths","2017 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2017 Total Deaths accompanied by alcohol intoxication from accidents and violence","2017 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2017 Total Deaths accompanied by drug intoxication from accidents and violence","2018 Total Total accidental and violent deaths","2018 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2018 Total Deaths accompanied by alcohol intoxication from accidents and violence","2018 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2018 Total Deaths accompanied by drug intoxication from accidents and violence","2019 Total Total accidental and violent deaths","2019 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2019 Total Deaths accompanied by alcohol intoxication from accidents and violence","2019 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2019 Total Deaths accompanied by drug intoxication from accidents and violence","2020 Total Total accidental and violent deaths","2020 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2020 Total Deaths accompanied by alcohol intoxication from accidents and violence","2020 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2020 Total Deaths accompanied by drug intoxication from accidents and violence","2021 Total Total accidental and violent deaths","2021 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2021 Total Deaths accompanied by alcohol intoxication from accidents and violence","2021 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2021 Total Deaths accompanied by drug intoxication from accidents and violence","2022 Total Total accidental and violent deaths","2022 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2022 Total Deaths accompanied by alcohol intoxication from accidents and violence","2022 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2022 Total Deaths accompanied by drug intoxication from accidents and violence","2023 Total Total accidental and violent deaths","2023 Total Deaths accompanied by alcohol and/or drug intoxication from accidents and violence total","2023 Total Deaths accompanied by alcohol intoxication from accidents and violence","2023 Total Deaths accompanied by alcohol and drug intoxication from accidents and violence","2023 Total Deaths accompanied by drug intoxication from accidents and violence"
001-122 Total,"Total",4277,940,834,68,38,4178,989,857,91,41,4128,872,748,79,45,4166,912,769,79,64,4077,908,766,104,38,4125,904,781,80,43,4353,964,855,71,38,4295,986,841,101,44,4337,1014,884,86,44,4245,901,774,93,34,4277,944,805,101,38,4150,868,768,57,43,4000,795,682,60,53,3866,729,648,44,37,3683,616,545,27,44,3605,678,610,25,43,3477,621,530,40,51,3297,595,494,54,47,3435,638,528,53,57,3480,584,479,54,51,3596,575,487,41,47,3331,528,436,38,54,3277,547,455,38,54,3368,526,423,35,68,3276,480,401,32,47,3430,460,381,31,48
001-122 Total,"0",6,0,0,0,0,1,0,0,0,0,3,0,0,0,0,2,0,0,0,0,5,0,0,0,0,4,0,0,0,0,4,0,0,0,0,2,0,0,0,0,5,0,0,0,0,6,0,0,0,0,2,0,0,0,0,5,0,0,0,0,4,0,0,0,0,6,0,0,0,0,4,0,0,0,0,2,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,1,0,0,0,0,2,0,0,0,0,2,0,0,0,0,1,1,0,0,1,0,0,0,0,0,1,0,0,0,0
```

---

#### statfin_ksyyt_pxt_11bd.px

**Title**: Infant deaths and stillbirths by Underlying cause of death (ICD-10, 3-character level), Year and Information

**File**: `statfin_ksyyt_pxt_11bd.csv` (0.09 MB)

**Description**: 
Statistical table 11bd from Statistics Finland.

**Variables**:
- **Underlying cause of death (ICD-10, 3-character level)** (`Tilaston peruskuolemansyy (ICD-10, 3-merkkitaso)`): 297 categories
- **Year** (`Vuosi`): 26 categories
  - Time dimension: 1998 to 2023
- **Information** (`Tiedot`): 5 categories
  - Values: Stillbirths, Infant deaths, Deaths under 7 days, Deaths between 7 and 27 days, Deaths between 28 days and 11 months

**Data Structure**:
- Columns: 1
- Sample row count: 297+
- Headers: Underlying cause of death (ICD-10, 3-character level),"1998 Stillbirths","1998 Infant deaths","1998 Deaths under 7 days","1998 Deaths between 7 and 27 days","1998 Deaths between 28 days and 11 months","1999 Stillbirths","1999 Infant deaths","1999 Deaths under 7 days","1999 Deaths between 7 and 27 days","1999 Deaths between 28 days and 11 months","2000 Stillbirths","2000 Infant deaths","2000 Deaths under 7 days","2000 Deaths between 7 and 27 days","2000 Deaths between 28 days and 11 months","2001 Stillbirths","2001 Infant deaths","2001 Deaths under 7 days","2001 Deaths between 7 and 27 days","2001 Deaths between 28 days and 11 months","2002 Stillbirths","2002 Infant deaths","2002 Deaths under 7 days","2002 Deaths between 7 and 27 days","2002 Deaths between 28 days and 11 months","2003 Stillbirths","2003 Infant deaths","2003 Deaths under 7 days","2003 Deaths between 7 and 27 days","2003 Deaths between 28 days and 11 months","2004 Stillbirths","2004 Infant deaths","2004 Deaths under 7 days","2004 Deaths between 7 and 27 days","2004 Deaths between 28 days and 11 months","2005 Stillbirths","2005 Infant deaths","2005 Deaths under 7 days","2005 Deaths between 7 and 27 days","2005 Deaths between 28 days and 11 months","2006 Stillbirths","2006 Infant deaths","2006 Deaths under 7 days","2006 Deaths between 7 and 27 days","2006 Deaths between 28 days and 11 months","2007 Stillbirths","2007 Infant deaths","2007 Deaths under 7 days","2007 Deaths between 7 and 27 days","2007 Deaths between 28 days and 11 months","2008 Stillbirths","2008 Infant deaths","2008 Deaths under 7 days","2008 Deaths between 7 and 27 days","2008 Deaths between 28 days and 11 months","2009 Stillbirths","2009 Infant deaths","2009 Deaths under 7 days","2009 Deaths between 7 and 27 days","2009 Deaths between 28 days and 11 months","2010 Stillbirths","2010 Infant deaths","2010 Deaths under 7 days","2010 Deaths between 7 and 27 days","2010 Deaths between 28 days and 11 months","2011 Stillbirths","2011 Infant deaths","2011 Deaths under 7 days","2011 Deaths between 7 and 27 days","2011 Deaths between 28 days and 11 months","2012 Stillbirths","2012 Infant deaths","2012 Deaths under 7 days","2012 Deaths between 7 and 27 days","2012 Deaths between 28 days and 11 months","2013 Stillbirths","2013 Infant deaths","2013 Deaths under 7 days","2013 Deaths between 7 and 27 days","2013 Deaths between 28 days and 11 months","2014 Stillbirths","2014 Infant deaths","2014 Deaths under 7 days","2014 Deaths between 7 and 27 days","2014 Deaths between 28 days and 11 months","2015 Stillbirths","2015 Infant deaths","2015 Deaths under 7 days","2015 Deaths between 7 and 27 days","2015 Deaths between 28 days and 11 months","2016 Stillbirths","2016 Infant deaths","2016 Deaths under 7 days","2016 Deaths between 7 and 27 days","2016 Deaths between 28 days and 11 months","2017 Stillbirths","2017 Infant deaths","2017 Deaths under 7 days","2017 Deaths between 7 and 27 days","2017 Deaths between 28 days and 11 months","2018 Stillbirths","2018 Infant deaths","2018 Deaths under 7 days","2018 Deaths between 7 and 27 days","2018 Deaths between 28 days and 11 months","2019 Stillbirths","2019 Infant deaths","2019 Deaths under 7 days","2019 Deaths between 7 and 27 days","2019 Deaths between 28 days and 11 months","2020 Stillbirths","2020 Infant deaths","2020 Deaths under 7 days","2020 Deaths between 7 and 27 days","2020 Deaths between 28 days and 11 months","2021 Stillbirths","2021 Infant deaths","2021 Deaths under 7 days","2021 Deaths between 7 and 27 days","2021 Deaths between 28 days and 11 months","2022 Stillbirths","2022 Infant deaths","2022 Deaths under 7 days","2022 Deaths between 7 and 27 days","2022 Deaths between 28 days and 11 months","2023 Stillbirths","2023 Infant deaths","2023 Deaths under 7 days","2023 Deaths between 7 and 27 days","2023 Deaths between 28 days and 11 months"

**Sample Data**:
```
Underlying cause of death (ICD-10, 3-character level),"1998 Stillbirths","1998 Infant deaths","1998 Deaths under 7 days","1998 Deaths between 7 and 27 days","1998 Deaths between 28 days and 11 months","1999 Stillbirths","1999 Infant deaths","1999 Deaths under 7 days","1999 Deaths between 7 and 27 days","1999 Deaths between 28 days and 11 months","2000 Stillbirths","2000 Infant deaths","2000 Deaths under 7 days","2000 Deaths between 7 and 27 days","2000 Deaths between 28 days and 11 months","2001 Stillbirths","2001 Infant deaths","2001 Deaths under 7 days","2001 Deaths between 7 and 27 days","2001 Deaths between 28 days and 11 months","2002 Stillbirths","2002 Infant deaths","2002 Deaths under 7 days","2002 Deaths between 7 and 27 days","2002 Deaths between 28 days and 11 months","2003 Stillbirths","2003 Infant deaths","2003 Deaths under 7 days","2003 Deaths between 7 and 27 days","2003 Deaths between 28 days and 11 months","2004 Stillbirths","2004 Infant deaths","2004 Deaths under 7 days","2004 Deaths between 7 and 27 days","2004 Deaths between 28 days and 11 months","2005 Stillbirths","2005 Infant deaths","2005 Deaths under 7 days","2005 Deaths between 7 and 27 days","2005 Deaths between 28 days and 11 months","2006 Stillbirths","2006 Infant deaths","2006 Deaths under 7 days","2006 Deaths between 7 and 27 days","2006 Deaths between 28 days and 11 months","2007 Stillbirths","2007 Infant deaths","2007 Deaths under 7 days","2007 Deaths between 7 and 27 days","2007 Deaths between 28 days and 11 months","2008 Stillbirths","2008 Infant deaths","2008 Deaths under 7 days","2008 Deaths between 7 and 27 days","2008 Deaths between 28 days and 11 months","2009 Stillbirths","2009 Infant deaths","2009 Deaths under 7 days","2009 Deaths between 7 and 27 days","2009 Deaths between 28 days and 11 months","2010 Stillbirths","2010 Infant deaths","2010 Deaths under 7 days","2010 Deaths between 7 and 27 days","2010 Deaths between 28 days and 11 months","2011 Stillbirths","2011 Infant deaths","2011 Deaths under 7 days","2011 Deaths between 7 and 27 days","2011 Deaths between 28 days and 11 months","2012 Stillbirths","2012 Infant deaths","2012 Deaths under 7 days","2012 Deaths between 7 and 27 days","2012 Deaths between 28 days and 11 months","2013 Stillbirths","2013 Infant deaths","2013 Deaths under 7 days","2013 Deaths between 7 and 27 days","2013 Deaths between 28 days and 11 months","2014 Stillbirths","2014 Infant deaths","2014 Deaths under 7 days","2014 Deaths between 7 and 27 days","2014 Deaths between 28 days and 11 months","2015 Stillbirths","2015 Infant deaths","2015 Deaths under 7 days","2015 Deaths between 7 and 27 days","2015 Deaths between 28 days and 11 months","2016 Stillbirths","2016 Infant deaths","2016 Deaths under 7 days","2016 Deaths between 7 and 27 days","2016 Deaths between 28 days and 11 months","2017 Stillbirths","2017 Infant deaths","2017 Deaths under 7 days","2017 Deaths between 7 and 27 days","2017 Deaths between 28 days and 11 months","2018 Stillbirths","2018 Infant deaths","2018 Deaths under 7 days","2018 Deaths between 7 and 27 days","2018 Deaths between 28 days and 11 months","2019 Stillbirths","2019 Infant deaths","2019 Deaths under 7 days","2019 Deaths between 7 and 27 days","2019 Deaths between 28 days and 11 months","2020 Stillbirths","2020 Infant deaths","2020 Deaths under 7 days","2020 Deaths between 7 and 27 days","2020 Deaths between 28 days and 11 months","2021 Stillbirths","2021 Infant deaths","2021 Deaths under 7 days","2021 Deaths between 7 and 27 days","2021 Deaths between 28 days and 11 months","2022 Stillbirths","2022 Infant deaths","2022 Deaths under 7 days","2022 Deaths between 7 and 27 days","2022 Deaths between 28 days and 11 months","2023 Stillbirths","2023 Infant deaths","2023 Deaths under 7 days","2023 Deaths between 7 and 27 days","2023 Deaths between 28 days and 11 months"
A00-Y89 Total,237,236,136,33,67,208,213,121,33,59,228,205,97,39,69,208,181,98,24,59,213,165,91,26,48,178,182,98,22,62,187,193,113,29,51,182,179,104,21,54,193,168,91,28,49,204,159,94,15,50,189,159,94,22,43,205,160,95,27,38,181,138,67,24,47,161,142,78,19,45,161,141,71,14,56,147,98,50,11,37,163,125,62,19,44,172,96,53,16,27,159,103,57,13,33,143,101,52,24,25,136,99,58,16,25,126,95,54,10,31,121,87,51,15,21,123,89,41,19,29,128,91,48,19,24,120,76,43,10,23
A00-R99, U00-U85 All diseases (excl.R999),237,230,136,33,61,207,208,117,33,58,227,202,97,39,66,208,179,98,24,57,204,158,91,25,42,176,175,95,22,58,181,185,111,26,48,180,176,103,21,52,184,160,88,25,47,196,150,91,14,45,189,157,94,22,41,205,155,91,27,37,181,133,65,24,44,161,136,77,19,40,161,133,68,14,51,147,96,50,11,35,163,121,62,19,40,172,95,53,16,26,156,103,57,13,33,140,98,51,24,23,130,97,58,16,23,111,92,52,10,30,108,84,50,15,19,108,88,41,19,28,123,89,46,19,24,102,75,42,10,23
```

---

#### statfin_ksyyt_pxt_11be.px

**Title**: Deaths by Underlying cause of death (ICD-10, 3-character level), Age, Year, Sex and Information

**File**: `statfin_ksyyt_pxt_11be.csv` (4.17 MB)

**Description**: 
Statistical table 11be from Statistics Finland.

**Variables**:
- **Underlying cause of death (ICD-10, 3-character level)** (`Tilaston peruskuolemansyy (ICD-10, 3-merkkitaso)`): 1731 categories
- **Age** (`Ikä`): 22 categories
- **Year** (`Vuosi`): 26 categories
  - Time dimension: 1998 to 2023
- **Sex** (`Sukupuoli`): 3 categories
  - Values: Total, Males, Females
- **Information** (`Tiedot`): 1 categories
  - Values: Deaths

**Data Structure**:
- Columns: 1
- Sample row count: 1,002+
- Headers: Underlying cause of death (ICD-10, 3-character level),"Age","1998 Total Deaths","1999 Total Deaths","2000 Total Deaths","2001 Total Deaths","2002 Total Deaths","2003 Total Deaths","2004 Total Deaths","2005 Total Deaths","2006 Total Deaths","2007 Total Deaths","2008 Total Deaths","2009 Total Deaths","2010 Total Deaths","2011 Total Deaths","2012 Total Deaths","2013 Total Deaths","2014 Total Deaths","2015 Total Deaths","2016 Total Deaths","2017 Total Deaths","2018 Total Deaths","2019 Total Deaths","2020 Total Deaths","2021 Total Deaths","2022 Total Deaths","2023 Total Deaths"

**Sample Data**:
```
Underlying cause of death (ICD-10, 3-character level),"Age","1998 Total Deaths","1999 Total Deaths","2000 Total Deaths","2001 Total Deaths","2002 Total Deaths","2003 Total Deaths","2004 Total Deaths","2005 Total Deaths","2006 Total Deaths","2007 Total Deaths","2008 Total Deaths","2009 Total Deaths","2010 Total Deaths","2011 Total Deaths","2012 Total Deaths","2013 Total Deaths","2014 Total Deaths","2015 Total Deaths","2016 Total Deaths","2017 Total Deaths","2018 Total Deaths","2019 Total Deaths","2020 Total Deaths","2021 Total Deaths","2022 Total Deaths","2023 Total Deaths"
A00-Y89 Total,"Total",49237,49368,49316,48504,49389,49033,47757,47751,48105,49093,49090,49904,50910,50568,51737,51478,52409,52302,53964,53670,54523,53962,55498,57632,63172,61301
A00-Y89 Total,"0",236,213,205,181,165,182,193,179,168,159,159,160,138,142,141,98,125,96,103,101,99,95,87,89,91,76
```

---

#### statfin_ksyyt_pxt_11bf.px

**Title**: Deaths by Month, Underlying cause of death (time series classification), Sex and Information

**File**: `statfin_ksyyt_pxt_11bf.csv` (1.02 MB)

**Description**: 
Statistical table 11bf from Statistics Finland.

**Variables**:
- **Month** (`Kuukausi`): 660 categories
  - Time dimension: 1969M01 to 2023M12
- **Underlying cause of death (time series classification)** (`Tilaston peruskuolemansyy (aikasarjaluokitus)`): 21 categories
- **Sex** (`Sukupuoli`): 3 categories
  - Values: Total, Males, Females
- **Information** (`Tiedot`): 1 categories
  - Values: Deaths

**Data Structure**:
- Columns: 1
- Sample row count: 1,002+
- Headers: Month,"Underlying cause of death (time series classification)","Total Deaths"

**Sample Data**:
```
Month,"Underlying cause of death (time series classification)","Total Deaths"
1969M01,"00-54 Total",4099
1969M01,"00-41 Diseases and accidental poisoning by alcohol (A00-R99, U071, U072, U109, X45)",3826
```

---

#### statfin_ksyyt_pxt_11bx.px

**Title**: Alcohol-related deaths by Alcohol-related deaths, Age, Year, Sex and Information

**File**: `statfin_ksyyt_pxt_11bx.csv` (0.03 MB)

**Description**: 
Statistical table 11bx from Statistics Finland.

**Variables**:
- **Alcohol-related deaths** (`Alkoholisyyt`): 14 categories
- **Age** (`Ikä`): 19 categories
- **Year** (`Vuosi`): 19 categories
  - Time dimension: 2005 to 2023
- **Sex** (`Sukupuoli`): 3 categories
  - Values: Total, Males, Females
- **Information** (`Tiedot`): 1 categories
  - Values: Alcohol-related deaths

**Data Structure**:
- Columns: 1
- Sample row count: 266+
- Headers: Alcohol-related deaths,"Age","2005 Total Alcohol-related deaths","2006 Total Alcohol-related deaths","2007 Total Alcohol-related deaths","2008 Total Alcohol-related deaths","2009 Total Alcohol-related deaths","2010 Total Alcohol-related deaths","2011 Total Alcohol-related deaths","2012 Total Alcohol-related deaths","2013 Total Alcohol-related deaths","2014 Total Alcohol-related deaths","2015 Total Alcohol-related deaths","2016 Total Alcohol-related deaths","2017 Total Alcohol-related deaths","2018 Total Alcohol-related deaths","2019 Total Alcohol-related deaths","2020 Total Alcohol-related deaths","2021 Total Alcohol-related deaths","2022 Total Alcohol-related deaths","2023 Total Alcohol-related deaths"

**Sample Data**:
```
Alcohol-related deaths,"Age","2005 Total Alcohol-related deaths","2006 Total Alcohol-related deaths","2007 Total Alcohol-related deaths","2008 Total Alcohol-related deaths","2009 Total Alcohol-related deaths","2010 Total Alcohol-related deaths","2011 Total Alcohol-related deaths","2012 Total Alcohol-related deaths","2013 Total Alcohol-related deaths","2014 Total Alcohol-related deaths","2015 Total Alcohol-related deaths","2016 Total Alcohol-related deaths","2017 Total Alcohol-related deaths","2018 Total Alcohol-related deaths","2019 Total Alcohol-related deaths","2020 Total Alcohol-related deaths","2021 Total Alcohol-related deaths","2022 Total Alcohol-related deaths","2023 Total Alcohol-related deaths"
Total,"Total",2008,2020,2167,2136,2065,1962,1889,1960,1926,1841,1666,1730,1558,1683,1718,1716,1646,1664,1727
Total,"0 - 14",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
```

---

#### statfin_ksyyt_pxt_11by.px

**Title**: Suicides by Age, Year, Sex and Information

**File**: `statfin_ksyyt_pxt_11by.csv` (0.01 MB)

**Description**: 
Statistical table 11by from Statistics Finland.

**Variables**:
- **Age** (`Ikä`): 21 categories
- **Year** (`Vuosi`): 103 categories
  - Time dimension: 1921 to 2023
- **Sex** (`Sukupuoli`): 3 categories
  - Values: Total, Males, Females
- **Information** (`Tiedot`): 1 categories
  - Values: Suicides

**Data Structure**:
- Columns: 1
- Sample row count: 21+
- Headers: Age,"1921 Total Suicides","1922 Total Suicides","1923 Total Suicides","1924 Total Suicides","1925 Total Suicides","1926 Total Suicides","1927 Total Suicides","1928 Total Suicides","1929 Total Suicides","1930 Total Suicides","1931 Total Suicides","1932 Total Suicides","1933 Total Suicides","1934 Total Suicides","1935 Total Suicides","1936 Total Suicides","1937 Total Suicides","1938 Total Suicides","1939 Total Suicides","1940 Total Suicides","1941 Total Suicides","1942 Total Suicides","1943 Total Suicides","1944 Total Suicides","1945 Total Suicides","1946 Total Suicides","1947 Total Suicides","1948 Total Suicides","1949 Total Suicides","1950 Total Suicides","1951 Total Suicides","1952 Total Suicides","1953 Total Suicides","1954 Total Suicides","1955 Total Suicides","1956 Total Suicides","1957 Total Suicides","1958 Total Suicides","1959 Total Suicides","1960 Total Suicides","1961 Total Suicides","1962 Total Suicides","1963 Total Suicides","1964 Total Suicides","1965 Total Suicides","1966 Total Suicides","1967 Total Suicides","1968 Total Suicides","1969 Total Suicides","1970 Total Suicides","1971 Total Suicides","1972 Total Suicides","1973 Total Suicides","1974 Total Suicides","1975 Total Suicides","1976 Total Suicides","1977 Total Suicides","1978 Total Suicides","1979 Total Suicides","1980 Total Suicides","1981 Total Suicides","1982 Total Suicides","1983 Total Suicides","1984 Total Suicides","1985 Total Suicides","1986 Total Suicides","1987 Total Suicides","1988 Total Suicides","1989 Total Suicides","1990 Total Suicides","1991 Total Suicides","1992 Total Suicides","1993 Total Suicides","1994 Total Suicides","1995 Total Suicides","1996 Total Suicides","1997 Total Suicides","1998 Total Suicides","1999 Total Suicides","2000 Total Suicides","2001 Total Suicides","2002 Total Suicides","2003 Total Suicides","2004 Total Suicides","2005 Total Suicides","2006 Total Suicides","2007 Total Suicides","2008 Total Suicides","2009 Total Suicides","2010 Total Suicides","2011 Total Suicides","2012 Total Suicides","2013 Total Suicides","2014 Total Suicides","2015 Total Suicides","2016 Total Suicides","2017 Total Suicides","2018 Total Suicides","2019 Total Suicides","2020 Total Suicides","2021 Total Suicides","2022 Total Suicides","2023 Total Suicides"

**Sample Data**:
```
Age,"1921 Total Suicides","1922 Total Suicides","1923 Total Suicides","1924 Total Suicides","1925 Total Suicides","1926 Total Suicides","1927 Total Suicides","1928 Total Suicides","1929 Total Suicides","1930 Total Suicides","1931 Total Suicides","1932 Total Suicides","1933 Total Suicides","1934 Total Suicides","1935 Total Suicides","1936 Total Suicides","1937 Total Suicides","1938 Total Suicides","1939 Total Suicides","1940 Total Suicides","1941 Total Suicides","1942 Total Suicides","1943 Total Suicides","1944 Total Suicides","1945 Total Suicides","1946 Total Suicides","1947 Total Suicides","1948 Total Suicides","1949 Total Suicides","1950 Total Suicides","1951 Total Suicides","1952 Total Suicides","1953 Total Suicides","1954 Total Suicides","1955 Total Suicides","1956 Total Suicides","1957 Total Suicides","1958 Total Suicides","1959 Total Suicides","1960 Total Suicides","1961 Total Suicides","1962 Total Suicides","1963 Total Suicides","1964 Total Suicides","1965 Total Suicides","1966 Total Suicides","1967 Total Suicides","1968 Total Suicides","1969 Total Suicides","1970 Total Suicides","1971 Total Suicides","1972 Total Suicides","1973 Total Suicides","1974 Total Suicides","1975 Total Suicides","1976 Total Suicides","1977 Total Suicides","1978 Total Suicides","1979 Total Suicides","1980 Total Suicides","1981 Total Suicides","1982 Total Suicides","1983 Total Suicides","1984 Total Suicides","1985 Total Suicides","1986 Total Suicides","1987 Total Suicides","1988 Total Suicides","1989 Total Suicides","1990 Total Suicides","1991 Total Suicides","1992 Total Suicides","1993 Total Suicides","1994 Total Suicides","1995 Total Suicides","1996 Total Suicides","1997 Total Suicides","1998 Total Suicides","1999 Total Suicides","2000 Total Suicides","2001 Total Suicides","2002 Total Suicides","2003 Total Suicides","2004 Total Suicides","2005 Total Suicides","2006 Total Suicides","2007 Total Suicides","2008 Total Suicides","2009 Total Suicides","2010 Total Suicides","2011 Total Suicides","2012 Total Suicides","2013 Total Suicides","2014 Total Suicides","2015 Total Suicides","2016 Total Suicides","2017 Total Suicides","2018 Total Suicides","2019 Total Suicides","2020 Total Suicides","2021 Total Suicides","2022 Total Suicides","2023 Total Suicides"
Total,382,359,394,482,531,525,614,600,674,795,813,776,732,686,615,705,709,723,835,774,675,537,665,598,637,650,621,636,683,624,636,722,722,793,846,961,949,933,881,908,922,994,873,908,911,892,933,1015,1096,983,1003,1113,1098,1176,1178,1220,1220,1200,1178,1226,1143,1164,1183,1231,1210,1310,1366,1405,1413,1512,1493,1451,1397,1387,1388,1247,1322,1228,1207,1165,1204,1095,1075,1064,994,1062,995,1033,1034,954,912,873,887,789,731,787,824,810,746,717,747,740,752
0 - 24,88,74,87,122,119,144,158,177,177,210,189,197,169,142,117,137,121,112,121,125,110,100,103,117,99,115,97,112,99,95,79,100,84,85,80,78,98,76,97,81,97,109,76,107,80,89,107,134,134,136,151,172,185,199,219,213,171,166,186,184,146,139,163,163,166,163,165,165,194,208,165,145,121,174,148,137,153,128,143,133,120,123,129,146,103,131,123,111,118,136,118,117,101,87,76,104,107,99,109,85,79,88,116
```

---

#### statfin_ksyyt_pxt_11c1.px

**Title**: Autopsies and other means to determine cause of death by Grounds for investigating the cause of death, Age, Year, Sex and Information

**File**: `statfin_ksyyt_pxt_11c1.csv` (0.01 MB)

**Description**: 
Statistical table 11c1 from Statistics Finland.

**Variables**:
- **Grounds for investigating the cause of death** (`Kuolemansyyn selvittämistapa`): 7 categories
  - Values: Total, Forensic autopsy, Medical autopsy, Other examination, Foreign death certificate...
- **Age** (`Ikä`): 4 categories
  - Values: Total, 0 - 64, 65 - 74, 75 -
- **Year** (`Vuosi`): 49 categories
  - Time dimension: 1975 to 2023
- **Sex** (`Sukupuoli`): 3 categories
  - Values: Total, Males, Females
- **Information** (`Tiedot`): 1 categories
  - Values: Deaths

**Data Structure**:
- Columns: 1
- Sample row count: 28+
- Headers: Grounds for investigating the cause of death,"Age","1975 Total Deaths","1976 Total Deaths","1977 Total Deaths","1978 Total Deaths","1979 Total Deaths","1980 Total Deaths","1981 Total Deaths","1982 Total Deaths","1983 Total Deaths","1984 Total Deaths","1985 Total Deaths","1986 Total Deaths","1987 Total Deaths","1988 Total Deaths","1989 Total Deaths","1990 Total Deaths","1991 Total Deaths","1992 Total Deaths","1993 Total Deaths","1994 Total Deaths","1995 Total Deaths","1996 Total Deaths","1997 Total Deaths","1998 Total Deaths","1999 Total Deaths","2000 Total Deaths","2001 Total Deaths","2002 Total Deaths","2003 Total Deaths","2004 Total Deaths","2005 Total Deaths","2006 Total Deaths","2007 Total Deaths","2008 Total Deaths","2009 Total Deaths","2010 Total Deaths","2011 Total Deaths","2012 Total Deaths","2013 Total Deaths","2014 Total Deaths","2015 Total Deaths","2016 Total Deaths","2017 Total Deaths","2018 Total Deaths","2019 Total Deaths","2020 Total Deaths","2021 Total Deaths","2022 Total Deaths","2023 Total Deaths"

**Sample Data**:
```
Grounds for investigating the cause of death,"Age","1975 Total Deaths","1976 Total Deaths","1977 Total Deaths","1978 Total Deaths","1979 Total Deaths","1980 Total Deaths","1981 Total Deaths","1982 Total Deaths","1983 Total Deaths","1984 Total Deaths","1985 Total Deaths","1986 Total Deaths","1987 Total Deaths","1988 Total Deaths","1989 Total Deaths","1990 Total Deaths","1991 Total Deaths","1992 Total Deaths","1993 Total Deaths","1994 Total Deaths","1995 Total Deaths","1996 Total Deaths","1997 Total Deaths","1998 Total Deaths","1999 Total Deaths","2000 Total Deaths","2001 Total Deaths","2002 Total Deaths","2003 Total Deaths","2004 Total Deaths","2005 Total Deaths","2006 Total Deaths","2007 Total Deaths","2008 Total Deaths","2009 Total Deaths","2010 Total Deaths","2011 Total Deaths","2012 Total Deaths","2013 Total Deaths","2014 Total Deaths","2015 Total Deaths","2016 Total Deaths","2017 Total Deaths","2018 Total Deaths","2019 Total Deaths","2020 Total Deaths","2021 Total Deaths","2022 Total Deaths","2023 Total Deaths"
Total,"Total",43866,44857,44264,43817,43857,44511,44528,43584,45517,45176,48347,47306,47988,49092,49132,50091,49319,49856,51033,47946,49326,49161,49142,49237,49368,49316,48504,49389,49033,47757,47751,48105,49093,49090,49904,50910,50568,51737,51478,52409,52302,53964,53670,54523,53962,55498,57632,63172,61301
Total,"0 - 64",15144,14917,14569,13714,13408,12903,12894,12500,12519,12479,12807,12782,12660,12852,12820,12720,12416,12097,11635,11164,11215,10909,10985,10962,11005,10973,10620,10545,10702,11176,11287,10899,11120,11129,10894,10738,10228,9793,9354,8873,8352,8367,8118,7994,7533,7749,7590,7656,7476
```

---

#### statfin_ksyyt_pxt_12d9.px

**Title**: Drug-related deaths by Drug (Selection B), Age, Year, Sex and Information

**File**: `statfin_ksyyt_pxt_12d9.csv` (0.01 MB)

**Description**: 
Statistical table 12d9 from Statistics Finland.

**Variables**:
- **Drug (Selection B)** (`Huume (B-luokitus)`): 5 categories
  - Values: Total, Disorders due to drugs (F11-F12,F14-F16,F19), Accidental drug poisoning (X41,X42,X44/T400-9,T436), Intentional drug poisoning (X61,X62,X64/T400-9,T436), Drug poisoning undetermined intent (Y11,Y12,Y14/T400-9,T436)
- **Age** (`Ikä`): 18 categories
- **Year** (`Vuosi`): 18 categories
  - Time dimension: 2006 to 2023
- **Sex** (`Sukupuoli`): 3 categories
  - Values: Total, Males, Females
- **Information** (`Tiedot`): 1 categories
  - Values: Drug-related deaths (Selection B)

**Data Structure**:
- Columns: 1
- Sample row count: 90+
- Headers: Drug (Selection B),"Age","2006 Total Drug-related deaths (Selection B)","2007 Total Drug-related deaths (Selection B)","2008 Total Drug-related deaths (Selection B)","2009 Total Drug-related deaths (Selection B)","2010 Total Drug-related deaths (Selection B)","2011 Total Drug-related deaths (Selection B)","2012 Total Drug-related deaths (Selection B)","2013 Total Drug-related deaths (Selection B)","2014 Total Drug-related deaths (Selection B)","2015 Total Drug-related deaths (Selection B)","2016 Total Drug-related deaths (Selection B)","2017 Total Drug-related deaths (Selection B)","2018 Total Drug-related deaths (Selection B)","2019 Total Drug-related deaths (Selection B)","2020 Total Drug-related deaths (Selection B)","2021 Total Drug-related deaths (Selection B)","2022 Total Drug-related deaths (Selection B)","2023 Total Drug-related deaths (Selection B)"

**Sample Data**:
```
Drug (Selection B),"Age","2006 Total Drug-related deaths (Selection B)","2007 Total Drug-related deaths (Selection B)","2008 Total Drug-related deaths (Selection B)","2009 Total Drug-related deaths (Selection B)","2010 Total Drug-related deaths (Selection B)","2011 Total Drug-related deaths (Selection B)","2012 Total Drug-related deaths (Selection B)","2013 Total Drug-related deaths (Selection B)","2014 Total Drug-related deaths (Selection B)","2015 Total Drug-related deaths (Selection B)","2016 Total Drug-related deaths (Selection B)","2017 Total Drug-related deaths (Selection B)","2018 Total Drug-related deaths (Selection B)","2019 Total Drug-related deaths (Selection B)","2020 Total Drug-related deaths (Selection B)","2021 Total Drug-related deaths (Selection B)","2022 Total Drug-related deaths (Selection B)","2023 Total Drug-related deaths (Selection B)"
Total,"Total",138,144,169,175,156,197,213,201,176,167,194,200,261,234,258,287,250,310
Total,"0 - 14",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
```

---

#### statfin_ksyyt_pxt_13u5.px

**Title**: Deaths by Wellbeing services county, Underlying cause of death (time series classification), Year and Information

**File**: `statfin_ksyyt_pxt_13u5.csv` (0.41 MB)

**Description**: 
Statistical table 13u5 from Statistics Finland.

**Variables**:
- **Wellbeing services county** (`Hyvinvointialue`): 26 categories
- **Underlying cause of death (time series classification)** (`Tilaston peruskuolemansyy (aikasarjaluokitus)`): 65 categories
- **Year** (`Vuosi`): 55 categories
  - Time dimension: 1969 to 2023
- **Information** (`Tiedot`): 1 categories
  - Values: Deaths

**Data Structure**:
- Columns: 1
- Sample row count: 1,002+
- Headers: Wellbeing services county,"Underlying cause of death (time series classification)","1969 Deaths","1970 Deaths","1971 Deaths","1972 Deaths","1973 Deaths","1974 Deaths","1975 Deaths","1976 Deaths","1977 Deaths","1978 Deaths","1979 Deaths","1980 Deaths","1981 Deaths","1982 Deaths","1983 Deaths","1984 Deaths","1985 Deaths","1986 Deaths","1987 Deaths","1988 Deaths","1989 Deaths","1990 Deaths","1991 Deaths","1992 Deaths","1993 Deaths","1994 Deaths","1995 Deaths","1996 Deaths","1997 Deaths","1998 Deaths","1999 Deaths","2000 Deaths","2001 Deaths","2002 Deaths","2003 Deaths","2004 Deaths","2005 Deaths","2006 Deaths","2007 Deaths","2008 Deaths","2009 Deaths","2010 Deaths","2011 Deaths","2012 Deaths","2013 Deaths","2014 Deaths","2015 Deaths","2016 Deaths","2017 Deaths","2018 Deaths","2019 Deaths","2020 Deaths","2021 Deaths","2022 Deaths","2023 Deaths"

**Sample Data**:
```
Wellbeing services county,"Underlying cause of death (time series classification)","1969 Deaths","1970 Deaths","1971 Deaths","1972 Deaths","1973 Deaths","1974 Deaths","1975 Deaths","1976 Deaths","1977 Deaths","1978 Deaths","1979 Deaths","1980 Deaths","1981 Deaths","1982 Deaths","1983 Deaths","1984 Deaths","1985 Deaths","1986 Deaths","1987 Deaths","1988 Deaths","1989 Deaths","1990 Deaths","1991 Deaths","1992 Deaths","1993 Deaths","1994 Deaths","1995 Deaths","1996 Deaths","1997 Deaths","1998 Deaths","1999 Deaths","2000 Deaths","2001 Deaths","2002 Deaths","2003 Deaths","2004 Deaths","2005 Deaths","2006 Deaths","2007 Deaths","2008 Deaths","2009 Deaths","2010 Deaths","2011 Deaths","2012 Deaths","2013 Deaths","2014 Deaths","2015 Deaths","2016 Deaths","2017 Deaths","2018 Deaths","2019 Deaths","2020 Deaths","2021 Deaths","2022 Deaths","2023 Deaths"
WHOLE COUNTRY,"00-54 Total",45966,44119,45876,43958,43411,44673,43866,44857,44264,43817,43857,44511,44528,43584,45517,45176,48347,47306,47988,49092,49132,50091,49319,49856,51033,47946,49326,49161,49142,49237,49368,49316,48504,49389,49033,47757,47751,48105,49093,49090,49904,50910,50568,51737,51478,52409,52302,53964,53670,54523,53962,55498,57632,63172,61301
WHOLE COUNTRY,"00-41 Diseases and accidental poisoning by alcohol (A00-R99, U071, U072, U109, X45)",42102,40394,41902,39828,39457,40841,40015,41130,40657,40328,40315,41063,41184,40254,42099,41749,44805,43622,44125,44942,44788,45740,44999,45641,47053,43936,45370,45379,45136,45300,45527,45538,44664,45556,45187,43750,43881,44208,45280,45218,46070,47209,46962,48203,47925,48730,48912,50695,50260,51061,50715,52286,54089,59586,57729
```

---

## Summary Statistics

**Total Data Size**: 0.81 GB

**File Sizes**:
- statfin_kuol_pxt_12as.csv: 819.09 MB
- statfin_ksyyt_pxt_11be.csv: 4.17 MB
- statfin_ksyyt_pxt_11b2.csv: 1.2 MB
- statfin_ksyyt_pxt_11bf.csv: 1.02 MB
- statfin_kuol_pxt_12au.csv: 0.92 MB
- statfin_kuol_pxt_12ak.csv: 0.73 MB
- statfin_ksyyt_pxt_13u5.csv: 0.41 MB
- statfin_ksyyt_pxt_11ay.csv: 0.35 MB
- statfin_ksyyt_pxt_11az.csv: 0.34 MB
- statfin_kuol_pxt_12ap.csv: 0.15 MB
- statfin_ksyyt_pxt_11bd.csv: 0.09 MB
- statfin_kuol_pxt_12an.csv: 0.03 MB
- statfin_ksyyt_pxt_11bx.csv: 0.03 MB
- statfin_kuol_pxt_12ag.csv: 0.02 MB
- statfin_kuol_pxt_12at.csv: 0.02 MB
- statfin_ksyyt_pxt_12d9.csv: 0.01 MB
- statfin_ksyyt_pxt_11by.csv: 0.01 MB
- statfin_ksyyt_pxt_11c1.csv: 0.01 MB
- statfin_kuol_pxt_12al.csv: 0.01 MB
- statfin_kuol_pxt_12ah.csv: 0.01 MB
- statfin_kuol_pxt_12aq.csv: 0.0 MB
- statfin_kuol_pxt_12af.csv: 0.0 MB
- statfin_kuol_pxt_12am.csv: 0.0 MB

**Data Coverage**:
- statfin_kuol_pxt_12af.px: 1751 - 2024
- statfin_kuol_pxt_12ag.px: 1980 - 2024
- statfin_kuol_pxt_12ah.px: 1945 - 2024
- statfin_kuol_pxt_12ak.px: 1990 - 2024
- statfin_kuol_pxt_12al.px: 1751 - 2024
- statfin_kuol_pxt_12am.px: 1751 - 2024
- statfin_kuol_pxt_12an.px: 1992 - 2023
- statfin_kuol_pxt_12ap.px: 1986 - 2023
- statfin_kuol_pxt_12aq.px: 1751 - 2024
- statfin_kuol_pxt_12as.px: 1990M01 - 2024M12
- statfin_kuol_pxt_12au.px: 1990 - 2024
- statfin_ksyyt_pxt_11ay.px: 1971 - 2023
- statfin_ksyyt_pxt_11az.px: 1969 - 2023
- statfin_ksyyt_pxt_11b2.px: 1998 - 2023
- statfin_ksyyt_pxt_11bd.px: 1998 - 2023
- statfin_ksyyt_pxt_11be.px: 1998 - 2023
- statfin_ksyyt_pxt_11bf.px: 1969M01 - 2023M12
- statfin_ksyyt_pxt_11bx.px: 2005 - 2023
- statfin_ksyyt_pxt_11by.px: 1921 - 2023
- statfin_ksyyt_pxt_11c1.px: 1975 - 2023
- statfin_ksyyt_pxt_12d9.px: 2006 - 2023
- statfin_ksyyt_pxt_13u5.px: 1969 - 2023

## Usage Notes

1. **Data Format**: All files are CSV with semicolon (;) delimiters
2. **Encoding**: UTF-8
3. **Missing Values**: May be represented as ".." or empty cells
4. **Time Variables**: Usually in YYYY or YYYYMM format
5. **Geographic Codes**: Area codes follow Statistics Finland standards

## Data Sources

- **API**: Statistics Finland PxWeb API (https://pxdata.stat.fi/PXWeb/api/v1/en/)
- **Categories**: 
  - Deaths: /StatFin/kuol/
  - Causes of Death: /StatFin/ksyyt/

For more information, visit: https://www.stat.fi/
