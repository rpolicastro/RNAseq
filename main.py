
from modules import RNAseq

## loading the sequencing object
rnaseq = RNAseq(
	projectID = 'PROJECT_001',
	projectName = 'RNA-seq Test',
	organism = 'S. cerevisiae',
	cores = 1,
	outDir = './outdir',
	paired = True
)
## adding sample info to sequencing object
rnaseq.sample_info('./samples.tsv', fastqDir = './sequences')

## fastQC checkinf of raw reads
rnaseq.fastqc()

## generating the STAR genome index
rnaseq.star_genome(
	gtf = './genes.gtf',
	fasta = './genome.fa',
)
## aligning fastq files with genome
rnaseq.star_align()

## counting reads
rnaseq.feature_count()
