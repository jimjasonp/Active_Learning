import pandas as pd
import glob
import os

path = r'C:\Users\jimja\Desktop\diploma_kodikes\data' # use your path
dmg_list = []
name_list = []
for filename in sorted(glob.glob(os.path.join(path , "meta*"))):
    df = pd.read_csv(filename,sep=' |,', engine='python').dropna()
    dmg_perc = df['Damage_percentage']
    if len(dmg_perc)== 1:
        dmg_perc = dmg_perc[0]
    dmg_list.append(dmg_perc)
    name_list.append(filename)



dmg_data = pd.DataFrame({'dmg':dmg_list,'name':name_list})