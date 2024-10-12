import pandas as pd
import glob
import os


filename = r'C:\Users\jimja\Desktop\thesis\data\metaData_case_34.csv'
dataframe = pd.read_csv(filename,sep=' |,', engine='python')

odd_layer ='DamageLayer5' ###['DamageLayer1', 'DamageLayer2', 'DamageLayer3', 'DamageLayer4', 'DamageLayer5']

def odd_layer_calc(odd_layer):
    DL = dataframe[odd_layer]

    df = 1 - (1-DL[0])*(1-DL[1])
    dm = 1 - (1-DL[2])*(1-DL[3])
    print(df)
    print(dm)

even_layer = 'DamageLayer2'
def even_layer_calc(even_layer):
    DL = dataframe[even_layer]
    dl = DL[0]
    print(dl)

odd_layer_calc(odd_layer)
even_layer_calc(even_layer)


### akoloutho paromoia diadikasia me y_set_creator kai kano drop to damage percentage 





###------------------------------------------------------------------------------
#prosthiki damage layers

#epeksergasia dedomenwn kai kataskeui functions gia ypologismo damage se kathe layer

# tune modelwn gia problepsi twn damage layer

#prosthiki keimenou gia shm me ml kai dl

#ftiaxno readme gia na eksigisw pws trexoun oi kwdikes