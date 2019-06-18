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

## Specifying Run Settings

The last step is to set a few settings in the 'settings.conf' file in the main repository directory. An example settings file is provided in the 'DOCS' directory of the repository.

| Setting | Description |
| ------- | ----------- |
|PROJECT_ID| Short alphanumeric project identifier (e.g. A001). |
|PROJECT_NAME| Descriptive name of project (e.g. 'Treatment RNA-seq').|
|ORGANISM| Name of organism (e.g. 'S. cerevisiae').|
|CORES| Number of available cores/threads (e.g. 1).|
|REPDIR| Directory of RNA-seq automation repository (e.g. '.../analysis/RNAseq').|
|OUTDIR| Directory where results will be output (e.g. '.../analysis/results').|
|SEQDIR| Directory containing the fastq files (e.g. '.../analysis/sequences').|
|SAMPLE_SHEET| Direcotry and name of sample sheet (e.g. '.../analysis/samples.tsv').|
|GENOME_GTF| Direcotry and name of genome GTF (e.g. '.../analysis/genome/genes.gtf').|
|GENOME_FASTA| Directory and name of genome fasta (e.g. '.../analysis/genome/genome.fasta').|

## Running the Workflow

After getting Singularity installed, the sample sheet prepared, and the settings specified, you are now ready to run the workflow. Navigate to the main directory and enter 'bash main.sh'.

# Built With

This workflow would not be possible without the great software listed below.

- [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) - Read quality control.
- [STAR](https://github.com/alexdobin/STAR) - Read aligner.
- [Samtools](http://www.htslib.org/) - SAM/BAM manipulation.
- [Subread](http://subread.sourceforge.net/) - Read annotation and counting.
- [Pandas](https://pandas.pydata.org/) - Dataframe manipulation.
