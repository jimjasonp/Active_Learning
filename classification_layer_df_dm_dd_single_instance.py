from y_set_df_dm_dd import layer_damage
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.linear_model import LogisticRegression
import pandas as pd
from x_set_creator import sensor_mean



X = sensor_mean
y = layer_damage['total_damage_per_layer']


for sample in y:
    if not sample =='df&dm&dd':
        print('found')
    else:
        print('not')



counter =0 
for i in y:
    if not i =='df&dm&dd':
        counter +=1

j =6 

while j>5:
    train_counter =0
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,shuffle=True)
    for i in y_train:
        if i =='df&dm&dd':
            train_counter +=1
    if train_counter >0.5*counter:
        j=0

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)





