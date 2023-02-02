import numpy as np
from sys import argv
import pandas as pd
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

	##############################################################################################################################
	Fsources = {'57211329338': "Chupradit, Supat", '57219950613': "Suksatan, Wanich", '57214268798': "Jermsittiparsert, Kittisak"}
	###############################################################
	Fsources.update({'57207627195': "Jastaniah, Samyah D."})
	Fsources.update({'57203840418': "Hafsan, Hafsan"})
	Fsources.update({'56299022800': "Tseng, Chengjui"})
	Fsources.update({'57843305300': "Karim, Yasir Salam"})
	Fsources.update({'57776927900': "Hamza, Mohammed Ubaid"})
	Fsources.update({'57196369598': "Hameed, Noora M."})
	Fsources.update({'57218904286': "Sura, Al Zubaidi"})
	Fsources.update({'57871910500': "Almotlaq, Saif Sabbar Kemil"})
	Fsources.update({'36629842700': "Yasin, Ghulam"})
	Fsources.update({'57202042400': "Heri Iswanto, A."})
	Fsources.update({'57865370900': "Dadras, Mahnaz"})
	Fsources.update({'57967351200': "Chorehi, Mohammad Mansouri"})
	###############################################
	Fsources.update({'57222058913': "Rahim, Anum"})
	Fsources.update({'57280388500': "Karim, Sehrish"})
	Fsources.update({'57205441866': "Muthanna, Fares M.S."})
	Fsources.update({'57218762417': "Barkat, Rahil"})
	Fsources.update({'57281021700': "Khwaja, Hajra"})
	Fsources.update({'57225904708': "Khan, Sabeen Sharif"})
	Fsources.update({'57221767465': "Tousif, Sohaib"})
	#Fsources.update({'12808195300': "Nonlaopon, Kamsing", '16229703500': "Botmart, Thongchai", '54890645300': "Weera, Wajaree"})

	print("#############################################################################")
	print("#############################################################################")
	print("#############################################################################")
	print("########################      Start the searches    #########################")
	print("#############################################################################")
	print("#############################################################################")
	print("#############################################################################")

	for fname in Fsources:

		if fname in userset:

			print("#############################################################################")
			print("The Fraud Index = 0 (You have a paper with the culprits: {})".format(Fsources[fname]))
			print("#############################################################################")

			continue

		layer1 = unpackdict('dict_data/'+fname+'_layer1.pkl')

		intersectlayer1 = dict()

		for i in userset:
			
			nametemp = layer1.get(i)

			if nametemp != None:

				intersectlayer1[i] = nametemp

		if len(intersectlayer1) != 0:

			print("#############################################################################")
			print("The Fraud Index = 1 (You have at least one common coauthor with the culprits: {})".format(Fsources[fname]))
			print("They are the following:")
			print(intersectlayer1)
			print("#############################################################################")

			continue

		layer2 = unpackdict('dict_data/'+fname+'_layer2.pkl')

		intersectlayer2 = dict()

		for i in userset:
			
			nametemp = layer2.get(i)

			if nametemp != None:

				intersectlayer2[i] = nametemp

		if len(intersectlayer2) != 0:

			print("#############################################################################")
			print("The Fraud Index = 2 (You have at least one common coauthor with coauthor of the culprits: {})".format(Fsources[fname]))
			print("They are the following:")
			print(intersectlayer2)
			print("#############################################################################")

			continue

	print("#############################################################################")
	print("#############################################################################")
	print("#############################################################################")
	print("##########################      End of searches    ##########################")
	print("#############################################################################")
	print("#############################################################################")
	print("#############################################################################")



main()
