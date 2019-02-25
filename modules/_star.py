
## generating the genomic index for the STAR aligner

def star_genome(self, genomeGTF, genomeFasta):
	self.gtf = genomeGTF
	self.fasta = genomeFasta
	# creating the output directory if it doesn't exist
	outdir = os.path.join(self.outdir, 'genome')
	if not os.path.isdir(outdir): os.mkdir(outdir)
	# compiling the STAR command
	command = [
		'STAR',
		'--runThreadN ' + str(self.cores),
		'--runMode genomeGenerate',
		'--genomeDir ' + outdir,
		'--genomeFastaFiles ' + fasta,
		'--sjdbGTFfile ' + self.gtf
	]
	# sending the STAR command
	subprocess.run(' '.join(command), shell=True, check=True)

## aligning reads with the STAR aligner

def star_align(self):
	# creating output directory if it doesn't exist
	outdir = os.path.join(self.outdir, 'alignment')
	if not os.path.isdir(outdir): os.mkdir(outdir)
	# compiling the command to send to STAR
	for sample,info in self.samples.items():
		command = [
			'STAR',
			'--runThreadN ' + str(self.cores),
			'--genomeDir ' + os.path.join(seqObject.outdir, 'genome'),
			'--outFileNamePrefix ' + os.path.join(outdir, sample + '_'),
			'--outSAMtype BAM SortedByCoordinate'
		]
		# if paired end run, grab the R1 and R2 files, otherwise just supply the R1 file
		if seqObject.paired:
			command.append('--readFilesIn ' + info.get('R1') + ' ' + info.get('R2'))
		else:
			command.append('--readFilesIn ' + info.get('R1'))
		# submit the command
		subprocess.run(' '.join(command), shell=True, check=True)
