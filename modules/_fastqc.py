
import os
import subprocess
import pandas as pd

## fastqc to get read quality

def fastqc(self):

	# create output directory if it doesn't exist
	outdir = os.path.join(self.outdir, 'fastqc')
	if not os.path.isdir(outdir): os.mkdir(outdir)

	# start compiling fastq command
	fastq_files = self.sample_sheet.loc[:,['R1','R2']].melt().set_index('variable').dropna().value.tolist()
	fastq_files = [os.path.join(self.seqdir, fastq) for fastq in fastq_files]
	fastq_files = ' '.join(fastq_files)	

	command = [
		'fastqc',
		'-o', outdir,
		'-t', str(self.cores),
		fastq_files
	]
	command = ' '.join(command)

	# run command
	subprocess.run(command, shell=True, check=True)
