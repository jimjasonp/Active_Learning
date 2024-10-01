import matplotlib.pyplot as plt

from data_processing import freqs,sensor_data_list,unfiltered_power_spectrum,power_spectrum
plt.plot(sensor_data_list[100]['s2'])
plt.title("random experiment of sensor s2 as timeseries")
plt.grid(True)
plt.show()

plt.plot(freqs,unfiltered_power_spectrum)
plt.xlim(0,max(freqs))
plt.title("fft on timeseries")
plt.grid(True)
plt.show()


plt.plot(power_spectrum)
plt.title("filtered fft on timeseries")
plt.grid(True)
plt.show()
