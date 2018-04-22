import cv2
import GenerateFeatureVector as gfv
from numpy import genfromtxt
from knn import KNearestNeighbors
from trainSVM import SVM
import glob

knn_obj = KNearestNeighbors()
svm_obj = SVM()

cell_length = 10
cell_width = 10
training = False
bins = 8

i = 0
for filename in sorted(glob.glob('Images/Testing/*.png')):
	print(i)
	i = i+1