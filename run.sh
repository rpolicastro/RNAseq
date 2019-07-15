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
fi

# Download singularity container if it doesn't exist yet
if [ ! -f "${OUTDIR}/container/rnaseq_automation_1.0.1.sif" ]
then
	echo "...downloading singularity container: rnaseq_automation_1.0.1.sif"
	singularity pull -U library://rpolicastro/default/rnaseq_automation:1.0.1
	mv rnaseq_automation_1.0.1.sif ${OUTDIR}/container
	
	if [ -f "${OUTDIR}/container/rnaseq_automation_1.0.1.sif" ]
	then 
		echo "...singularity container downloaded"
	else 
		echo "Container not found"
		exit 1
	fi
else
	echo "...singularity container already exists in ${OUTDIR}/container"
fi

## Activate singularity container

echo "...running singularity container"

SINGULARITYENV_PROJECT_ID=$PROJECT_ID \
SINGULARITYENV_PROJECT_NAME=$PROJECT_NAME \
SINGULARITYENV_ORGANISM=$ORGANISM \
SINGULARITYENV_CORES=$CORES \
SINGULARITYENV_REPDIR=$REPDIR \
SINGULARITYENV_OUTDIR=$OUTDIR \
SINGULARITYENV_SEQDIR=$SEQDIR \
SINGULARITYENV_SAMPLE_SHEET=$SAMPLE_SHEET \
SINGULARITYENV_GENOME_GTF=$GENOME_GTF \
SINGULARITYENV_GENOME_FASTA=$GENOME_FASTA \
singularity run \
-eCB \
$REPDIR,\
$OUTDIR,\
$SEQDIR,\
$(dirname $GENOME_GTF),\
$(dirname $GENOME_FASTA),\
$(dirname $SAMPLE_SHEET) \
-H $REPDIR \
${OUTDIR}/container/rnaseq_automation_1.0.1.sif
