import matplotlib.pyplot as plt

from data_processing import freqs,power_spectrum



plt.plot(freqs,power_spectrum)
plt.xlim(0,max(freqs))
plt.title("Power Spectral Density of the Sunspot Number Time Series")
plt.grid(True)
plt.show()