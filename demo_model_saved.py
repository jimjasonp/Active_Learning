#from y_set_creator import damage_data_df
from y_set_creator import y_set_creator
from training_params import feature_for_training,sensor_median_high,sensor_max,sensor_mean,sensor_stdev
from training_params import model_choice
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,mean_absolute_error,root_mean_squared_error,mean_absolute_percentage_error


# to programma trabaei ta dedomena me duo tropous
# o prwtos tropos einai na trabaei to feature apo to data processing
# o deuteros einai apo to csv pou kanei save to main



# -------------------user input-------------------
#############################################
mode = 'regression'  #classification / regression
sensor_list = ['s2','s3','s4']      #s2,s3,s4
feature = sensor_max   #sensor_median_high,sensor_max,sensor_mean,sensor_stdev
damage_index = 'Damage_percentage' # ['Damage_percentage', 'DamageLayer1', 'DamageLayer2', 'DamageLayer3', 'DamageLayer4', 'DamageLayer5']
model = 'RF'                   #knn,svm,DT,dummy,   xgb,linear_regression,RF
data_percentage = 0.66 # 0-> no data .... 1 -> full dataset (150 samples)
#odhgies gia user:
#------gia na kanw tune to montelo pou thelo peirazw to arxeio training params
#----- an thelo na allaksw ton arithmo twn samples phgainw stis train test split
#------an thelo na treksw arxeio apo data_processing tote energopoiw tis duo parakatw grammes kai tis ftiaxnw opws thelw kai sbhnw to X apo pio katw
#from data_processing import sensor_median_high,sensor_max,sensor_stdev,sensor_mean
#X = sensor_mean.iloc[:,:]
X = feature_for_training(feature,sensor_list)
#############################################






####     test      ####


#y = y_set_creator(damage_index,mode)
#y = y.iloc[:,:]


from y_set_for_layer import DL1,DL2,DL3,DL4,DL5
y = DL1['df']

#########################




# Split the data into training and test sets

#prwta epilegw to pososto twn dedomenwn pou tha xrhsimopoihsw gia to train kai test tou montelou


if data_percentage == 1:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,shuffle=True)
else:
    X, X_drop, y, y_drop = train_test_split(X, y, test_size=1-data_percentage,shuffle=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,shuffle=True)


# Scale the features using StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
y_pred = model_choice(model,X_train,y_train,X_test)

if mode == 'classification':

    CM = confusion_matrix(y_test,y_pred)
    print(CM)

    accuracy = accuracy_score(y_test, y_pred)
    print('===============')
    print("Accuracy:", accuracy)

if mode == 'regression':
    mae = mean_absolute_error(y_test,y_pred)
    rmse = root_mean_squared_error(y_test,y_pred)
    print('mae is ')
    print(mae)
    print('=================')
    print('rmse is')
    print(rmse)


