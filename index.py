# USAGE
# python index.py --dataset images --index index.cpickle

# Apply image descriptor (rgbhistogram.py) to ech image in the dataset
# Loop over each image in the dataset, extract a 3D RGB histogram from each image,
# store the features in a dictionary, and write the dictionary to a file

# Import the necessary packages
from pyimagesearch.rgbhistogram import rgbhistogram
import argparse
import cPickle
import glob
import cv2

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the dictionary that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
args = vars(ap.parse_args())

# Initialize the index dictionary to store oour quantified images,
# with the 'key' of the dictionary being the image filename and the 
# 'value' being our computed features
index = {}

# Initialize our image descriptor: a 3D RGB histogram with 8 bins per channel
desc = RGBHistogram([8,8,8])

# Use glob to to grab the image paths and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.png"):
	# Extract the unique image ID (i.e the filename)
	k = imagePath[imagePath.rfind("/") + 1:]
	# Load the image, describe it using the RGB histogram descriptor, and update the index
	image = cv2.imread(imagePath)
	features = desc.describe(image)
	index[k] = features

# Now write the index to the disk
f = open(args["index"], "w")
f.write(cPickle.dumps(index))
f.close()

# show how many images we indexed
print "done...indexed %d images" % (len(index))
