#from y_set_creator import damage_data_df
from y_set_creator_dmg_percentage import y_set_creator
from x_set_creator import sensor_mean,sensor_max,sensor_median_high,sensor_stdev
from helper_functions import model_choice
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
import time
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
# to programma trabaei ta dedomena me duo tropous
# o prwtos tropos einai na trabaei to feature apo to data processing
# o deuteros einai apo to csv pou kanei save to main


# -------------------user input-------------------
#############################################
mode = 'classification'  #classification
sensor_list = ['s2','s3','s4']      #s2,s3,s4
feature = sensor_max   #sensor_median_high,sensor_max,sensor_mean,sensor_stdev
damage_index = 'Damage_percentage' # ['Damage_percentage', 'DamageLayer1', 'DamageLayer2', 'DamageLayer3', 'DamageLayer4', 'DamageLayer5']
model = 'svm'                   #knn,svm,DT,dummy, 
data_percentage = 1 # 0-> no data .... 1 -> full dataset (150 samples)
#odhgies gia user:
#------gia na kanw tune to montelo pou thelo peirazw to arxeio training params
#----- an thelo na allaksw ton arithmo twn samples phgainw stis train test split
#------an thelo na treksw arxeio apo data_processing tote energopoiw tis duo parakatw grammes kai tis ftiaxnw opws thelw kai sbhnw to X apo pio katw
#from data_processing import sensor_median_high,sensor_max,sensor_stdev,sensor_mean
#X = sensor_mean.iloc[:,:]
X = feature[sensor_list]
X = feature.iloc[:,:]
#############################################


y = y_set_creator(damage_index,mode)
y = y.iloc[:,:]



if data_percentage == 1:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,shuffle=True)
else:
    X, X_drop, y, y_drop = train_test_split(X, y, test_size=1-data_percentage,shuffle=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,shuffle=True)
# Scale the features using StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)



def class_model_results(model):
    start_model = time.time()
    y_pred = model_choice(model,X_train,y_train,X_test)
    acc = accuracy_score(y_test,y_pred)
    end_model = time.time()
    training_time = end_model-start_model
    return [acc,training_time,y_pred]

def cm_maker(model):
    y_pred = class_model_results(model)[2]
    cm = confusion_matrix(y_test,y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.show()
    
model_list = ['knn','svm','DT','dummy']

for model in model_list:
    cm_maker(model)

def bar_charts_acc_time():
    
    knn = class_model_results('knn')
    acc_knn = knn[0]
    time_knn = knn[1]*1000

    svm = class_model_results('svm')
    acc_svm = svm[0]
    time_svm = svm[1]*1000

    DT = class_model_results('DT')
    acc_DT = DT[0]
    time_DT = DT[1]*1000

    # creating the dataset
    data = {'K nearest neighbors':acc_knn, 
            'SVM':acc_svm,
            'Decision Trees':acc_DT}

    model_names  = list(data.keys())
    acc = list(data.values())
 
    fig = plt.figure(figsize = (10, 5))

    # creating the bar plot
    plt.bar(model_names, acc, color ='maroon', 
            width = 0.4)

    plt.xlabel("Models")
    plt.ylabel("Accuracy")
    plt.title(f"Accuracy of models")
    plt.show()


    #time bar plot
    
    # creating the dataset
    data = {'K nearest neighbors':time_knn, 
            'SVM':time_svm,
            'Decision Trees':time_DT}

    model_names  = list(data.keys())
    time = list(data.values())
 
    fig = plt.figure(figsize = (10, 5))

    # creating the bar plot
    plt.bar(model_names, time, color ='maroon', 
            width = 0.4)

    plt.xlabel("Models")
    plt.ylabel("Training time")
    plt.title(f"Training time of models in ms")
    plt.show()


bar_charts_acc_time()

