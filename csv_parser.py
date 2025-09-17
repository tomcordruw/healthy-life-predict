#!/usr/bin/env python3
"""
CSV Parser for Finnish Statistical Data (Statfin)
This script parses the CSV files with unusual quoting format and converts them to standard CSV format.
"""

import pandas as pd
import numpy as np
import os
import re
from pathlib import Path

def clean_csv_line(line):
    """Clean a line from the CSV file by handling unusual quoting"""
    line = line.strip()
    if line.startswith('"') and line.endswith('"'):
        line = line[1:-1]  # Remove outer quotes
    
    # Replace double quotes with single quotes for inner quotes
    line = line.replace('""', '"')
    return line

def parse_statfin_csv(input_file, output_file=None):
    """
    Parse a Statfin CSV file with unusual quoting and save as standard CSV
    
    Args:
        input_file (str): Path to input CSV file
        output_file (str): Path to output CSV file (optional)
    
    Returns:
        pd.DataFrame: Parsed dataframe
    """
    print(f"Processing: {input_file}")
    
    try:
        # Read the file
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if not lines:
            print(f"Warning: Empty file {input_file}")
            return pd.DataFrame()
        
        # Process header
        header = clean_csv_line(lines[0])
        
        # Handle multi-line headers (some files might have headers that span multiple lines)
        if len(lines) > 1 and not any(char.isdigit() for char in lines[1][:50]):
            # This might be a continuation of the header
            for i in range(1, min(5, len(lines))):  # Check up to 5 lines for header continuation
                next_line = clean_csv_line(lines[i])
                if any(char.isdigit() for char in next_line[:50]):  # Found data line
                    break
                header += " " + next_line
        
        # Split header into column names
        header_parts = []
        if '","' in header:
            # Standard comma-separated quoted fields
            parts = header.split('","')
            for part in parts:
                clean_part = part.strip('"').strip()
                if clean_part:
                    header_parts.append(clean_part)
        else:
            # Fallback: split by comma and clean
            parts = header.split(',')
            for part in parts:
                clean_part = part.strip('"').strip()
                if clean_part:
                    header_parts.append(clean_part)
        
        # Special handling for life_tables_detailed.csv format
        if len(header_parts) == 1 and 'Year' in header_parts[0]:
            # This is the life tables format with everything in one string
            header_str = header_parts[0]
            if 'Sex' in header_str and 'Age' in header_str:
                header_parts = ['Year', 'Sex', 'Age', 'Probability_of_death_per_mille', 'Survivors_per_100k', 'Life_expectancy_years']
        
        # Process data lines
        cleaned_data = []
        data_start_line = 1
        
        # Find where actual data starts
        for i in range(1, min(10, len(lines))):
            line = lines[i].strip()
            if line and any(char.isdigit() for char in line[:50]):
                data_start_line = i
                break
        
        for line in lines[data_start_line:]:
            cleaned_line = clean_csv_line(line)
            if cleaned_line:
                try:
                    # Split by comma, handling quoted fields
                    if '","' in cleaned_line:
                        parts = cleaned_line.split('","')
                    else:
                        parts = cleaned_line.split(',')
                    
                    # Clean each part
                    clean_parts = []
                    for part in parts:
                        clean_part = part.strip('"').strip()
                        
                        # Try to convert to appropriate data type
                        if clean_part == '' or clean_part == '.' or clean_part.lower() == 'nan':
                            clean_parts.append(np.nan)
                        else:
                            # Try integer first, then float, then keep as string
                            try:
                                if '.' not in clean_part and clean_part.isdigit():
                                    clean_parts.append(int(clean_part))
                                elif re.match(r'^-?\d+\.?\d*$', clean_part):
                                    clean_parts.append(float(clean_part))
                                else:
                                    clean_parts.append(clean_part)
                            except ValueError:
                                clean_parts.append(clean_part)
                    
                    # Only add if we have the right number of columns
                    if len(clean_parts) == len(header_parts):
                        cleaned_data.append(clean_parts)
                    elif len(clean_parts) > 0:  # Allow partial rows for some files
                        # Pad with NaN if fewer columns, truncate if more
                        while len(clean_parts) < len(header_parts):
                            clean_parts.append(np.nan)
                        cleaned_data.append(clean_parts[:len(header_parts)])
                        
                except Exception as e:
                    print(f"Warning: Error parsing line in {input_file}: {line.strip()[:100]}...")
                    continue
        
        # Create DataFrame
        if cleaned_data and header_parts:
            df = pd.DataFrame(cleaned_data, columns=header_parts)
            
            # Save to output file if specified
            if output_file:
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                df.to_csv(output_file, index=False, encoding='utf-8')
                print(f"Saved cleaned data to: {output_file}")
            
            print(f"Successfully parsed {len(df)} rows and {len(df.columns)} columns")
            return df
        else:
            print(f"Warning: No data found in {input_file}")
            return pd.DataFrame()
            
    except Exception as e:
        print(f"Error processing {input_file}: {e}")
        return pd.DataFrame()

def process_all_statfin_files():
    """Process all CSV files in the statfin directory"""
    
    input_dir = Path("statfin")
    output_dir = Path("processed-data")
    
    # Create output directory
    output_dir.mkdir(exist_ok=True)
    
    # Find all CSV files
    csv_files = list(input_dir.rglob("*.csv"))
    
    print(f"Found {len(csv_files)} CSV files to process")
    print("=" * 60)
    
    processed_files = []
    
    for csv_file in csv_files:
        # Create corresponding output path
        relative_path = csv_file.relative_to(input_dir)
        output_file = output_dir / relative_path
        
        # Process the file
        df = parse_statfin_csv(str(csv_file), str(output_file))
        
        if not df.empty:
            processed_files.append({
                'input_file': str(csv_file),
                'output_file': str(output_file),
                'rows': len(df),
                'columns': len(df.columns),
                'column_names': list(df.columns)
            })
        
        print("-" * 60)
    
    # Create summary report
    summary_file = output_dir / "processing_summary.txt"
    with open(summary_file, 'w') as f:
        f.write("CSV Processing Summary\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Total files processed: {len(processed_files)}\n\n")
        
        for i, file_info in enumerate(processed_files, 1):
            f.write(f"{i}. {file_info['input_file']}\n")
            f.write(f"   Output: {file_info['output_file']}\n")
            f.write(f"   Dimensions: {file_info['rows']} rows × {file_info['columns']} columns\n")
            f.write(f"   Columns: {', '.join(file_info['column_names'][:5])}")
            if len(file_info['column_names']) > 5:
                f.write(f" ... (+{len(file_info['column_names']) - 5} more)")
            f.write("\n\n")
    
    print(f"\nProcessing complete! Summary saved to: {summary_file}")
    return processed_files

if __name__ == "__main__":
    # Process all files
    processed_files = process_all_statfin_files()
    
    print(f"\nSuccessfully processed {len(processed_files)} files")
    print("Cleaned CSV files are available in the 'processed-data' directory")