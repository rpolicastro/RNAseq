
import subprocess
import os
import pandas as pd
import csv

def count_reads(self, genomeGTF=None, genomeFasta=None):

	# set genome GTF and Fasta if defined
	if genomeGTF is not None: self.genome_gtf = genomeGTF
	if genomeFasta is not None: self.genome_fasta = genomeFasta

	# create output directory if it doesn't exist
	outdir = os.path.join(self.outdir, 'counts')
	if not os.path.isdir(outdir): os.mkdir(outdir)

	# function to count reads
	def _count(self, row):
		# start building command
		command = [
			'featureCounts',
			'-F GTF -t exon -g gene_id',
			'--minOverlap 10 --largestOverlap',
			'--primary -s 2 -T', str(self.cores)
		]
		# add paired end options where appropriate
		if row['paired'].lower() == 'paired': command.extend(['-p -B -C'])
		# finishing command
		command.extend([
                       '-a', self.genome_gtf,
			'-o', os.path.join(self.outdir, 'counts', row['sample_ID'] + '_' + row['condition'] + '_' + str(row['replicate']) + '_counts.tsv'),
			os.path.join(self.outdir, 'aligned', row['sample_ID'] + '_' + row['condition'] + '_' + str(row['replicate']) + '_Aligned.sortedByCoord.out.bam')
		])
		command = ' '.join(command)
		# submit command
		subprocess.run(command, shell=True, check=True)

	# run counting command
	self.sample_sheet.apply(lambda row: _count(self=self, row=row), axis=1)

	# combine results files
	count_files = [f for f in os.listdir(os.path.join(self.outdir, 'counts')) if f.endswith('_counts.tsv')]
	master_created = False
	for count_file in count_files:
		df = pd.read_csv(os.path.join(self.outdir, 'counts', count_file), sep='\t', header=0, index_col=0, skiprows = 1)
		df = df.iloc[:,5].to_frame()
		df.iloc[:,0] = pd.to_numeric(df.iloc[:,0])
		if not master_created:
			master = df
			master_created = True
		else:
			master = master.join(df, how='outer')
	master.to_csv(os.path.join(self.outdir, 'counts', 'counts_merged.tsv'), sep='\t', header=True, index=True, quoting=csv.QUOTE_NONE)
