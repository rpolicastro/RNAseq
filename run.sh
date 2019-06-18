#!/bin/bash

## Load settings

source settings.conf

## Create important directories

mkdir -p $OUTDIR

## Download singularity container

mkdir -p ${OUTDIR}/container && cd ${OUTDIR}/container
singularity pull shub://rpolicastro/RNAseq
cd $REPDIR

## Activate singularity container

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
