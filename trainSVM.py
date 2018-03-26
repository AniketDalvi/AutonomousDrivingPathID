from sklearn import svm
X = []
feature = #Do file parsing here pipelining one feature vector at a time from the CSV 
X.append(feature) 
y = [-1, 1] #-1 implies not a road and 1 implies that it is a road
clf = svm.SVC() 
clf.fit(X, y)  
clf.predict('input feature vector here')