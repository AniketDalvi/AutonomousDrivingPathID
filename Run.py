import cv2
import GenerateFeatureVector as gfv
from numpy import genfromtxt
from knn import KNearestNeighbors
from trainSVM import SVM
import glob
import sys

#knn_obj = KNearestNeighbors()
svm_obj = SVM()

cell_length = 10
cell_width = 10
training = False
bins = 8

destination = 'Result/result'
i = 450
print(i)
for filename in sorted(glob.glob('Images/Testing/*.png')):
	print(i)
	sys.stdout.flush()
	image = cv2.imread(filename, -1)
	gfv.FeatureVectorGenerator.generate_feature_vector(image, cell_width, cell_length, training, bins, True)
    

	test_vector = genfromtxt('new-testdata.csv', delimiter=',')

	test_vector = test_vector[:, 0:26]

	counter = 0
	my_data = genfromtxt('new-traindata.csv', delimiter=',')
#	print(my_data)
	svm_obj.train(my_data)

#	labels = my_data[:, 26]
#	my_data = my_data[:, 0:26]
	rows, columns, channels = image.shape
	#print(rows)
	#print(columns)
#	knn_obj.train(my_data, labels, 20)

	for x in range(0, rows - cell_width, cell_width):
	    for y in range(0, columns - cell_length, cell_length):
	        test = [test_vector[counter]]
#	        label = knn_obj.predict(test)
	        label = svm_obj.test(test)
	#        print(label)
	        if label == 1:           
	            image[x:x+cell_width, y:y+cell_length, 0] = 00
	            image[x:x+cell_width, y:y+cell_length, 1] = 00
	            image[x:x+cell_width, y:y+cell_length, 2] = 100
	        
	        counter += 1
	        
	#cv2.imshow('image', image)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
	url = destination + str(i) + '.png'
	i = i+1
	cv2.imwrite(url, image)
