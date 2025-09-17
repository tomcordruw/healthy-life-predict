#!/usr/bin/env python3
"""
Life Tables CSV Parser
A specific parser for the life_tables_detailed.csv file based on the successful notebook parsing logic.
"""

import pandas as pd
import numpy as np
import os

def parse_life_tables_csv(input_file="statfin/mortality_rates/life_tables_detailed.csv", 
                         output_file="processed-data/mortality_rates/life_tables_detailed_clean.csv"):
    """
    Parse the life_tables_detailed.csv file using the exact logic from the notebook
    """
    
    def clean_csv_line(line):
        """Clean a line from the CSV file"""
        line = line.strip()
        if line.startswith('"') and line.endswith('"'):
            line = line[1:-1]  # Remove outer quotes
        
        # Replace double quotes with single quotes for inner quotes
        line = line.replace('""', '"')
        return line

    # Read and clean the file
    cleaned_data = []
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Process header - we know the structure from the notebook
    columns = ['Year', 'Sex', 'Age', 'Probability_of_death_per_mille', 'Survivors_per_100k', 'Life_expectancy_years']

    # Process data lines (skip header)
    for line in lines[1:]:
        cleaned_line = clean_csv_line(line)
        if cleaned_line:
            try:
                parts = cleaned_line.split(',')
                if len(parts) >= 6:
                    year = int(parts[0])
                    sex = parts[1].strip('"')
                    age = parts[2].strip('"')
                    
                    # Handle potential missing values
                    try:
                        prob_death = float(parts[3]) if parts[3].strip() and parts[3].strip() != '.' else np.nan
                    except:
                        prob_death = np.nan
                        
                    try:
                        survivors = int(parts[4]) if parts[4].strip() and parts[4].strip() != '.' else np.nan
                    except:
                        survivors = np.nan
                        
                    try:
                        life_expectancy = float(parts[5]) if parts[5].strip() and parts[5].strip() != '.' else np.nan
                    except:
                        life_expectancy = np.nan
                    
                    cleaned_data.append([year, sex, age, prob_death, survivors, life_expectancy])
            except Exception as e:
                print(f"Error parsing line: {line.strip()}, Error: {e}")
                continue

    # Create DataFrame
    df = pd.DataFrame(cleaned_data, columns=columns)

    # Convert Age to numeric where possible
    df['Age_numeric'] = pd.to_numeric(df['Age'], errors='coerce')

    # Save to output file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_csv(output_file, index=False)
    
    print(f"Successfully parsed life tables data:")
    print(f"- Shape: {df.shape}")
    print(f"- Columns: {df.columns.tolist()}")
    print(f"- Output file: {output_file}")
    print(f"- Sample data:")
    print(df.head())
    
    return df

if __name__ == "__main__":
    df = parse_life_tables_csv()