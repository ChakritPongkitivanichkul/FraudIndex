import numpy as np
from sys import argv
import pandas as pd
# from pybliometrics.scopus import AbstractRetrieval
# from pybliometrics.scopus import ScopusSearch
import pickle

###############################################################################
###############################################################################
###############################################################################

def IDextract(filename):

	df = pd.read_csv(filename)

	authorsID = df["Author(s) ID"].to_numpy()
	
	IDset = set()

	for a in authorsID:

		IDset.update(a.split(";")[:-1])

	return(IDset)

def unpackdict(filename):

	with open(filename, 'rb') as f:
		
		loaded_dict = pickle.load(f)
	
	return(loaded_dict)

###############################################################################
###############################################################################
###############################################################################

def main():

	userset = IDextract(argv[1])

	Fsources = ['SC','WS','KJ'] #Suphat Chupradit, Wanich Suksatan, Kittisak Jermsittiparsert

	for fname in Fsources:

		layer1 = unpackdict(fname+'_layer1.pkl')

		intersectlayer1 = dict()

		for i in userset:
			
			nametemp = layer1.get(i)

			if nametemp != None:

				intersectlayer1[i] = nametemp

		if len(intersectlayer1) != 0:

			print("#############################################################################")
			print("The Fraud Index = 1 (You have at least one common coauthor with the culprits: {})".format(fname))
			print("They are the following:")
			print(intersectlayer1)
			print("#############################################################################")

			continue

		layer2 = unpackdict(fname+'_layer2.pkl')

		intersectlayer2 = dict()

		for i in userset:
			
			nametemp = layer2.get(i)

			if nametemp != None:

				intersectlayer2[i] = nametemp

		if len(intersectlayer2) != 0:

			print("#############################################################################")
			print("The Fraud Index = 2 (You have at least one common coauthor with coauthor of the culprits: {})".format(fname))
			print("They are the following:")
			print(intersectlayer2)
			print("#############################################################################")

			continue


main()
