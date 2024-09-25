import pandas as pd
import statistics

feature_list = ['max','mean','stdev','median_high']

sensor_max = pd.DataFrame()
sensor_mean = pd.DataFrame()
sensor_stdev = pd.DataFrame()
sensor_median_high = pd.DataFrame()

def feature_maker(feature,sensor_fft,power_spectrum):
    if feature == 'max':
        sensor_fft.append(max(power_spectrum))
    elif feature =='mean':
        sensor_fft.append(statistics.mean(power_spectrum))
    elif feature =='stdev':
        sensor_fft.append(statistics.stdev(power_spectrum))
    elif feature =='median_high':
        sensor_fft.append(statistics.median_high(power_spectrum))


def feature_df_assign(feature,sensor_fft_df):
    if feature == 'max':
        sensor_max = sensor_max.assign(**sensor_fft_df)
    elif feature =='mean':
        sensor_mean = sensor_mean.assign(**sensor_fft_df)
    elif feature =='stdev':
        sensor_stdev = sensor_stdev.assign(**sensor_fft_df)
    elif feature =='median_high':
        sensor_median_high = sensor_median_high.assign(**sensor_fft_df)