import pandas as pd
import glob
import os

path = r'C:\Users\jimja\Desktop\diploma_kodikes\data' # use your path
data_list = []
name_list = []
for filename in sorted(glob.glob(os.path.join(path , "data*"))):
    df = pd.read_csv(filename,sep=' |,', engine='python').dropna()
    data_list.append(df)
    name_list.append(filename)



sensor_data = pd.DataFrame({'data':data_list,'name':name_list})
