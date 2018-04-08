import cv2
import GenerateFeatureVector as gfv
from numpy import genfromtxt

cell_length = 10
cell_width = 10
training = True
bins = 8
image = cv2.imread('1.png', -1)
#for testing purposes
#image = cv2.imread('Images/mountain_center.png', -1);
#gfv.FeatureVectorGenerator.generate_feature_vector(image, cell_width, cell_length, training, bins)
counter = 0
my_data = genfromtxt('Nothing.csv', delimiter=',')
rows, columns, channels = image.shape
for x in range(0, rows - cell_width, cell_width):
    for y in range(0, columns - cell_length, cell_length):
        vector = my_data[counter]
        if vector[24] == 1:           
            image[x:x+cell_width, y:y+cell_length, 0] = 0
            image[x:x+cell_width, y:y+cell_length, 1] = 0
            image[x:x+cell_width, y:y+cell_length, 2] = 100
        if vector[24] == -1:
            image[x:x+cell_width, y:y+cell_length, 0] = 0
            image[x:x+cell_width, y:y+cell_length, 1] = 100
            image[x:x+cell_width, y:y+cell_length, 2] = 0
        counter += 1
        
print(counter)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()