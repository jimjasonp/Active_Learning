import pandas as pd
import statistics

sensor_fft_df = pd.DataFrame()
sensor_fft = []


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


def df_creator(sensor):
    new_data = {sensor: sensor_fft}
    global sensor_fft_df
    sensor_fft_df = sensor_fft_df.assign(**new_data)


def feature_df_assign(feature,sensor_fft_df):
    if feature == 'max':
        global sensor_max
        sensor_max = sensor_max.assign(**sensor_fft_df)
        sensor_max.to_csv('sensor_max')
    elif feature =='mean':
        global sensor_mean
        sensor_mean = sensor_mean.assign(**sensor_fft_df)
        sensor_mean.to_csv('sensor_mean')
    elif feature =='stdev':
        global sensor_stdev
        sensor_stdev = sensor_stdev.assign(**sensor_fft_df)
        sensor_stdev.to_csv('sensor_stdev')
    elif feature =='median_high':
        global sensor_median_high
        sensor_median_high = sensor_median_high.assign(**sensor_fft_df)
        sensor_median_high.to_csv('sensor_medianhigh')