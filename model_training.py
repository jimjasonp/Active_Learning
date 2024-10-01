#from data_processing import sensor_median_high
from y_set_creator import damage_data_df
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.dummy import DummyClassifier

# to programma trabaei ta dedomena me duo tropous
# o prwtos tropos einai na trabaei to feature apo to data processing
# o deuteros einai apo to csv pou kanei save to main


sensor_max = pd.read_csv(r'C:\Users\jimja\Desktop\thesis\results\sensor_max.csv')
sensor_median_high = pd.read_csv(r'C:\Users\jimja\Desktop\thesis\results\sensor_median_high.csv')
sensor_mean = pd.read_csv(r'C:\Users\jimja\Desktop\thesis\results\sensor_mean.csv')
sensor_stdev = pd.read_csv(r'C:\Users\jimja\Desktop\thesis\results\sensor_stdev.csv')


def feature_for_training(feature):
    feature = feature[[
        's2',
        's3'
        ,'s4'
        ]]
    X = feature.iloc[:,:]
    return X

X = feature_for_training(sensor_stdev)

y = damage_data_df.iloc[:,:]

# Split the data into training and test sets

#prwta epilegw to pososto twn dedomenwn pou tha xrhsimopoihsw gia to train kai test tou montelou
## an thelo na xrhsimopoihsw to 100 % tote to prwto train test split sbhnetai
## sunolika exw 150 samples



#X, X_drop, y, y_drop = train_test_split(X, y, test_size=0.8,shuffle=True)


## ta X kai y einai auta pou tha xrhsimopoisw
## ta X_drop kai y_drop einai auta pou den xrhsimopoiw

#sto deutero split xrhsimopoiw ta dedomena training apo thn prohgoumenh ektelesh ths train test split
#kai ta xrhsimopoiw gia na ftiaksw ta dedomena train kai test

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,shuffle=True)


# Scale the features using StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


#knn = KNeighborsClassifier(n_neighbors=5)
#knn.fit(X_train, y_train)
#y_pred = knn.predict(X_test)

#svm = SVC()
#svm.fit(X_train, y_train)
#y_pred = svm.predict(X_test)

DT = DecisionTreeClassifier()
DT.fit(X_train, y_train)
y_pred = DT.predict(X_test)

#dummy = DummyClassifier(strategy='uniform')
#dummy.fit(X_train, y_train)
#y_pred = dummy.predict(X_test)

CM = confusion_matrix(y_test,y_pred)
print(CM)

accuracy = accuracy_score(y_test, y_pred)
print('===============')
print("Accuracy:", accuracy)


