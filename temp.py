import cv2
import GenerateFeatureVector as gfv
from numpy import genfromtxt
from knn import KNearestNeighbors
from trainSVM import SVM

knn_obj = KNearestNeighbors()
svm_obj = SVM()

cell_length = 10
cell_width = 10
training = False
bins = 8
#for testing purposes
image = cv2.imread('Images/Testing/000102.png', -1);
test_vector = gfv.FeatureVectorGenerator.generate_feature_vector(image, cell_width, cell_length, training, bins, False)
print(test_vector)
