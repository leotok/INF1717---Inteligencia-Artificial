import re,os,sys,glob,operator
import numpy as np
from filters import filter_text

def generate_reviews(folder,classification):
    files = glob.glob(folder+"/*.txt")
    reviews_list = []

    for i, review in enumerate(files):
        reviews_list.append(Review(review,classification))

        if i%1000 == 0 and i != 0:
            print i, "files read"
    return reviews_list


class Review:
    word_index = {}
    word_count = {}
    curr_index = 0
    def __init__(self,rev_file,classification):
        # rev_file: path to .txt review. classification:'p'/'n'

        self.name = re.sub("(.*\/)","",rev_file)
        self.name = self.name.strip(".txt")
        self.classification = classification
        
        with open(rev_file, 'r') as f:
        	raw = f.read()

        self.filtered = filter_text(raw)

        self.feature_frequency = {}

        for word in self.filtered:

            try:
                self.feature_frequency[word] += 1
            except KeyError:
                self.feature_frequency[word] = 1
            try:
                rpnse = Review.word_index[word]
                Review.word_count[word] += 1	 
            except KeyError:
                Review.word_index[word] = Review.curr_index
                Review.word_count[word] = 1
                Review.curr_index += 1
   
    def most_frequent_words(num_words):
        features = sorted(Review.word_count, key=Review.word_count.get, reverse=True)[:num_words]
        features_index = {}
        i=0
        for feature in features:
            features_index[feature] = i
            i+=1
        return features_index
    most_frequent_words = staticmethod(most_frequent_words)
    
    

def generate_arff(reviews,filename,features=None):
	
	with open(filename, 'w') as f:

		f.write("@relation review\n")

		if not features:
			features = Review.most_frequent_words(200)

		word_count_for_review = {}
		rev_data = ""
		wrote_features = False
		for i, review in enumerate(reviews):

			if i % 1000 == 0 and i != 0:
				print i

			word_count_for_review[review] = {}

			for feature in features:
				if not wrote_features:
					f.write("@attribute "+feature+" numeric\n")
				
				try:
					word_count_for_review[review][feature] = review.feature_frequency[feature]
				except:
					word_count_for_review[review][feature] = 0

				rev_data += str(word_count_for_review[review][feature]) + ", "

			if not wrote_features:
				wrote_features = True
			rev_data += review.classification+"\n"

		f.write("@attribute class {p,n}\n")
		f.write("\n@data\n")

		f.write(rev_data)		

	return features	

def generate_vector(reviews,features=None):
    vect = []
    if not features:
        features = Review.most_frequent_words(1000)
    num_features = len(features)
    print len(features)
    i = 0
    for review in reviews:
        if i%1000 == 0:
            print i
        i+=1
        freqs = [0]*num_features
        for word in review.feature_frequency.keys():
            try:
                freqs[features[word]] = review.feature_frequency[word]
            except KeyError:
                continue
        if review.classification == 'p':
            freqs.append(1)
        else:
            freqs.append(0)
        vect.append(freqs)
    return vect,features

    
def run():

	with open("words_collection.txt", "r") as f:
		words_collection = f.read()
	words_collection = words_collection.split()

	working_folder = os.getcwd()+"/movie_review_dataset/"

	print "Reading part1/neg..."
	reviews = generate_reviews(working_folder+"part1/neg",'n')
	print "Reading part1/pos..."
	reviews += generate_reviews(working_folder+"part1/pos",'p')
	print "Reading part2/neg..."
	reviews += generate_reviews(working_folder+"part2/neg",'n')
	print "Reading part2/pos..."
	reviews += generate_reviews(working_folder+"part2/pos",'p')

    # working_folder = os.getcwd()+"/sample_neg/"
    # reviews = generate_reviews(working_folder,'n')

    # working_folder = os.getcwd()+"/sample_pos/"
    # reviews += generate_reviews(working_folder,'p')

	print "Generating 'reviews_dataset.arff'..."

	features_used = generate_arff(reviews,"reviews_dataset_words_col.arff", features=words_collection)	

	print "Done!"
    

if __name__ == '__main__':

	run()