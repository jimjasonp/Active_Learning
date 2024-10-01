from x_set_creator import sensor_data_list
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics

##----------------- feature selection
feature_list = ['max','mean','stdev','median_high']

sensor_max = pd.DataFrame()
sensor_mean = pd.DataFrame()
sensor_stdev = pd.DataFrame()
sensor_median_high = pd.DataFrame()
##----------------------feature selection


#gia kathe feature kataskeuazo ena dataframe pou tha mpoun gia kathe sensora oi times tou feature gia kathe timeserie tou sensora

for feature in feature_list:
    sensor_fft_df = pd.DataFrame()
    sensor_fft = []
    sensor_names = ['s2','s3','s4']

    for sensor in sensor_names:
        sensor_fft = []
        #gia kathe sample sensora dld gia kathe xronoseira efarmozo fft
        for i in range(0,len(sensor_data_list)):
            sample_sensor =sensor_data_list[i][sensor]



##-----------------fourier
            fs = 1/1000

            fourier = np.fft.fft(sample_sensor)
            #sample sensor is the value of s2 which is the 
            freqs = np.fft.fftfreq(sample_sensor.size,d=fs)
            unfiltered_power_spectrum = np.abs(fourier)

            #### new addition 25/09
            ### filtrarei ta apotelesmata tou fft kai krataei mono tis times pou einai pio megales
            power_spectrum = []
            for element in unfiltered_power_spectrum: 
                if element>2*10e-4:
                    power_spectrum.append(element)
##-----------------fourier



            # ta apotelesmata tou fft ta metatrepw se kapoio feature
            
##-----------------feature selection
            if feature == 'max':
                sensor_fft.append(max(power_spectrum))
            elif feature =='mean':
                sensor_fft.append(statistics.mean(power_spectrum))
            elif feature =='stdev':
                sensor_fft.append(statistics.stdev(power_spectrum))
            elif feature =='median_high':
                sensor_fft.append(statistics.median_high(power_spectrum))

##-----------------feature selection
        # tis times tou kathe feature tis pernaw se ena df 
        new_data = {sensor: sensor_fft}
        sensor_fft_df = sensor_fft_df.assign(**new_data)
##-----------------feature selection
    if feature == 'max':
        sensor_max = sensor_max.assign(**sensor_fft_df)
    elif feature =='mean':
        sensor_mean = sensor_mean.assign(**sensor_fft_df)
    elif feature =='stdev':
        sensor_stdev = sensor_stdev.assign(**sensor_fft_df)
    elif feature =='median_high':
        sensor_median_high = sensor_median_high.assign(**sensor_fft_df)
##-----------------feature selection
