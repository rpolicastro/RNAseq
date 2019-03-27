

import pandas as pd
import os
import subprocess

## generating STAR genomic index

def star_genome(self, genomeGTF, genomeFasta):
	self.genome_gtf = genomeGTF
	self.genome_fasta = genomeFasta
	
	# creating directory for genomic index
	outdir = os.path.join(self.outdir, 'genome')
	if not os.path.isdir(outdir): os.mkdir(outdir)

	# building command
	command = [
		'STAR',
		'--runThreadN', str(self.cores),
		'--runMode genomeGenerate',
		'--genomeDir', outdir,
		'--genomeFastaFiles', self.genome_fasta,
		'--sjdbGTFfile', self.genome_gtf
	]
	command = ' '.join(command)

	# submitting command
	subprocess.run(command, shell=True, check=True)

## aligning reads using STAR

def star_align(self):

	# creatig directory for aligned files
	outdir = os.path.join(self.outdir, 'aligned')
	if not os.path.isdir(outdir): os.mkdir(outdir)

	# defining function to align reads
	def _align(self, row):

		# making command
		command = [
			'STAR',
			'--runThreadN', str(self.cores),
			'--genomeDir', os.path.join(self.outdir, 'genome'),
			'--outFileNamePrefix', os.path.join(self.outdir, 'aligned', row['sample_ID'] + '_' + row['condition'] + '_' + str(row['replicate']) + '_'),
			'--outSAMtype BAM SortedByCoordinate',
			'--readFilesIn', os.path.join(self.seqdir, row['R1'])
		]
		if row['paired'].lower() == 'paired': command.append(os.path.join(self.seqdir, row['R2']))
		command = ' '.join(command)

		# running command
		subprocess.run(command, shell=True, check=True)

	# looping through fastq files and aligning them
	self.sample_sheet.apply(lambda x: _align(self=self, row=x), axis=1)

