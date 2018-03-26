# loading libraries
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.metrics import accuracy_score

#-------------------------Used for Testing------------------------------------
#names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
#instantiatete design matrix X and target vector y
#X = np.array(tr_data.ix[:, 0:4])       # end index is exclusive
#y = np.array(tr_data['class'])         # showing you two ways of indexing a pandas df
# split into train and test
#X_tr, X_test, Y_tr, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
#acc = accuracy_score(y_test, pred) * 100
#print('\nThe accuracy of the knn classifier for k = 3 is %d%%' % acc)
#------------------------Used for Testing----------------------------------------

# loading training data
tr_data = pd.read_csv('<insert path of csv>', header=None, names=names)
tr_data.head()

# create design matrix X and target vector y
X_tr = np.array(tr_data.ix[:, 0:24])    # end index is exclusive
Y_tr = np.array(tr_data.ix[:,24])       # class is in column 25
X_test = <test image>

# instantiate learning model (k = 3)
knn = KNeighborsClassifier(n_neighbors=3)

# fitting the model
knn.fit(X_tr, Y_tr)

# predict the response
pred = knn.predict(X_test)
