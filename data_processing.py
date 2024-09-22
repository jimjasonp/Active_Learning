from x_set_creator import sensor_data_list
from y_set_creator import damage_data_list
import matplotlib.pyplot as plt
import numpy as np


def sensor_fft(sensor_name):


    sensor_fft.sensor_name = []

    for i in range(0,100):
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


sensor_fft('s2')
print(sensor_fft.sensor_name)
sensor_fft('s3')
print(sensor_fft.sensor_name)
sensor_fft('s4')
print(sensor_fft.sensor_name)