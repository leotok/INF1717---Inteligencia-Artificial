import re
import nltk
from bs4 import BeautifulSoup
import collections

import sys

def _slugify(text):
	# Removes html tags,punctuation and puts everything in lowercase

	slug = BeautifulSoup(text,"html5lib").get_text()
	slug = re.sub("[^a-zA-Z]", " ", slug )  
	slug = slug.lower()
	return slug

def _get_meaningful_words(text):
    
	words = text.split()	

	try:
		stopwords_set = set(nltk.corpus.stopwords.words("english"))
	except:
		nltk.download("stopwords")
		stopwords_set = set(nltk.corpus.stopwords.words("english"))

	filtered = []
	for word in words:
		if word not in stopwords_set and len(word) > 2:
			try:
				if word[-1] == 's':
					filtered.append(word[0:-1]) 
				else:
					filtered.append(word)
			except IndexError:
				continue
	return filtered



def filter_text(text):
	filtered = _slugify(text)
	filtered = _get_meaningful_words(filtered)
	return filtered


############# Strike-A-Match ###############

# https://gist.github.com/scotta/1063364/8b8970bb617c2f8689fedc50721e7bcc60767df8
#
# """Implementation of the "Strike a match" algorithm presented in the article  
# http://www.catalysoft.com/articles/StrikeAMatch.html by Simon White.
# 
# Excerpt from the above URL: The similarity between two strings s1 and s2 is
# twice the number of character pairs that are common to both strings divided by
# the sum of the number of character pairs in the two strings. Note that the
# formula rates completely dissimilar strings with a similarity value of 0, since
# the size of the letter-pair intersection in the numerator of the fraction will
# be zero. On the other hand, if you compare a (non-empty) string to itself, then
# the similarity is 1.
 

def _get_character_pairs(text):
    """Returns a dicttionary of adjacent character pair counts."""

    if not hasattr(text, "upper"):
        raise ValueError("Invalid argument")

    results = collections.defaultdict(int)  # default value of 0

    for word in text.upper().split():
        for pair in [word[i]+word[i+1] for i in range(len(word)-1)]:
            results[pair] += 1
    return results

def compare_strings(string1, string2):
    """Returns a value between 0.0 and 1.0 indicating the similarity between the
    two strings. A value of 1.0 is a perfect match and 0.0 is no similarity.
 
    >>> for w in ('Sealed', 'Healthy', 'Heard', 'Herded', 'Help', 'Sold'):
    ...     compare_strings('Healed', w)
	"""

    s1_pairs = _get_character_pairs(string1)
    s2_pairs = _get_character_pairs(string2)

    s1_size = sum(s1_pairs.values())
    s2_size = sum(s2_pairs.values())

    intersection_count = 0

    # determine the smallest dict to optimise the calculation of the
    # intersection.
    if s1_size < s2_size:
        smaller_dict = s1_pairs
        larger_dict = s2_pairs
    else:
        smaller_dict = s2_pairs
        larger_dict = s1_pairs

    # determine the intersection by counting the subtractions we make from both
    # dicts.
    for pair, smaller_pair_count in smaller_dict.items():
        if pair in larger_dict and larger_dict[pair] > 0:
            if smaller_pair_count < larger_dict[pair]:
                intersection_count += smaller_pair_count
            else:
                intersection_count += larger_dict[pair]

    return (2.0 * intersection_count) / (s1_size + s2_size)
