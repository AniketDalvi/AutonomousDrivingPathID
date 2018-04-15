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

image = cv2.imread('Images/Training/1.png', -1)
#gfv.FeatureVectorGenerator.generate_feature_vector(image, cell_width, cell_length, training, bins, True)


test_vector = genfromtxt('testdata.csv', delimiter=',')
test_vector = test_vector[:, 0:24]

counter = 0
my_data = genfromtxt('traindata.csv', delimiter=',')
svm_obj.train(my_data)
labels = my_data[:, 24]
my_data = my_data[:, 0:24]
rows, columns, channels = image.shape
#print(rows)
#print(columns)
knn_obj.train(my_data, labels, 20)

for x in range(0, rows - cell_width, cell_width):
    for y in range(0, columns - cell_length, cell_length):
        test = [test_vector[counter]]
        #label = knn_obj.predict(test)
        label = svm_obj.test(test)
        print(label)
        if label == 1:           
            image[x:x+cell_width, y:y+cell_length, 0] = 0
            image[x:x+cell_width, y:y+cell_length, 1] = 0
            image[x:x+cell_width, y:y+cell_length, 2] = 100
        
        counter += 1
        
print(counter)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()