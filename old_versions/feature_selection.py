import pandas as pd
import statistics

feature_list = ['max','mean','stdev','median_high']

#### auto to function to bazw mesa sto main

def feature_maker(feature,sensor_fft,power_spectrum):
    if feature == 'max':
        sensor_fft.append(max(power_spectrum))
    elif feature =='mean':
        sensor_fft.append(statistics.mean(power_spectrum))
    elif feature =='stdev':
        sensor_fft.append(statistics.stdev(power_spectrum))
    elif feature =='median_high':
        sensor_fft.append(statistics.median_high(power_spectrum))
    return sensor_fft


#auto to function den to xrhsimopoiw

def feature_df_assign(feature,sensor_fft_df,sensor_max,sensor_mean,sensor_stdev,sensor_median_high):

    if feature == 'max':
        sensor_max = sensor_max.assign(**sensor_fft_df)
        #sensor_max.to_csv(r'C:\Users\jimja\Desktop\thesis\feature_csvs\sensor_max.csv')
    elif feature =='mean':
        sensor_mean = sensor_mean.assign(**sensor_fft_df)
        #sensor_mean.to_csv(r'C:\Users\jimja\Desktop\thesis\feature_csvs\sensor_mean.csv')
    elif feature =='stdev':
        sensor_stdev = sensor_stdev.assign(**sensor_fft_df)
        #sensor_stdev.to_csv(r'C:\Users\jimja\Desktop\thesis\feature_csvs\sensor_stdev.csv')
    elif feature =='median_high':
        sensor_median_high = sensor_median_high.assign(**sensor_fft_df)
        #sensor_median_high.to_csv(r'C:\Users\jimja\Desktop\thesis\feature_csvs\sensor_median_high.csv')
