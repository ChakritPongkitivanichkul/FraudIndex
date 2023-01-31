import numpy as np
from sys import argv
import pandas as pd

def IDextract(filename):

	df = pd.read_csv(filename)

	authorsID = df["Author(s) ID"].to_numpy()
	
	IDset = set()

	for a in authorsID:
		IDset.update(a.split(";")[:-1])

	return(IDset)

commonids = IDextract(argv[1]).intersection(IDextract(argv[2]))

print(commonids)