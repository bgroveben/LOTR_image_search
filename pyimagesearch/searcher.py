# Search the index on the disk and compare feature vectors to determine how similar they are
# Import packages
import numpy as np 

# Define Searcher class and a constructor with our index as the sole parameter
class Searcher:
	def __init__(self, index):
		# Store our index of images
		self.index = index

	def search(self, queryFeatures):
		# Initialize our dictionary of results
		# The key is the image filename from the index, the value is how similar
		# the given image is to the query image
		results = {}

		# loop over the index
		for (k, features) in self.index.items():
			# Compute the chi-squared distance between the features in our index 
			# and our query features -- using the chi-squared distancee which is 
			# normally used in the computer vision field to compare histograms
			d = self.chi2_distance(features, queryFeatures)

			# Now that we have the distance betwen the two feature vectors, we can 
			# update the results dictionary -- the key is the current image ID in the 
			# index and the value is the distance we just computed, representing how
			# 'similar' the image in the index is to our query
			results[k] = d 

		# Sort our results, so that the smaller chi-squared distances (i.e the 
		# more relevant images) are at the front of the list, and then return the results
		results = sorted([(v, k) for (k, v) in results.items()])
		return results

	# Define the chi-squared distance function used to compare the two histograms
	# The difference between the large bins vs. the small bins is (generally) less important
	def chi2_distance(self, histA, histB, eps = 1e -10):
		# The epsilon dummy value (eps) avoids errors caused by dividing by zero
		# Compute the chi-squared distance
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a , b) in zip(histA, histB)])
		# Return the chi-squared distance 
		return d 
		# The larger the chi-squared distance, the less similar the images are
		