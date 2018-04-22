from sklearn import svm
class SVM:
    def __init__(self):
        self.clf = None      
    
    '''
        @args:
            feature_vector - a list of the attributes with the class/label 
                             being the last attribute
        @return:
            Learns a linear SVM model between given data points
    '''
    def train(self, feature_vector):
        X = []
        y = []
        self.clf = svm.SVC(C = 0.25, probability = True)
        for i in range(len(feature_vector)):
            X.append(feature_vector[i][:len(feature_vector[i])-1])
            y.append(feature_vector[i][len(feature_vector[i])-1])
        self.clf.fit(X, y)   
        
    
    def test(self,feature_vector):
        '''
        @args:
            feature_vector - a list of the attributes whose 
                                class/label is to be predicted
        @return:
            predicted class/label according to learned svm model
        '''          
        return [self.clf.predict(feature_vector)[0], max(max(self.clf.predict_proba(feature_vector)))]

#example on how to run/call the program
#svmObj = SVM()
#feature_vector = [[1,1,1], [0,0,0]]
#svmObj.train(feature_vector)
#test_vector = [[1, 1]]
#print(svmObj.test(test_vector))
