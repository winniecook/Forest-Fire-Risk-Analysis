#!/usr/bin/env nextflow

params.input = "$baseDir/data/forests.csv"
params.outdir = "$baseDir/results"

process PREPROCESS {
    publishDir "${params.outdir}", mode: 'copy'

    input:
    path input_file

    output:
    path 'preprocessed_data.csv'

    script:
    """
    python $baseDir/scripts/01_data_preprocessing.py $input_file preprocessed_data.csv
    """
}

process EXPLORATORY_ANALYSIS {
    publishDir "${params.outdir}", mode: 'copy'

    input:
    path preprocessed_data

    output:
    path 'exploratory_plots.png'

    script:
    """
    python $baseDir/scripts/02_exploratory_analysis.py $preprocessed_data exploratory_plots.png
    """
}

process STATISTICAL_MODELING {
    publishDir "${params.outdir}", mode: 'copy'

    input:
    path preprocessed_data

    output:
    path 'model_results.txt'

    script:
    """
    python $baseDir/scripts/03_statistical_modeling.py $preprocessed_data model_results.txt
    """
}

process VISUALIZATION {
    publishDir "${params.outdir}", mode: 'copy'

    input:
    path preprocessed_data
    path model_results

    output:
    path 'final_visualizations.pdf'

    script:
    """
    python $baseDir/scripts/04_visualization.py $preprocessed_data $model_results final_visualizations.pdf
    """
}

workflow {
    input_ch = channel.fromPath(params.input)
    
    preprocessed_ch = PREPROCESS(input_ch)
    EXPLORATORY_ANALYSIS(preprocessed_ch)
    model_results_ch = STATISTICAL_MODELING(preprocessed_ch)
    VISUALIZATION(preprocessed_ch, model_results_ch)
}