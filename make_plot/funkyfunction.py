import numpy as np
import matplotlib.pyplot as plt
from spectrum import Spectrum

def make_plot(spectrumfile):
	if spectrumfile[-4:] == 'fits':
		spectrum = Spectrum(file =spectrumfile)
		fig, (ax) = plt.subplots(1,1)
		ax.plot(spectrum.data[spectrum.cols.names[0]], spectrum.data[spectrum.cols.names[1]])
		ax.set_xlabel("Wavelength ("+spectrum.cols.units[0].lower()+")")
		ax.set_ylabel("Flux ("+spectrum.cols.units[1].lower()+")")
	else:
		table = np.loadtxt(spectrumfile, skiprows=1)
		wav = table[:,0]
		flux = table[:,1]
		plt.plot(wav,flux)
	plt.show()
