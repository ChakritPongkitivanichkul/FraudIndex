import numpy as np
from sys import argv
import pandas as pd
from pybliometrics.scopus import AbstractRetrieval
from pybliometrics.scopus import ScopusSearch
import pickle

###############################################################################
###############################################################################
###############################################################################


def generatelist(nameorid):

	if isinstance(nameorid, str):
		au = ScopusSearch('AUTHOR-NAME({})'.format(nameorid))
	elif isinstance(nameorid, int):
		au = ScopusSearch('AU-ID({})'.format(nameorid))

	df = pd.DataFrame(pd.DataFrame(au.results))

	nextlist = df[['author_names','author_ids']].to_numpy()

	nameid_dict = dict()

	for i,nameid in enumerate(nextlist):

		if nameid[0] == None:
			continue

		namelist = nameid[0].split(";")
		
		idlist = nameid[1].split(";")
		
		for i,name in enumerate(namelist):
		
			#nameid_dict[idlist[i]] = name.split(",")[0]
			nameid_dict[idlist[i]] = name

	return(nameid_dict)

def cascade(nameorid, level=3):

	dict_layer = []

	seed = [nameorid]

	for i in range(level):

		leveldict = dict()

		for s in seed:

			sdict = generatelist(s)

			leveldict.update(sdict)

		dict_layer.append(leveldict)

		seed = [int(id) for id in leveldict.keys()]

	return(dict_layer)

###############################################################################
###############################################################################
###############################################################################


