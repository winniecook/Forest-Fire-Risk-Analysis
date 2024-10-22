import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys

def create_correlation_heatmap(df):
    """Create correlation heatmap for numeric features"""
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    plt.figure(figsize=(12, 10))
    corr_matrix = numeric_df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap of Forest Fire Features')
    plt.tight_layout()
    return plt

def create_pairplot(df):
    """Create pairplot for key numeric features"""
    # Select relevant numeric columns and the target variable
    plot_columns = ['temp', 'RH', 'wind', 'rain', 'fire']
    plot_df = df[plot_columns].copy()
    
    # Ensure 'fire' is treated as categorical
    plot_df['fire'] = plot_df['fire'].astype('category')
    
    sns.pairplot(plot_df, hue='fire', vars=['temp', 'RH', 'wind', 'rain'], height=2)
    plt.suptitle('Pairplot of Key Features', y=1.02)
    return plt

def create_regional_analysis(df):
    """Create plots for regional analysis"""
    plt.figure(figsize=(12, 6))
    
    # Create side-by-side bar plots
    plt.subplot(1, 2, 1)
    sns.countplot(data=df, x='region', hue='fire')
    plt.title('Fire Occurrence by Region')
    
    plt.subplot(1, 2, 2)
    sns.boxplot(data=df, x='region', y='temp')
    plt.title('Temperature Distribution by Region')
    
    plt.tight_layout()
    return plt

def main(input_file, output_file):
    """Main function to run the exploratory analysis"""
    # Load data
    print(f"Loading data from {input_file}")
    df = pd.read_csv(input_file)
    
    # Print data info
    print("\nData shape:", df.shape)
    print("\nColumns in dataset:", df.columns.tolist())
    print("\nNumeric columns:", df.select_dtypes(include=['float64', 'int64']).columns.tolist())
    
    # Create plots
    print("\nCreating correlation heatmap...")
    heatmap = create_correlation_heatmap(df)
    heatmap.savefig('correlation_heatmap.png')
    plt.close()
    
    print("Creating pairplot...")
    pairplot = create_pairplot(df)
    pairplot.savefig('feature_pairplot.png')
    plt.close()
    
    print("Creating regional analysis plots...")
    regional_plot = create_regional_analysis(df)
    regional_plot.savefig('regional_analysis.png')
    plt.close()
    
    # Combine all plots into one figure
    print("\nCombining plots...")
    fig = plt.figure(figsize=(15, 30))
    
    # Add correlation heatmap
    plt.subplot(3, 1, 1)
    img = plt.imread('correlation_heatmap.png')
    plt.imshow(img)
    plt.axis('off')
    plt.title('Correlation Heatmap')
    
    # Add pairplot
    plt.subplot(3, 1, 2)
    img = plt.imread('feature_pairplot.png')
    plt.imshow(img)
    plt.axis('off')
    plt.title('Feature Pairplot')
    
    # Add regional analysis
    plt.subplot(3, 1, 3)
    img = plt.imread('regional_analysis.png')
    plt.imshow(img)
    plt.axis('off')
    plt.title('Regional Analysis')
    
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()
    
    print(f"Exploratory analysis completed. Results saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python 02_exploratory_analysis.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)