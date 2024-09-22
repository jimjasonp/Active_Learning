from x_set_creator import sensor_data_list
from y_set_creator import damage_data_list
import matplotlib.pyplot as plt
import numpy as np


for i in range(0,100):
    sample_sensor =sensor_data_list[i]['s2']

    fs = 1/750
    #the sampling frequency is 1/(seconds in a total experiment time)

    fourier = np.fft.fft(sample_sensor)
    #sample sensor is the value of s2 which is the 
    freqs = np.fft.fftfreq(sample_sensor.size,d=fs)

    power_spectrum = np.abs(fourier)
    print(max(power_spectrum))
    #plt.plot(freqs,power_spectrum)

    #plt.xlim(0,max(freqs))
    #plt.title("Power Spectral Density of the Sunspot Number Time Series")
    #plt.grid(True)
    #plt.show()