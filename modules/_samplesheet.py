
## loading sample sheet into dict
## sample sheet should be tab delimted text file
## colum headers optional but recommended
##   colnames should be 'sample_ID', 'sample_name', 'R1_file', and 'R2_file'
##   'sample_ID' should be a simple ID name for the sample (ex. SAMPLE001)
##   'sample_name' should be a descriptive name for the sample without spaces (ex. GENE_KD)

def sample_sheet(self, sampleSheet, fastqDir):
	# open sample sheet to grab sample info
	with open(sampleSheet) as file:
		# columns into list of lists
		samples = [x.strip().split('\t') for x in file if not x.startswith('sample_ID')]
		# turn list of list into named dictionary
		if self.paired:
			self.samples = {x[0]:{'name':x[1],'R1':os.path.join(fastqDir, x[2]), 'R2':os.path.join(fastqDir, x[3])} for x in samples}
		else:
			self.samples = {x[0]:{'name':x[1],'R1':os.path.join(fastqDir, x[2]), 'R2':None} for x in samples}
