import dicom
import numpy as np
#import pylab
from matplotlib import pyplot as plt

string = 'mza-01'
archivo = string + '.DCM'

ds1 = dicom.read_file(archivo)

dimentions = ds1.pixel_array.ndim
if dimentions > 2:
    img = ds1.pixel_array[80,:,:]
    print dimentions
else:
    img = ds1.pixel_array

tag = 'DoseGridScaling'

if tag in ds1.dir(''):
    img = ds1.DoseGridScaling * img

plt.figure()
plt.hist(img.ravel(), bins=256,range=(img.min(),img.max()), fc='k', ec='k')
plt.show()

plt.figure()
plt.imshow(img, cmap= 'gray', vmin=img.min(), vmax=img.max()) 
plt.show()

plt.savefig(string + '.png')


#for Tag in range(TagNames1):
#    if Tag == "PixelData":
#        continue
#    archivo1.write(Tag)
#    archivo1.write("\t")
#    archivo1.write
    




