#!/usr/bin/env python

import sys
sys.path.append('./spectrum')
from spectrum import Spectrum

def plottest(filename = None, outputpdf = "test.pdf"):
	if filename ==None:
		raise IOError("Needs to give input filename.")
	s = Spectrum(filename)
	s.plot1D(outputpdf)
	return
	
def main(argv):
	path = '../data/'
	pdfpath =  '../pdf/'
	f = open(path+'file.txt')
	for lines in f:
		lines = lines.rstrip()
		plottest(filename = path+lines, outputpdf = pdfpath+lines[:-4]+'.pdf')
	return
    
if __name__ == "__main__":
    main(sys.argv[1:])