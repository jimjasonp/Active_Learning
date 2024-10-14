import os
import glob
import pandas as pd
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



#sample = dmg_data['damage_file_name'][0] + '.csv'


###### apo edw kai panw einai idio me y_set_creator






DL1 = pd.DataFrame()
DL2 = pd.DataFrame()
DL3 = pd.DataFrame()
DL4 = pd.DataFrame()
DL5 = pd.DataFrame()


mode = 'classification'  #'classification','regression'

odd_layer =['DamageLayer1', 'DamageLayer3', 'DamageLayer5'] ###['DamageLayer1', 'DamageLayer2', 'DamageLayer3', 'DamageLayer4', 'DamageLayer5']

for layer in odd_layer:
    df_list = []
    dm_list = []
    for path in dmg_data['damage_file_name']:
        path = path + '.csv'
        dataframe = pd.read_csv(path,sep=' |,', engine='python')
        DL = dataframe[layer]
        df = 1 - (1-DL[0])*(1-DL[1])
        dm = 1 - (1-DL[2])*(1-DL[3])
        if mode == 'classification':
            df_list.append(str(df))
            dm_list.append(str(dm))
        if mode == 'regression':
            df_list.append(df)
            dm_list.append(dm)
    if layer == 'DamageLayer1':
        DL1 = pd.DataFrame({'df': df_list,'dm':dm_list})
    if layer == 'DamageLayer3':
        DL3 = pd.DataFrame({'df': df_list,'dm':dm_list})
    if layer == 'DamageLayer5':
        DL5 = pd.DataFrame({'df': df_list,'dm':dm_list})


even_layer = [ 'DamageLayer2',  'DamageLayer4']

for layer in even_layer:
    dd_list = []
    for path in dmg_data['damage_file_name']:
        path = path + '.csv'
        dataframe = pd.read_csv(path,sep=' |,', engine='python')
        DL = dataframe[layer]
        dd = DL[0]
        if mode == 'classification':
            dd_list.append(str(dd))
        if mode == 'regression':
            dd_list.append(dd)
    if layer == 'DamageLayer2':
        DL2 = pd.DataFrame({'dd': dd_list})
    if layer == 'DamageLayer4':
        DL4 = pd.DataFrame({'dd': dd_list})
import os
import glob
import pandas as pd
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



#sample = dmg_data['damage_file_name'][0] + '.csv'


###### apo edw kai panw einai idio me y_set_creator






DL1 = pd.DataFrame()
DL2 = pd.DataFrame()
DL3 = pd.DataFrame()
DL4 = pd.DataFrame()
DL5 = pd.DataFrame()


mode = 'regression'  #'classification','regression'

odd_layer =['DamageLayer1', 'DamageLayer3', 'DamageLayer5'] ###['DamageLayer1', 'DamageLayer2', 'DamageLayer3', 'DamageLayer4', 'DamageLayer5']

for layer in odd_layer:
    df_list = []
    dm_list = []
    for path in dmg_data['damage_file_name']:
        path = path + '.csv'
        dataframe = pd.read_csv(path,sep=' |,', engine='python')
        DL = dataframe[layer]
        df = 1 - (1-DL[0])*(1-DL[1])
        dm = 1 - (1-DL[2])*(1-DL[3])
        if mode == 'classification':
            df_list.append(str(df))
            dm_list.append(str(dm))
        if mode == 'regression':
            df_list.append(df)
            dm_list.append(dm)
    if layer == 'DamageLayer1':
        DL1 = pd.DataFrame({'df': df_list,'dm':dm_list})
    if layer == 'DamageLayer3':
        DL3 = pd.DataFrame({'df': df_list,'dm':dm_list})
    if layer == 'DamageLayer5':
        DL5 = pd.DataFrame({'df': df_list,'dm':dm_list})


even_layer = [ 'DamageLayer2',  'DamageLayer4']

for layer in even_layer:
    dd_list = []
    for path in dmg_data['damage_file_name']:
        path = path + '.csv'
        dataframe = pd.read_csv(path,sep=' |,', engine='python')
        DL = dataframe[layer]
        dd = DL[0]
        if mode == 'classification':
            dd_list.append(str(dd))
        if mode == 'regression':
            dd_list.append(dd)
    if layer == 'DamageLayer2':
        DL2 = pd.DataFrame({'dd': dd_list})
    if layer == 'DamageLayer4':
        DL4 = pd.DataFrame({'dd': dd_list})
