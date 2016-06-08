#!/usr/bin/python

import os
from collections import *
path = os.path.dirname(__file__)

txt_path = path + "/sample/3418_3.txt"
sample_folder = path + "/sample"
arff_path = path + "/words.txt"
txt_sample = path + "/txt_sample.txt"

def wordCount(file_path, dictionary, posneg):

	file = open(file_path, "r")

	ret = ""
	counter = 0
	wordcount = {}

	for word in dictionary:
		wordcount[word] = 0

	for word in file.read().split():
		if word not in wordcount:
			pass
		else:
			wordcount[word] += 1

			for k,v in wordcount.items():
				if counter < len(dictionary):
					ret += str(v) + ","
				else:
					ret += str(v)
				counter += 1

	if posneg == "negativo":
		ret += " negativo"
	else:
		ret += " positivo"


	return(ret)


arff = open(arff_path, "r")

words = []

for word in arff.read().split():
	words.append(word)

print(len(words))

print(wordCount(txt_path, words, "negativo"))


for file_path in os.listdir(sample_folder):
	print((sample_folder + "/" + file_path))

	file = (sample_folder + "/" + file_path)

