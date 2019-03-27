# Running Workflow

After preparing conda environment and making the sample sheet, you are ready to run the workflow. 

## Quick Start

An example workflow script 'main.py' is provided in the 'examples' directory. This file can be moved to the main repository directory, edited with the correct information, and run for an easy start. To run the script enter `python main.py`.

## Normal Start

You must first load the RNAseq module. Make sure you are in the repository directory.

```
from modules import RNAseq
```

Next, initialize the RNAseq object, and specify the correct arguments.

```
rnaseq = RNAseq(
        projectID = 'PROJECT_001',
        projectName = 'RNA-seq Test',
        organism = 'S. cerevisiae',
        cores = 1,
        outDir = './outdir',
        seqDir = './sequences'
)
```

Add sample info from your sample sheet to the RNAseq object.

```
rnaseq.sample_info('./samples.tsv')
```

Run read quality control on the FASTQ files using FastQC.

```
rnaseq.fastqc()
```

Generate a STAR aligner genomic index. You must supply the GTF annotation file and FASTA genomic sequences file.

```
rnaseq.star_genome(gtf = './genes.gtf', fasta = './genome.fasta')
```

Align the reads to the genome using STAR aligner.

```
rnaseq.star_align()
```

Finally, annotate the reads and get the counts per transcript.

```
rnaseq.count_reads()
```
