from x_set_creator import sensor_data_list
from y_set_creator import damage_data_list
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def sensor_fft(sensor_name):


    sensor_fft.sensor_name = []

    for i in range(0,len(sensor_data_list)):
        sample_sensor =sensor_data_list[i][sensor_name]

        fs = 1/750
        #the sampling frequency is 1/(seconds in a total experiment time)

        fourier = np.fft.fft(sample_sensor)
        #sample sensor is the value of s2 which is the 
        freqs = np.fft.fftfreq(sample_sensor.size,d=fs)

        power_spectrum = np.abs(fourier)
        
        sensor_fft.sensor_name.append(max(power_spectrum))

        #plt.plot(freqs,power_spectrum)

        #plt.xlim(0,max(freqs))
        #plt.title("Power Spectral Density of the Sunspot Number Time Series")
        #plt.grid(True)
        #plt.show()

# kalw th sunarthsh pou upologizei to max tou fft gia kathe deigma apo aisththra gia olous tous aisththres
# auta ta max ta pernaw se mia lista wste meta na ftiaksw ena dataframe pou tha balw ola ta dedomena gia olous tous aisththres
sensor_fft('s2')
s2_max = sensor_fft.sensor_name
sensor_fft('s3')
s3_max = sensor_fft.sensor_name
sensor_fft('s4')
s4_max = sensor_fft.sensor_name


#ftiaxno ena dataframe opou bazw mesa ta max tou fft gia kathe aisththra kai to antistoixo damage percentage se auth thn periptwsh

sensor_fft_df = pd.DataFrame({'s2_max':s2_max,'s3_max':s3_max,'s4_max':s4_max,'damage_percentage':damage_data_list})