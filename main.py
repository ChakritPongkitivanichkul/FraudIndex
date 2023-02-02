import generatelayers
import numpy as np
from sys import argv
import pandas as pd
from pybliometrics.scopus import ScopusSearch
import pickle

def main():

	scopusid = int(argv[1])

	aulist=generatelayers.cascade(scopusid,level=2)

	with open('dict_data/{}_layer1.pkl'.format(scopusid), 'wb') as f:
	    pickle.dump(aulist[0], f)

	with open('dict_data/{}_layer2.pkl'.format(scopusid), 'wb') as f:
	    pickle.dump(aulist[1], f)


main()