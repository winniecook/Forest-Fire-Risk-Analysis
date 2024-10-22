import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
import sys

def read_model_results(model_results_file):
    """Read and parse the model results file"""
    with open(model_results_file, 'r') as f:
        content = f.read()
    return content

def parse_feature_importance(model_results):
    """Parse feature importance from model results text"""
    features = []
    importances = []
    
    lines = model_results.split('\n')
    feature_section = False
    
    for line in lines:
        if "Feature Importance" in line:
            feature_section = True
            continue
        if feature_section and line.strip():
            if "Model Parameters" in line:
                break
            try:
                feature, importance = line.strip().split()
                if feature != "feature" and importance != "importance":  # Skip header
                    features.append(feature)
                    importances.append(float(importance))
            except ValueError:
                continue
    
    return features, importances

def create_feature_importance_plot(model_results):
    """Create feature importance visualization from model results"""
    features, importances = parse_feature_importance(model_results)
    
    if features and importances:
        plt.figure(figsize=(10, 6))
        y_pos = np.arange(len(features))
        plt.barh(y_pos, importances)
        plt.yticks(y_pos, features)
        plt.xlabel('Importance Score')
        plt.title('Feature Importance')
        plt.tight_layout()
        return plt.gcf()
    return None

def create_data_distribution_plots(df):
    """Create distribution plots for key features"""
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    if 'fire' in numeric_cols:
        numeric_cols = numeric_cols.drop('fire')
    
    n_cols = 3
    n_rows = (len(numeric_cols) + n_cols - 1) // n_cols
    
    plt.figure(figsize=(15, n_rows * 4))
    for i, col in enumerate(numeric_cols):
        plt.subplot(n_rows, n_cols, i + 1)
        sns.histplot(data=df, x=col, hue='fire', multiple="stack")
        plt.title(f'Distribution of {col}')
    plt.tight_layout()
    return plt.gcf()

def create_correlation_plot(df):
    """Create correlation heatmap"""
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    if 'fire' in numeric_cols:
        numeric_cols = numeric_cols.drop('fire')
    
    corr = df[numeric_cols].corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
    plt.title('Feature Correlation Heatmap')
    plt.tight_layout()
    return plt.gcf()

def main(data_file, model_results_file, output_file):
    """Main function to create and save visualizations"""
    print(f"Loading data from {data_file}")
    df = pd.read_csv(data_file)
    
    print(f"Reading model results from {model_results_file}")
    model_results = read_model_results(model_results_file)
    
    print("Creating visualizations...")
    with PdfPages(output_file) as pdf:
        # Distribution plots
        fig = create_data_distribution_plots(df)
        if fig:
            pdf.savefig(fig)
            plt.close(fig)
        
        # Correlation plot
        fig = create_correlation_plot(df)
        if fig:
            pdf.savefig(fig)
            plt.close(fig)
        
        # Feature importance plot
        fig = create_feature_importance_plot(model_results)
        if fig:
            pdf.savefig(fig)
            plt.close(fig)
    
    print(f"Visualizations saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python 04_visualization.py <data_file> <model_results_file> <output_file>")
        sys.exit(1)
    
    data_file = sys.argv[1]
    model_results_file = sys.argv[2]
    output_file = sys.argv[3]
    main(data_file, model_results_file, output_file)