from astropy.io import fits
import matplotlib.pyplot as p

class Spectrum(object):
    def __init__(self, file = None):
    	"""
    	Specify filename for Spectrum object
    	"""
        if file ==None:
            raise IOError('No filename')
        self.file = fits.open(file)
        self.ra = self.file[1].header["ra"]
        self.dec = self.file[1].header["dec"]
        self.data = self.file[1].data
        self.cols = self.file[1].columns
        
    def plot1D(self, outputpdf, x=0, y=1):
    	"""
    	Method to plot spectrum. 
    	Argument: outputpdf as filename for pdf
    	Optional: x, y index for x and y axis in Spectrum.data table
    	"""
    	fig, (ax) = p.subplots(1,1)
    	ax.plot(self.data[self.cols.names[x]], self.data[self.cols.names[y]])
    	ax.set_xlabel("Wavelength ("+self.cols.units[x].lower()+")")
    	ax.set_ylabel("Flux ("+self.cols.units[y].lower()+")")
    	#p.show()
    	p.savefig(outputpdf)