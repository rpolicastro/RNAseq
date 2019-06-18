#!/bin/bash

## Load settings

source settings.conf

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

python ./modules/main.py
