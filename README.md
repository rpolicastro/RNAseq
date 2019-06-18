# RNAseq
Automation of RNA-seq Workflow

# Getting Started

## Cloning Repository

To get started, you must first clone the RNAseq automation repository. Navigate to a directory you would like to clone the repo to and enter `git clone https://github.com/rpolicastro/RNAseq.git`.

## Installing Singularity

Singularity containers are self contained 'boxes' that house the software and other files necessary for the workflow. The container itself will automatically be downloaded, but you must have the Singularity software installed to both download and use the container. Please refer to the [documentation](https://www.sylabs.io/docs/) on their website.

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

After getting Singularity installed, the sample sheet prepared, and the settings specified, you are now ready to run the workflow. Navigate to the main directory and enter 'bash main.sh'.

# Built With

This workflow would not be possible without the great software listed below.

- [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) - Read quality control.
- [STAR](https://github.com/alexdobin/STAR) - Read aligner.
- [Samtools](http://www.htslib.org/) - SAM/BAM manipulation.
- [Subread](http://subread.sourceforge.net/) - Read annotation and counting.
- [Pandas](https://pandas.pydata.org/) - Dataframe manipulation.
