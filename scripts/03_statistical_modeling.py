import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import sys

def prepare_data(df):
    """Prepare data for modeling by selecting appropriate features"""
    # Get all numeric columns except 'fire'
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if 'fire' in numeric_columns:
        numeric_columns.remove('fire')
    
    # Remove any other non-feature columns
    feature_columns = [col for col in numeric_columns if col not in ['index', 'id', 'date']]
    
    print(f"Using features: {feature_columns}")
    
    X = df[feature_columns]
    y = df['fire']
    
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_random_forest(X_train, y_train):
    """Train a Random Forest model"""
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    return rf_model

def evaluate_model(model, X_test, y_test):
    """Evaluate the model and generate performance metrics"""
    y_pred = model.predict(X_test)
    
    # Generate classification report
    class_report = classification_report(y_test, y_pred)
    
    # Generate confusion matrix
    conf_matrix = confusion_matrix(y_test, y_pred)
    
    return class_report, conf_matrix, y_pred

def analyze_feature_importance(model, feature_names):
    """Analyze and sort feature importance"""
    importances = pd.DataFrame({
        'feature': feature_names,
        'importance': model.feature_importances_
    })
    return importances.sort_values('importance', ascending=False)

def main(input_file, output_file):
    """Main function to run the statistical modeling pipeline"""
    print(f"Loading data from {input_file}")
    df = pd.read_csv(input_file)
    
    print("\nPreparing data for modeling...")
    X_train, X_test, y_train, y_test = prepare_data(df)
    
    print("\nTraining Random Forest model...")
    rf_model = train_random_forest(X_train, y_train)
    
    print("\nEvaluating model...")
    class_report, conf_matrix, y_pred = evaluate_model(rf_model, X_test, y_test)
    
    print("\nAnalyzing feature importance...")
    feature_importance = analyze_feature_importance(model=rf_model, feature_names=X_train.columns)
    
    # Save results
    with open(output_file, 'w') as f:
        f.write("Forest Fire Prediction Model Results\n")
        f.write("===================================\n\n")
        
        f.write("Model Performance\n")
        f.write("-----------------\n")
        f.write(class_report)
        f.write("\n\n")
        
        f.write("Confusion Matrix\n")
        f.write("----------------\n")
        f.write(str(conf_matrix))
        f.write("\n\n")
        
        f.write("Feature Importance\n")
        f.write("-----------------\n")
        f.write(feature_importance.to_string())
        f.write("\n\n")
        
        # Add model parameters
        f.write("Model Parameters\n")
        f.write("----------------\n")
        f.write(str(rf_model.get_params()))
        
        # Add basic statistics
        f.write("\n\nData Statistics\n")
        f.write("--------------\n")
        f.write(f"Training set size: {X_train.shape[0]}\n")
        f.write(f"Test set size: {X_test.shape[0]}\n")
        f.write(f"Number of features: {X_train.shape[1]}\n")
        f.write(f"Features used: {', '.join(X_train.columns)}\n")
    
    print(f"\nResults saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python 03_statistical_modeling.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)