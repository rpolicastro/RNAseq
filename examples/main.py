#!/usr/bin/env python

from modules import RNAseq
import os

os.chdir('~/workdir')

## loading the sequencing object
rnaseq = RNAseq(
	projectID = 'PROJECT_001',
	projectName = 'RNA-seq Test',
	organism = 'S. cerevisiae',
	cores = 1,
	outDir = './outdir',
	seqDir = './sequences'
)

## adding sample info to sequencing object
rnaseq.sample_info('./samples.tsv')

## fastQC check of raw reads
rnaseq.fastqc()

## generating the STAR genome index
rnaseq.star_genome(
	gtf = './genes.gtf',
	fasta = './genome.fasta'
)
## aligning fastq files to genome
rnaseq.star_align()

## counting reads
rnaseq.count_reads()
