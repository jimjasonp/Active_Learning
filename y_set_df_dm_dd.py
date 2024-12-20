import pandas as pd
import math
from y_set_creator_dmg_percentage import dmg_data
DL1 = pd.DataFrame()
DL2 = pd.DataFrame()
DL3 = pd.DataFrame()
DL4 = pd.DataFrame()
DL5 = pd.DataFrame()
layer_damage = pd.DataFrame()

odd_layer =['DamageLayer1', 'DamageLayer3', 'DamageLayer5'] ###['DamageLayer1', 'DamageLayer2', 'DamageLayer3', 'DamageLayer4', 'DamageLayer5']

for layer in odd_layer:
    dtotal_list = []
    i = 0
    for path in dmg_data['damage_file_name']:
        path = path + '.csv'
        dataframe = pd.read_csv(path,sep=' |,', engine='python')
        DL = dataframe[layer]
        df = 1 - (1-DL[0])*(1-DL[1])
        dm = 1 - (1-DL[2])*(1-DL[3])

        if df==0 and dm ==0:
            dtotal_list.append('clean')
            i = i+1
        elif df==0:
            dtotal_list.append('dm')
        elif dm ==0:
            dtotal_list.append('df')
        else:
            dtotal_list.append('df&dm')

    if layer == 'DamageLayer1':
        DL1 = pd.DataFrame({'Layer_1': dtotal_list})
    if layer == 'DamageLayer3':
        DL3 = pd.DataFrame({'Layer_3': dtotal_list})
    if layer == 'DamageLayer5':
        DL5 = pd.DataFrame({'Layer_5': dtotal_list})
even_layer = [ 'DamageLayer2',  'DamageLayer4']

for layer in even_layer:
    dd_list = []
    for path in dmg_data['damage_file_name']:
        path = path + '.csv'
        dataframe = pd.read_csv(path,sep=' |,', engine='python')
        DL = dataframe[layer]
        dd = 1 - DL[0]
        dd = math.floor(dd*10)/10

        if dd ==0:
            dd_list.append('clean')
        else :
            dd_list.append('dd')

    if layer == 'DamageLayer2':
        DL2 = pd.DataFrame({'Layer_2': dd_list})
    if layer == 'DamageLayer4':
        DL4 = pd.DataFrame({'Layer_4': dd_list})


layer_damage = layer_damage.assign(**DL1,**DL2,**DL3,**DL4,**DL5)


dm_df_dd_list = []
for i in range(0,len(layer_damage)):
    if layer_damage['Layer_1'][i] == 'df' and layer_damage['Layer_3'][i] == 'df' and layer_damage['Layer_5'][i] == 'df':
        if layer_damage['Layer_2'][i] == 'dd' or layer_damage['Layer_4'][i] == 'dd':
            dm_df_dd_list.append('df&dd')
        else :
            dm_df_dd_list.append('df')
    elif layer_damage['Layer_1'][i] == 'dm' and layer_damage['Layer_3'][i] == 'dm' and layer_damage['Layer_5'][i] == 'dm':
        if layer_damage['Layer_2'][i] == 'dd' or layer_damage['Layer_4'][i] == 'dd':
            dm_df_dd_list.append('dm&dd')
        else :
            dm_df_dd_list.append('dm')
    elif layer_damage['Layer_1'][i] == 'clean' and layer_damage['Layer_3'][i] == 'clean' and layer_damage['Layer_5'][i] == 'clean':
        if layer_damage['Layer_2'][i] == 'dd' or layer_damage['Layer_4'][i] == 'dd':
            dm_df_dd_list.append('dd')
        else :
            dm_df_dd_list.append('clean')
    else:
        if layer_damage['Layer_2'][i] == 'dd' or layer_damage['Layer_4'][i] == 'dd':
            dm_df_dd_list.append('df&dm&dd')
        else :
            dm_df_dd_list.append('df&dm')

layer_damage['total_damage_per_layer'] = dm_df_dd_list
