import pandas as pd
import glob
import os
import numpy as np
from y_set_creator import dmg_index_list
path = r'C:\Users\jimja\Desktop\thesis\data' # use your path
# to sensor data list einai auto pou einai sth morfh gia train
sensor_data_list = []
name_list = []


### h lista tou damage percnetage kai twn dedomenwn apo sensores den exoun idio megethos giati leipoun kapoia data apo damage
### gia auto to logo oi arithmoi instance pou den uparxoun kai stis duo listes tha fugoun



# gia kathe filename sto path pou tou exw dwsei afairei to .csv wste meta na mporei na diabasei ton arithmo
for filename in sorted(glob.glob(os.path.join(path , "data*"))):
    filename = filename.removesuffix('.csv')
    name_list.append(filename)


#apo kathe filename krataei mono ton arithmo sto telos kai me auton ton arithmo ftiaxeni th nea sthlh index number
sensor_data = pd.DataFrame({'name':name_list})
sensor_data['sensor_index_number'] = [int(i.split('_')[-1]) for i in sensor_data['name']]


#kanw sort th lista basei tou index number
sensor_data = sensor_data.sort_values(by=['sensor_index_number'])



############
############
############
############
############


#### auta apo edw kai katw mpainoun mono otan exoun afairethei oi periptwseis pou den uparxoun sto damage




##########

suffix='.csv'
new_names=[]


#se kathe filename sth lista pou exei ginei sort prosthetei to .csv wste na mporei na to diabasei
for filename in sensor_data['name']:
    filename = filename+suffix
    new_names.append(filename)



#anoigei ta arxeia apo kathe path kai ftiaxnei th lista me tis metrhseis

for filename in new_names:
    df = pd.read_csv(filename,sep=' |,', engine='python').dropna()
    sensor_data_list.append(df)



