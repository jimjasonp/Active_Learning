import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.dummy import DummyClassifier
from main import sensor_max,sensor_mean,sensor_stdev,sensor_median_high
## kanw import ta csv gia kathe feature pou thelw


#metatrepw to feature sth morfh pou thelw me ton arithmo twn sensors pou thelw se kathe periptwsh
def feature_for_training(feature,sensor_list):
    feature = feature[sensor_list]
    X = feature.iloc[:,:]
    return X

#epilegw analogws to montelo pou thelw 
def model_choice(model,X_train,y_train,X_test):
    if str(model) == 'knn':
        knn = KNeighborsClassifier(n_neighbors=5)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
    if str(model) =='svm':
        svm = SVC()
        svm.fit(X_train, y_train)
        y_pred = svm.predict(X_test)
    if str(model) =='DT':
        DT = DecisionTreeClassifier()
        DT.fit(X_train, y_train)
        y_pred = DT.predict(X_test)
    if str(model) =='dummy':
        dummy = DummyClassifier(strategy='uniform')
        dummy.fit(X_train, y_train)
        y_pred = dummy.predict(X_test)
    return y_pred