import numpy as np
import matplotlib.pyplot as plt

def make_plot(spectrumfile):
	table = np.loadtxt(spectrumfile, skiprows=1)
	wav = table[:,0]
	flux = table[:,1]
	plt.plot(wav,flux)
	plt.show()