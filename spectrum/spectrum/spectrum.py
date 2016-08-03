from astropy.io import fits

class Spectrum(object):
    def __init__(self, file = None):
        if file ==None:
            raise IOError('No filename')
        self.file = fits.open(file)
        self.ra = self.file[1].header["ra"]
        self.dec = self.file[1].header["dec"]
        self.data = self.file[1].data
        self.cols = self.file[1].columns
