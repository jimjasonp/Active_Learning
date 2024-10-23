from x_set_creator import sensor_data_list
import pandas as pd
import numpy as np
#kalw kapoia functions pou exw ftiaksei kai leitourgoun ekswterika
from x_set_creator import fourier

feature_list = ['max','mean','stdev','median_high']

sensor_max = pd.DataFrame()
sensor_mean = pd.DataFrame()
sensor_stdev = pd.DataFrame()
sensor_median_high = pd.DataFrame()


#gia kathe feature kataskeuazo ena dataframe pou tha mpoun gia kathe sensora oi times tou feature gia kathe timeserie tou sensora

# h diadikasia ginetai epanalhptika gia kathe feature sto feature list
sensor_fft_df = pd.DataFrame()
sensor_names = ['s2','s3','s4']
for sensor in sensor_names:
    sensor_fft = []
    #gia kathe sample sensora dld gia kathe xronoseira (pou prokuptei apo to shma pou lambanei o sensoras efarmozo fft
    for i in range(0,len(sensor_data_list)):
        #efarmozo to metasxhmatismo fourier (fft) se kathe timeserie
        sample_sensor =sensor_data_list[i][sensor]
        power_spectrum = fourier(sample_sensor)
        # ta apotelesmata tou fft ta metatrepw se kapoio feature   
        sensor_fft.append(power_spectrum)
        # tis times tou kathe feature tis pernaw se ena df
    new_data = {sensor: sensor_fft}
    sensor_fft_df = sensor_fft_df.assign(**new_data)    

