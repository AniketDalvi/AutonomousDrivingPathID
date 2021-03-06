import numpy as np
import cv2
import csv
import matplotlib.pyplot as plt
import os
import glob
import sys

class FeatureVectorGenerator():
    
    @staticmethod
    def generate_feature_vector(img, cell_size_x, cell_size_y, train, bins, save):
        f_vectors = []
        columns, rows, channels = img.shape
        
        for y in range(0, columns - cell_size_y, cell_size_y):
            for x in range(0, rows - cell_size_x, cell_size_x):
                window_class = 0
                window = img[y:y+cell_size_y, x:x+cell_size_x]
            
                if train:
                    window_class = FeatureVectorGenerator.get_training_feedback(img, x, y, cell_size_y, cell_size_x)
                # print(window[..., 0])
                # print(window[..., 1])
                # print(window[..., 2])
                a, a_bin_edges = np.histogram(window[..., 0], bins, (0, 255))
                b, b_bin_edges = np.histogram(window[..., 1], bins, (0, 255))
                c, c_bin_edges = np.histogram(window[..., 2], bins, (0, 255))
                # if np.count_nonzero(a) == 0 and np.count_nonzero(b) == 0 and np.count_nonzero(c) == 0:
                #     print(columns)
                #     print(rows)
                #     print(y)
                #     print(x)
                #     print('\n')
                #     # print(np.concatenate((a, b, c)))
                #     # print('bad vector')
                #     print(window[..., 0])
                #     print(window[..., 1])
                #     print(window[..., 2])

                #25th element x, 26th element y, then class val
                c = np.append(c, x)
                c = np.append(c, y)
                c = np.append(c, window_class)
                #print(np.concatenate((a, b, c)))
                #sys.stdout.flush()
                
                f_vectors.append(np.concatenate((a, b, c)))

                
        if save:
            FeatureVectorGenerator.write_data(f_vectors, train)


    @staticmethod
    def get_training_feedback(img, x, y, cell_size_y, cell_size_x):
        img2 = img.copy()
        cv2.rectangle(img2, (x, y), (x+cell_size_x, y+cell_size_y), (0, 0, 255), 1)
        #resized = cv2.resize(img2, (int(cell_size_y / .1), int(cell_size_x / .1)), interpolation = cv2.INTER_CUBIC)
        cv2.imshow('image', img2)
        
        k = cv2.waitKey(0)
        # 1 for road -1 for other
        if k == ord('y') or k == ord('Y'):
            return 1
        
        cv2.destroyAllWindows()    
        return -1

    @staticmethod
    def binary_road(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('image', gray)
        #cv2.waitKey(0)
        
        cv2.normalize(gray, gray, 0, 255, cv2.NORM_MINMAX)
        #cv2.imshow('image', gray)
        #cv2.waitKey(0)
        
        _, gary = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY_INV)
        _, gray = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
        gray = np.add(gray, gary) - 255
        print(gray)
        #cv2.imshow('image2', gray)
        #cv2.waitKey(0)
        
        erode = cv2.erode(gray, np.ones((3, 3)), anchor = (2,2), iterations = 1)
        dilate = cv2.dilate(gray, np.ones((3, 3)), anchor = (2,2), iterations = 1)
        _, dilate = cv2.threshold(dilate, 1, 50, cv2.THRESH_BINARY_INV)
        path_trace = erode+dilate
        path_trace = np.int32(path_trace)
        cv2.watershed(img,path_trace)
        cv2.imshow('image', cv2.convertScaleAbs(path_trace))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def write_data(feature_vectors, train):
        name = "new-testdata.csv"
        if train:
            name = "new-traindata.csv"
        if not train:
            os.remove(name)
        with open(name,'a') as resultFile:
            wr = csv.writer(resultFile)
            wr.writerows(feature_vectors)                    

if __name__ == '__main__':
    #print('Use run.py to start')
    
#     for filename in sorted(glob.glob('Images/Testing/*.png')):
#         image = cv2.imread(filename, -1);

#         FeatureVectorGenerator.binary_road(image)
#    image = cv2.imread('Images/dump/000180.png', -1);
    FeatureVectorGenerator.generate_feature_vector(image, 10, 10, False, 8, True)







   # @staticmethod
    # def return_data(train):
    #     images = 0
    #     f_vectors = [];
    #     name = "testdata.csv"
    #     if train:
    #         name = "traindata.csv"
    #     f=open(name, "r")
    #     for line in f:
    #         if line.startswith("-"):
    #             if not len(f_vectors) == 0:
    #                 images = images + 1

    #         else:
    #             if not len(line.strip()) == 0:
    #                 array = [int(x) for x in line.split(',')]
    #                 f_vectors.append(np.asarray(array))
    #     return f_vectors
