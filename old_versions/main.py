from x_set_creator import sensor_data_list
import pandas as pd

#kalw kapoia functions pou exw ftiaksei kai leitourgoun ekswterika
from fourier_transform import fourier
from feature_selection import feature_maker

feature_list = ['max','mean','stdev','median_high']

sensor_max = pd.DataFrame()
sensor_mean = pd.DataFrame()
sensor_stdev = pd.DataFrame()
sensor_median_high = pd.DataFrame()


#gia kathe feature kataskeuazo ena dataframe pou tha mpoun gia kathe sensora oi times tou feature gia kathe timeserie tou sensora

for feature in feature_list:
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
            sensor_fft = feature_maker(feature,sensor_fft,power_spectrum)
        # tis times tou kathe feature tis pernaw se ena df 
        new_data = {sensor: sensor_fft}
        sensor_fft_df = sensor_fft_df.assign(**new_data)    
    #kataskeuazw ena dataframe gia to kathe feature me to antistoixo onoma
    if feature == 'max':
        sensor_max = sensor_max.assign(**sensor_fft_df)
    elif feature =='mean':
        sensor_mean = sensor_mean.assign(**sensor_fft_df)
    elif feature =='stdev':
        sensor_stdev = sensor_stdev.assign(**sensor_fft_df)
    elif feature =='median_high':
        sensor_median_high = sensor_median_high.assign(**sensor_fft_df)