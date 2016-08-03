# teambadass



This is a module for working with spectra files.





__funkyfunction__

* Reads in ascii data file to "table" list


* It uses the matplotlib module to plot() wavelength (table[:,0]) against flux (table[:,1])
* Or reads in fits file to Spectrum Object
* Spectrum has ra, dec, data, matplotlib to plot() as above

__to use:__

* add make_plot directory to your python path
* Go into data directory
* from funkyfunction import make_plot
* make_plot('filename.extension')
  * extension can definitely be ascii, maybe fits (fits file compatibility fixed now)