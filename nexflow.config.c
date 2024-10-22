docker {
    enabled = true
}

process {
    container = 'forest-fire-analysis'
}

params {
    input = "$baseDir/data/forests.csv"
    outdir = "$baseDir/results"
}

executor {
    name = 'local'
    cpus = 4
    memory = '8 GB'
}

timeline {
    enabled = true
    file = "${params.outdir}/timeline.html"
}

report {
    enabled = true
    file = "${params.outdir}/report.html"
}