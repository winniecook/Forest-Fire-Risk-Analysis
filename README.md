# Forest Fire Analysis Pipeline

This project is an advanced data analysis pipeline for forest fire data, using Python and R for analysis, Conda for environment management, Docker for containerization, and Nextflow for workflow management.

## Project Structure

```
forest-fire-analysis/
├── data/
│   └── forests.csv
├── scripts/
│   ├── 01_data_preprocessing.py
│   ├── 02_exploratory_analysis.py
│   ├── 03_statistical_modeling.py
│   └── 04_visualization.R
├── notebooks/
│   └── forest_fire_analysis.ipynb
├── results/
│   └── .gitkeep
├── Dockerfile
├── environment.yml
├── main.nf
├── nextflow.config
└── README.md
```

## Setup Instructions

1. Install Conda, Docker, and Nextflow on your system.

2. Clone this repository:
   ```
   git clone https://github.com/yourusername/forest-fire-analysis.git
   cd forest-fire-analysis
   ```

3. Create the Conda environment:
   ```
   conda env create -f environment.yml
   ```

4. Activate the Conda environment:
   ```
   conda activate forest-fire-env
   ```

5. Build the Docker image:
   ```
   docker build -t forest-fire-analysis .
   ```

6. Run the Nextflow pipeline:
   ```
   nextflow run main.nf
   ```

## Pipeline Steps

1. **Data Preprocessing**: Cleans the data, handles missing values, and performs feature engineering.
2. **Exploratory Analysis**: Creates various plots to visualize relationships in the data.
3. **Statistical Modeling**: Performs statistical analysis and builds predictive models.
4. **Visualization**: Creates final visualizations and summary reports.

## Results

After running the pipeline, you can find the results in the `results` directory:

- `preprocessed_data.csv`: Cleaned and preprocessed dataset
- `exploratory_plots.png`: Exploratory data analysis plots
- `model_results.txt`: Statistical modeling results
- `final_visualizations.pdf`: Final visualization report

## Interactive Analysis

For more in-depth, interactive analysis of the forest fire data:

1. Ensure you have run the Nextflow pipeline to generate the preprocessed data.
2. Navigate to the `notebooks` directory.
3. Start JupyterLab by running `jupyter lab` in your terminal.
4. Open the `forest_fire_analysis.ipynb` notebook.
5. Run the cells to perform additional analysis and visualization.

This notebook complements the automated pipeline by allowing for more flexible exploration of the data and results.

## Customization

You can customize the pipeline by modifying the following files:

- `nextflow.config`: Adjust computational resources and output directories
- `environment.yml`: Add or remove dependencies
- `main.nf`: Modify the workflow structure or add new processes

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or encounter any problems.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.