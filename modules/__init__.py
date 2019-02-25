
import os
import subprocess

class RNAseq(object):

	def __init__(self, projectID, projectName, organism, cores=1, outDir=None, paired=False):
                self.project_id = projectID
                self.project_name = projectName
                self.organism = organism
                self.cores = cores
                self.paired = paired
                self.outdir = outDir
                if not outDir: self.outdir = os.getcwd()

	from ._fastqc import fastqc
	from ._samplesheet import sample_sheet
	from ._star import star_genome, star_align
	from ._subread import feature_count
