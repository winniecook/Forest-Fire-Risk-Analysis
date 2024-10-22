import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import sys

def load_data(file_path):
    """Load data from CSV file"""
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """Clean the data by removing duplicates and handling missing values"""
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    df = df.dropna()
    
    return df

def feature_engineering(df):
    """Create new features from existing ones"""
    # Create temp-humidity ratio if both columns exist
    if 'temp' in df.columns and 'humid' in df.columns:
        df['temp_humid_ratio'] = df['temp'] / df['humid']
    
    # Create wind-rain interaction if both columns exist
    if 'wind' in df.columns and 'rain' in df.columns:
        df['wind_rain_interaction'] = df['wind'] * df['rain']
    
    return df

def normalize_features(df):
    """Normalize numerical features using StandardScaler"""
    scaler = StandardScaler()
    
    # Get list of numeric columns from the dataframe
    numeric_features = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    # Remove target variable if it exists
    if 'fire' in numeric_features:
        numeric_features.remove('fire')
    
    # Only normalize if we have numeric features
    if numeric_features:
        df[numeric_features] = scaler.fit_transform(df[numeric_features])
    
    return df

def main(input_file, output_file):
    """Main function to run the preprocessing pipeline"""
    # Load data
    print(f"Loading data from {input_file}")
    df = load_data(input_file)
    
    if df is None:
        print("Failed to load data. Exiting.")
        sys.exit(1)
    
    # Print initial data info
    print("\nInitial data shape:", df.shape)
    print("\nColumns in dataset:", df.columns.tolist())
    
    # Clean data
    print("\nCleaning data...")
    df = clean_data(df)
    
    # Feature engineering
    print("Performing feature engineering...")
    df = feature_engineering(df)
    
    # Normalize features
    print("Normalizing features...")
    df = normalize_features(df)
    
    # Save preprocessed data
    print(f"\nSaving preprocessed data to {output_file}")
    df.to_csv(output_file, index=False)
    print("Preprocessing completed successfully!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python 01_data_preprocessing.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)