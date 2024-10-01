from y_set_creator import damage_data_df
from training_params import feature_for_training,sensor_median_high,sensor_max,sensor_mean,sensor_stdev
from training_params import model_choice
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix




# to programma trabaei ta dedomena me duo tropous
# o prwtos tropos einai na trabaei to feature apo to data processing
# o deuteros einai apo to csv pou kanei save to main



# -------------------user input-------------------
#############################################
sensor_list = ['s2','s3','s4']
feature = sensor_median_high
model = 'DT'#knn,svm,DT,dummy
#odhgies gia user:
# -----gia na kanw tune to montelo pou thelo peirazw to arxeio training params
#----- an thelo na allaksw ton arithmo twn samples phgainw stis train test split
#------an thelo na treksw arxeio apo data_processing tote energopoiw tis duo parakatw grammes kai tis ftiaxnw opws thelw kai sbhnw to X apo pio katw
#from data_processing import sensor_median_high,sensor_max,sensor_stdev,sensor_mean
#X = sensor_median_high.iloc[:,:]
X = feature_for_training(feature,sensor_list)
#############################################




y = damage_data_df.iloc[:,:]

# Split the data into training and test sets

#prwta epilegw to pososto twn dedomenwn pou tha xrhsimopoihsw gia to train kai test tou montelou
## an thelo na xrhsimopoihsw to 100 % tote to prwto train test split sbhnetai
## sunolika exw 150 samples



#X, X_drop, y, y_drop = train_test_split(X, y, test_size=0.8,shuffle=True)


## ta X kai y einai auta pou telika tha xrhsimopoisw
## ta X_drop kai y_drop einai auta pou den xrhsimopoiw

#sto deutero split xrhsimopoiw ta dedomena training apo thn prohgoumenh ektelesh ths train test split
#kai ta xrhsimopoiw gia na ftiaksw ta actual dedomena train kai test

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,shuffle=True)


# Scale the features using StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)



y_pred = model_choice(model,X_train,y_train,X_test)


CM = confusion_matrix(y_test,y_pred)
print(CM)

accuracy = accuracy_score(y_test, y_pred)
print('===============')
print("Accuracy:", accuracy)


