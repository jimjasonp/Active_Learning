
import matplotlib.pyplot as plt
from y_set_creator import y_set_creator
from training_params import feature_for_training,sensor_median_high,sensor_max,sensor_mean,sensor_stdev
from training_params import model_choice
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,root_mean_squared_error


mode = 'regression'  #classification / regression
sensor_list = ['s2','s3','s4']      #s2,s3,s4
feature = sensor_mean   #sensor_median_high,sensor_max,sensor_mean,sensor_stdev
damage_index = 'Damage_percentage' # ['Damage_percentage', 'DamageLayer1', 'DamageLayer2', 'DamageLayer3', 'DamageLayer4', 'DamageLayer5']

X = feature_for_training(feature,sensor_list)
y = y_set_creator(damage_index,mode)
y = y.iloc[:,:]


data_percentage = 0.33  # 0 ---> 1

if data_percentage == 1:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,shuffle=True)
else:
    X, X_drop, y, y_drop = train_test_split(X, y, test_size=1-data_percentage,shuffle=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,shuffle=True)

samples = len(X_train)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model_list = ['linear_regression','RF','xgb']

def reg_models(model):

    y_pred = model_choice(model,X_train,y_train,X_test)
    mae = mean_absolute_error(y_test,y_pred)
    return mae


def bar_charts_mae():

    mae_lr = reg_models('linear_regression')
    mae_rf = reg_models('RF')
    mae_xgb = reg_models('xgb')

    # creating the dataset
    data = {'Linear Regression':mae_lr, 
            'Random Forest':mae_rf,
            'XGB':mae_xgb}

    model_names  = list(data.keys())
    mae = list(data.values())
 
    fig = plt.figure(figsize = (10, 5))

    # creating the bar plot
    plt.bar(model_names, mae, color ='maroon', 
            width = 0.4)

    plt.xlabel("Models")
    plt.ylabel("Mean absolute error")
    plt.title(f"Mean absolute error of models with number of samples used = {samples}")
    plt.show()



def scatter_x_y (model):
    y_pred = model_choice(model,X_train,y_train,X_test)
    plt.plot(range(len(y_test)),y_test)
    plt.plot(range(len(y_test)),y_pred)
    plt.xlabel("sample")
    plt.ylabel("y value")
    plt.title(f"Comparison of predicted and y test for each datapoint using {model}")
    plt.legend(["y_test", "y_pred"], loc="lower right")
    plt.show()

for model in model_list:
    scatter_x_y(model)

    
bar_charts_mae()