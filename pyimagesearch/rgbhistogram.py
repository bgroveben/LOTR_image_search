# Define image descriptor
# Create a 3D RGB histogram using OpenCV
# Import the necessary packages
import numpy as np
import cv2

# Define image descriptor as a class instead of a function
class RGBHistogram
	# Define a constuctor for the RGBHistogram
	def __init__(self, bins):
		# Store the number of bins the histogram will use
		self.bins = bins
	# "Describe" the image and return a feature vector
	def describe(self, image):
		# Compute a 3D histogram in the RGB colorspace
		# Normalize the images so that images with the same content,
		# but either scaled larger or smaller with have roughly the same histogram
		hist = cv2.calcHist([image], [0, 1, 2],
			None, self.bins, [0, 256, 0, 256, 0, 256])
		hist = cv2.normalize(hist)
		# When computing a 3D histogram, the histogram will be represented as a 
		# Numpy array with (N, N, N) bins. In ordr to more easily compute the distance
		# between the histograms, flatten the histogram to have a shape of ( N ** 3, )
		# Return out 3D histogram as a flattened array
		return hist.flatten()