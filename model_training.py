from data_processing import sensor_max
from y_set_creator import damage_data_df

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


# Split the data into features (X) and target (y)
X = sensor_max.iloc[:,:]
y = damage_data_df.iloc[:,:]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

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

CM = confusion_matrix(y_test,y_pred)
print(CM)

accuracy = accuracy_score(y_test, y_pred)
print('===============')
print("Accuracy:", accuracy)