
import pandas as pd

def sample_sheet(self, sampleSheet):
	self.sample_sheet = pd.read_csv(sampleSheet, sep='\t', header=0, index_col=False)
