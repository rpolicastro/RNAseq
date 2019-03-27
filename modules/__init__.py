
import os

class RNAseq(object):

	def __init__(self, projectID, projectName, organism, seqDir, cores=1, outDir=None):
		self.project_id = projectID
		self.project_name = projectName
		self.organism = organism
		self.cores = cores
		self.outdir = outDir
		self.seqdir = seqDir
		if not outDir: self.outdir = os.getcwd()

	from ._samplesheet import sample_sheet
	from ._fastqc import fastqc
	from ._star import star_genome, star_align
	from ._subread import count_reads
