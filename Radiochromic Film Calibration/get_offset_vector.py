import dicom
import numpy as np
#import pylab
from matplotlib import pyplot as plt

string = "Dose plane 1.5 cm from iso_NCI"
archivo = string + ".dcm"

ds1 = dicom.read_file(archivo)

a = ds1.GridFrameOffsetVector

offset_vector = np.zeros(len(a))

for i in range(0,len(a)):
    offset_vector[i] = np.float(a[i])