from spectrum import Spectrum
import sys
import matplotlib.pyplot as p

spectrum = Spectrum(file =sys.argv[1])
fig, (ax) = p.subplots(1,1)
ax.plot(spectrum.data[spectrum.cols.names[0]], spectrum.data[spectrum.cols.names[2]])
ax.set_xlabel("Wavelength ("+spectrum.cols.units[0].lower()+")")
ax.set_ylabel("Flux ("+spectrum.cols.units[1].lower()+")")
p.show()
