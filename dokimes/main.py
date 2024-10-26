from x_set_creator import sensor_data_list
import numpy as np
import pandas as pd


feature_list = ['max','mean','stdev','median_high']
sensor_names = ['s2','s3','s4']

#gia kathe feature kataskeuazo ena dataframe pou tha mpoun gia kathe sensora oi times tou feature gia kathe timeserie tou sensora

for feature in feature_list:

    for sensor in sensor_names:
        sensor_fft = []
        #gia kathe sample sensora dld gia kathe xronoseira efarmozo fft
        for i in range(0,len(sensor_data_list)):
            sample_sensor =sensor_data_list[i][sensor]

            from fourier import fourier
            fourier(sample_sensor)
            from feature_selection import feature_maker
            from fourier import power_spectrum
            feature_maker(feature,sensor_fft,power_spectrum)


 
        from feature_selection import df_creator
        df_creator(sensor)
        from feature_selection import sensor_fft_df

    from feature_selection import feature_df_assign
    feature_df_assign(feature,sensor_fft_df)
