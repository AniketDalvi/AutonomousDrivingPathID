import cv2
import GenerateFeatureVector as gfv

cell_length = 10
cell_width = 10
training = True
bins = 8

#for testing purposes
image = cv2.imread('Images/mountain_center.png', -1);
gfv.FeatureVectorGenerator.generate_feature_vector(image, cell_width, cell_length, training, bins)