
## fastqc to get read quality

def fastqc(self):
	# create output directory if it doesn't exist
	outdir = os.path.join(self.outdir, 'fastqc')
	if not os.path.isdir(outdir): os.mkdir(outdir)
	# if paired end, grab both R1 and R2, otherwise just get R1
	if self.paired:
		fastq_files = [' '.join([value.get('R1'), value.get('R2')]) for key,value in self.samples.items()]
		fastq_files = ' '.join(fastq_files)
	else:
		fastq_files = [value.get('R1') for key,value in self.samples.items()]
		fastq_files = ' '.join(fastq_files)
	# compile command to send to fastqc
	command = [
		'fastqc',
		'-o ' + outdir,
		'-t ' + str(self.cores),
		fastq_files
	]
	# run command
	subprocess.run(' '.join(command), shell=True, check=True)
