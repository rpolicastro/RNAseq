# RNAseq
Automation of RNA-seq Workflow

# Getting Started

## Cloning Repository

To get started, you must first clone the RNAseq automation repository. Navigate to a directory you would like to clone the repo to and enter `git clone https://github.com/rpolicastro/RNAseq.git`.

## Preparing Conda Environment

This workflow takes advantage of the [conda](https://conda.io/en/latest/) package manager and virtual environment. The conda package manager installs both the main software and all dependencies into a 'virtual environment' to ensure compatabilty. Furthermore, the provided 'environment.yml' file will reproduce the software environment used when developing the workflow. This ensures prolonged compatabilty and reproducibility.

Before creating the environment, you must first install miniconda.
1. [Install miniconda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html?highlight=conda), and make sure that conda is in your PATH.
2. Update conda to the latest version `conda update conda`.

You are now read to create the virtual sofware environment, and download all software and dependencies. If you would like to recreate the environment used when writing the original workflow, navigate to the main repository directory and enter `conda create -f environment.yml`. If you would like to create your own environment with the latest software versions, follow the steps below.

1. Create the new environment and specify the software to include in it.
```
conda create -n rnaseq-automation -y -c conda-forge -c bioconda \
pandas fastqc star samtools subread
```
2. Update the software to the latest compatible versions.
```
conda update -n rnaseq-automation -y -c conda-forge -c bioconda --all
```

If you wish to use any of the software in the environment outside of the workflow you can type `conda activate rnaseq-automation`. You can deactivate the environment by closing your terminal or entering `conda deactivate`.

## Creating Sample Sheet

In order to keep track of samples, this workflow requires the creation of a sample sheet. An example sheet [samples.tsv](https://github.com/rpolicastro/RNAseq/blob/master/examples/samples.tsv) is provided in the *examples* directory. It is important to follow exact formatting of this sheet, as the information within it is used in various stages of the workflow.

| Column | Description |
| ------ | ----------- |
| sample_ID | Short sample identifier (e.g. A001). |
| condition | Experimental condition (e.g. EWSR1_KD). |
| replicate | Sample replicate number (e.g. 1). |
| R1 | Name of R1 fastq file of experimental condition. |
| R2 | Name of R2 fastq file of experimental condition (put NA if single end). |
| paired | Put 'paired' or 'unpaired' depending on the run. |

## Running the Workflow

After getting the conda environment ready and the sample sheet prepared, you are ready to [run the workflow](https://github.com/rpolicastro/RNAseq/blob/master/docs/run_workflow.md).

# Built With

This workflow would not be possible without the great software listed below.

- [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) - Read quality control.
- [STAR](https://github.com/alexdobin/STAR) - Read aligner.
- [Samtools](http://www.htslib.org/) - SAM/BAM manipulation.
- [Subread](http://subread.sourceforge.net/) - Read annotation and counting.
