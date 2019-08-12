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

singularity exec \
-eCB \
$REPDIR,\
$OUTDIR,\
$SEQDIR,\
$(dirname $GENOME_GTF),\
$(dirname $GENOME_FASTA),\
$(dirname $SAMPLE_SHEET) \
-H $REPDIR \
${OUTDIR}/container/rnaseq_automation_1.0.1.sif \
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
