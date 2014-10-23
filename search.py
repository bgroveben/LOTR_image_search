# USAGE
# python search.py --dataset images --index index.cpickle

# Here's some code to handle loading the images off of the disk and performing the search
# Most of this code handles displaying the results; the actual search is done in a single line (#25)
# Import packages
from pyimagesearch.searcher import searcher
import numpy as np 
import argparse
import cPickle
import cv2

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the directory that contains the images we just indexed")
ap.add_argument("-i", "--index", required = True,
	help = "Path to where we stored our index")
args = vars(ap.parse_args())

# Load the index and initialize our searcher
index = cPickle.loads(open(args["index"]).read())
searcher = Searcher(index)

# Loop over the images in the index. We will use each image as a query image 
for (query, QueryFeatures) in index.items():
	# Perform the search using the current query
	results = searcher.search(queryFeatures)

	# Load the query image and display it 
	path = args["dataset"] + "/%s" % (query)
	queryImage = cv2.imread(path)
	cv2.imshow("Query", queryImage)
	print "query: %s" % (query)

	# Initialize the two montages to display our results --
	# We have a total of 25 images in the index, but let's only
	# display the top 10 results; 5 images per montage, with
	# images that are 400 by 166 pixels
	montageA = np.zeros((166 * 5, 400, 3), dtype = "uint8")
	montageB = np.zeros((166 * 5, 400, 3), dtype = "uint8")

	# Loop over the top ten results
	for j in xrange(0, 10):
		# grab the result (we are using row-major order) and
		# load the result image 
		(score, imageName) = results[j]
		path = args["dataset"] + "/%s" % (imageName)
		result = cv2.imread(path)
		print "\t%d. %s : %.3f" % (j + 1, imageName, score)

		# Check to see if the first montage should be used
		if j < 5:
			montageA[j * 166:(j + 1) * 166, :] = result

		# Otherwise, the second montage should be used
		else:
			montageB[(j - 5) * 166:((j -5) + 1) * 166, :] = result

	# Show the results
	cv2.imshow("Results 1-5", montageA)
	cv2.imshow("Results 6-10", montageB)
	cv2.waitKey(0)
