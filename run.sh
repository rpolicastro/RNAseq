#!/bin/bash

set -e


## Checks and Preparations
## ----------

## load settings

source settings.conf

## check settings

if [ ! -f "${REPDIR}/main.py" ]; then echo "WARNING: Repository directory is invalid." && exit 1; fi
if [ ! -d "${SEQDIR}" ]; then echo "WARNING: Sequence directory does not exist." && exit 1; fi
if [ ! -f "$GENOME_GTF" ]; then echo "WARNING: Genome GTF does not exist." && exit 1; fi
if [ ! -f "$GENOME_FASTA" ]; then echo "WARNING: Genome FASTA does not exist." && exit 1; fi
if [ ! -f "$SAMPLE_SHEET" ]; then echo "WARNING: Sample sheet does not exist." && exit 1; fi
if [ ! -n "$PROJECT_ID" ]; then echo "WARNING: Project ID not set." && exit 1; fi
if [ ! -n "$PROJECT_NAME" ]; then echo "WARNING: Project name not set." && exit 1; fi
if [ ! -n "$ORGANISM" ]; then echo "WARNING: Organism name not set." && exit 1; fi
if [ ! -n "$CORES" ]; then echo "WARNING: Cores not set." && exit 1; fi

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
if [ ! -f "${OUTDIR}/container/RNAseq_latest.sif" ]
then
	echo "...downloading singularity container: RNAseq_latest.sif"
	singularity pull shub://rpolicastro/RNAseq
	[ -f "${OUTDIR}/container/RNAseq_latest.sif" ]; then echo "...singularity container downloaded"; else exit 1; fi
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
