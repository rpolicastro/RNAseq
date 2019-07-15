#!/bin/bash

set -e


## Checks and Preparations
## ----------

## load settings

source settings.conf

## Create important directories

if [ ! -d "$OUTDIR" ]; then mkdir -p $OUTDIR; fi


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
if [ ! -f "${OUTDIR}/container/rnaseq_automation_1.0.0.sif" ]
then
	echo "...downloading singularity container: RNAseq_latest.sif"
	singularity pull -U library://rpolicastro/default/rnaseq_automation:1.0.0
	if [ -f "${OUTDIR}/container/rnaseq_automation_1.0.0.sif" ]
	then 
		echo "...singularity container downloaded"
	else 
		echo "Container not found"
		exit 1
	fi
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
$(dirname $GENOME_GTF), \
$(dirname $GENOME_FASTA), \
$(dirname $SAMPLE_SHEET) \
-H $REPDIR \
${OUTDIR}/container/rnaseq_automation_1.0.0.sif


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
