from astropy.io import fits
import matplotlib.pyplot as p

class Spectrum(object):
    def __init__(self, file = None):
        if file ==None:
            raise IOError('No filename')
        self.file = fits.open(file)
        self.ra = self.file[1].header["ra"]
        self.dec = self.file[1].header["dec"]
        self.data = self.file[1].data
        self.cols = self.file[1].columns
        
    def plot1D(self, outputpdf):
    	fig, (ax) = p.subplots(1,1)
    	ax.plot(self.data[self.cols.names[0]], self.data[self.cols.names[1]])
    	ax.set_xlabel("Wavelength ("+self.cols.units[0].lower()+")")
    	ax.set_ylabel("Flux ("+self.cols.units[1].lower()+")")
    	#p.show()
    	p.savefig(outputpdf)