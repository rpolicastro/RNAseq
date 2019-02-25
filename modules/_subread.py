
# using featureCount from subread to count reads

def feature_count(self):
	# creating the output directory if it doesn't exist
	outdir = os.path.join(self.outdir, "results", "counts")
	if not os.path.isdir(outdir): os.mkdir(outdir)
	# getting the paths for the aligned bam files
	bams = [x for x in os.listdir(os.path.join(self.outdir, "alignment")) if x.endswith(".bam")]
	# compiling the command to send to featureCounts
	command = [
		'featureCounts',
		'-a', self.gtf,
		'-o', os.path.join(outdir, 'counts.tsv'),
		' '.join(bams),
		'-F GTF',
		'-t exon',
		'-g gene_id',
		'--minOverlap 10',
		'--largestOverlap',
		'--primary',
		'-s 2',
		'-J',
		'-G', self.fasta,
		'-T', str(self.cores)
	]
	# if it's a paired end run add a few more options
	if self.paired:
		command.extend(['-p', '-B', '-C'])
	# submit the command
	subread.run(' '.join(command), shell=True, check=True)			
