import dicom
import numpy as np
#import pylab
from matplotlib import pyplot as plt

string = 'FANT CIRS AX -10'
archivo = string + '.dcm'

ds1 = dicom.read_file(archivo)
img = ds1.pixel_array






plt.figure()
plt.hist(img,256,[0,256]); 
plt.xlim([0,256]) 
plt.show()

plt.figure()
imgplot = plt.imshow(img, cmap= 'gray', )
#clim=(105,140)
plt.show()