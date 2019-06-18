#!/usr/bin/env python

from modules import RNAseq
import os
import argparse

## Fetching Arguments
## --------------------

## initialize parser

parser = argparse.ArgumentParser(description = 'Settings for RNA-seq analysis workflow')

## add arguments to parser

parser.add_argument('--projectID', action='store', nargs=1, type=str, required=True, help='Short project ID indicator.')
parser.add_argument('--projectName', action='store', nargs=1, type=str, required=True, help='Descriptive project name.')
parser.add_argument('--organism', action='store', nargs=1, type=str, required=True, help='Organism name.')
parser.add_argument('--cores', action='store', nargs=1, type=int, required=True, help='Number of available cores/threads.')
parser.add_argument('--outDir', action='store', nargs=1, type=str, required=True, help='Directory to output results.')
parser.add_argument('--seqDir', action='store', nargs=1, type=str, required=True, help='Directory containing fastq files.')
parser.add_argument('--sampleSheet', action='store', nargs=1, type=str, required=True, help='Directory and name of sample sheet.')
parser.add_argument('--genomeFasta', action='store', nargs=1, type=str, required=True, help='Directory and name of genomic fasta file.')
parser.add_argument('--genomeGTF', action='store', nargs=1, type=str, required=True, help='Directory and name of genomic GTF file.')

## fetch supplied arguments to parser

args = parser.parse_args()

## Running Workflow
## --------------------

## loading the sequencing object
rnaseq = RNAseq(
	projectID = args.projectID,
	projectName = args.projectName,
	organism = args.organism,
	cores = args.cores,
	outDir = args.outDir,
	seqDir = args.seqDir
)

## adding sample info to sequencing object
rnaseq.sample_sheet(args.sampleSheet)

## fastQC check of raw reads
rnaseq.fastqc()

## generating the STAR genome index
rnaseq.star_genome(
	genomeGTF = args.genomeGTF,
	genomeFasta = args.genomeFasta
)
## aligning fastq files to genome
rnaseq.star_align()

## counting reads
rnaseq.count_reads()
