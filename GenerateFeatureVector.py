import numpy as np
import cv2
import matplotlib.pyplot as plt

class FeatureVectorGenerator():
	
	@staticmethod
	def generate_feature_vector(img, cell_size_x, cell_size_y, train, bins):

		fVectors = [];
		rows, columns, channels = img.shape
		for y in range(0, columns - cell_size_y, cell_size_y):
			for x in range(0, rows - cell_size_x, cell_size_x):
				window_class = 0
				window = img[x:x+cell_size_x, y:y+cell_size_y]
				
				if train:
					window_class = FeatureVectorGenerator.get_training_feedback(window, cell_size_y, cell_size_x)

				a, a_bin_edges = np.histogram(window[..., 0], bins, (0, 255))
				b, b_bin_edges = np.histogram(window[..., 1], bins, (0, 255))
				c, c_bin_edges = np.histogram(window[..., 2], bins, (0, 255))
				c = np.append(c, window_class)
				fVectors.append(np.concatenate((a, b, c)))
				#print(fVectors.pop())
				#print('\n')

	@staticmethod
	def get_training_feedback(img, cell_size_y, cell_size_x):
		resized = cv2.resize(img, (int(cell_size_y / .1), int(cell_size_x / .1)), interpolation = cv2.INTER_CUBIC)
		cv2.imshow('image', resized)
		k = cv2.waitKey(0)
		print(k)
		# 1 for road -1 for other
		if k == ord('y') or k == ord('Y'):
			return 1
		cv2.destroyAllWindows()	
		return -1


if __name__ == '__main__':
	image = cv2.imread('Images/mountain_center.png', -1);
	for i in range(1):
		FeatureVectorGenerator.generate_feature_vector(image, 10, 10, False, 8)