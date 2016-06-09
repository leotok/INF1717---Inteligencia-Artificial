import re,os,sys,glob,operator
import numpy as np
from filters import filter_text
from arff_generator import *




if __name__ == '__main__':
	
	working_folder = os.getcwd()+"/movie_review_dataset/"

 	print "Reading part1/neg..."
	reviews = generate_reviews(working_folder+"part1/neg",'n')
	print "Reading part1/pos..."
	reviews += generate_reviews(working_folder+"part1/pos",'p')
	print "Reading part2/neg..."
	reviews += generate_reviews(working_folder+"part2/neg",'n')
	print "Reading part2/pos..."
	reviews += generate_reviews(working_folder+"part2/pos",'p')	

	features = Review.most_frequent_words(1000)

	with open("words_collection.txt","w") as f:
		for word in features:
			f.write(word+"\n")