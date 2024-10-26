import pandas as pd
import glob
import os

path = r'C:\Users\jimja\Desktop\thesis\data' # use your path
dmg_list = []
name_list = []

# gia kathe file name sto path pou exw dwsei afairei to .csv kai afairei nan values kai kanei mia lista mono me to damage percentage
for filename in sorted(glob.glob(os.path.join(path , "meta*"))):
    df = pd.read_csv(filename,sep=' |,', engine='python').dropna()
    dmg_perc = df['Damage_percentage']
    if len(dmg_perc)== 1:
        dmg_perc = dmg_perc[0]
    dmg_list.append(dmg_perc)
    filename = filename.removesuffix('.csv')
    name_list.append(filename)





# ftiaxnei ena dataframe me to damage percentage kai prosthetei to index number kai kanei sort basei autou 
dmg_data = pd.DataFrame({'dmg':dmg_list,'damage_file_name':name_list})
dmg_data['dmg_index_number'] = [int(i.split('_')[-1]) for i in dmg_data['damage_file_name']]
dmg_data = dmg_data.sort_values(by=['dmg_index_number'])

#krataw ksexwrista ta index numbers wste na to perasw sto sensors gia na dw poia indeces den uparxoun
dmg_index_list = dmg_data['dmg_index_number']

dmg_data = dmg_data.drop(['damage_file_name'],axis=1)
damage_instances = dmg_data['dmg']
new_dmg = []

# meta ftiaxnei mia nea lista me to damage percentage sth sosth seira
for dmg in damage_instances:
    new_dmg.append(dmg)

new_damage_data = pd.DataFrame({'damage_perc':new_dmg,'damage_index_number':dmg_data['dmg_index_number']})




# to damage data df einai to damage sth morfh gia train epeidh kanw classification thelo na exw labels gia auto kanw to damage percentage string
damage_data_list=[]
for dmg in damage_instances:
    damage_data_list.append(str(dmg))
damage_data_df = pd.DataFrame({'damage_percentage':damage_data_list})