import matplotlib.pyplot as plt

from x_set_creator import sensor_data_list,power_spectrum


plt.plot(sensor_data_list[100]['s2'])
plt.title("random experiment of sensor s2 as timeseries")
plt.grid(True)
plt.show()




plt.plot(power_spectrum)
plt.title("fft on timeseries")
plt.xlim(0,300)
plt.grid(True)
plt.show()
