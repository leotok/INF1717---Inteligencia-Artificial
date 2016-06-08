#!/usr/bin/python

import os
from collections import *
path = os.path.dirname(__file__)

path = path + "/sample/3418_3.txt"

def wordCount(file_path, dictionary):

	file = open(file_path, "r")

	wordcount = {}

	for word in dictionary:
		wordcount[word] = 0

	for word in file.read().split():
		if word not in wordcount:
			pass
		else:
			print(word)
			wordcount[word] += 1

			for k,v in wordcount.items():
				print k, v

wordCount("sample/3418_3.txt",
	["gangster", "not good", "bad", "terrible", "awful"])
