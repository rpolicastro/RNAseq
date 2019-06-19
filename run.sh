#!/bin/bash

set -e


## Checks and Preparations
## ----------

## load settings

source settings.conf

## check settings

if [ ! -f "${REPDIR}/main.py" ] && echo "WARNING: Repository directory is invalid." && exit 1
if [ ! -d "${SEQDIR}" ] && echo "WARNING: Sequence directory does not exist." && exit 1
if [ ! -f "$GENOME_GTF" ] && echo "WARNING: Genome GTF does not exist." && exit 1
if [ ! -f "$GENOME_FASTA" ] && echo "WARNING: Genome FASTA does not exist." && exit 1
if [ ! -f "$SAMPLE_SHEET" ] && echo "WARNING: Sample sheet does not exist." && exit 1
if [ ! -n "$PROJECT_ID" ] && echo "WARNING: Project ID not set." && exit 1
if [ ! -n "$PROJECT_NAME" ] && echo "WARNING: Project name not set." && exit 1
if [ ! -n "$ORGANISM" ] && echo "WARNING: Organism name not set." && exit 1
if [ ! -n "$CORES" ] && echo "WARNING: Cores not set." && exit 1

## Create important directories

if [ ! -d "$OUTDIR" ] && mkdir -p $OUTDIR


## Download and Start Singularity Container
## ----------

## Download singularity container

# Create directory to download singularity container to if it doesn't exist
if [ ! -d "${OUTDIR}/container" ]
then
	mkdir -p ${OUTDIR}/container
	cd ${OUTDIR}/container
fi

# Download singularity container if it doesn't exist yet
if [ ! -f "${OUTDIR}/container/RNAseq_latest.sif" ]
then
	echo "...downloading singularity container: RNAseq_latest.sif"
	singularity pull shub://rpolicastro/RNAseq
	[ -f "${OUTDIR}/container/RNAseq_latest.sif" ] && echo "...singularity container downloaded" || exit 1
else
	echo "...singularity container already exists in ${OUTDIR}/container"
fi

# Change back to the repository directory
cd $REPDIR

## Activate singularity container

echo "...shelling into singularity container"

singularity shell \
-e -C \
-B $REPDIR, \
$OUTDIR, \
$SEQDIR, \
$(dirname $GENOME_GTF) \
$(dirname $GENOME_FASTA) \
$(dirname $SAMPLE_SHEET) \
-H $REPDIR \
${OUTDIR}/container/RNAseq_latest.sif


## Run RNA-seq Automation Script
## ----------

## Activate conda environment

source activate rnaseq-automation

## Run RNA-seq automation script

python main.py \
--projectID $PROJECT_ID \
--projectName $PROJECT_NAME \
--organism $ORGANISM \
--cores $CORES \
--outDir $OUTDIR \
--seqDir $SEQDIR \
--sampleSheet $SAMPLE_SHEET \
--genomeGTF $GENOME_GTF \
--genomeFasta $GENOME_FASTA

exit 0
