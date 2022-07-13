import numpy as np
import matplotlib.pyplot as plt
import cv2

skiprows = 7

string = 'mza_01'
archivo = open(string + '.flm','r')

#columna

#columna = np.loadtxt(archivo, delimiter='\t', skiprows=skiprows,usecols=(0,))

#max_y = columna[-1]
#min_y = columna[1]

#archivo.close()

#fila

archivo = open(string + '.flm','r')

filas=archivo.readlines()

v = filas[skiprows-1].split('\t')


eje_x = np.float32(v[1:])

eje_x_inv = np.fliplr(eje_x)
#max_x = v[-1]
#min_x = v[1]
#
#archivo.close()
#
#archivo = open(string + '.flm','r')
#
#mat = np.loadtxt(archivo, delimiter='\t', skiprows=skiprows,usecols=range(1,len(v)))
##el archivo tiene 602 columnas de datos, la ultima columna tiene '\n' por eso se omite
#
##Bien! Tenemos la matriz
#
##maximo = np.amax(mat)
##
##mat_norm_255 = mat*255/maximo
#
##Grafica el histograma de la matriz mat_norm_255
#fig1 = plt.figure()
#
#plt.hist(mat.ravel(), bins=256, fc='k', ec='k')
#
#plt.show()
#
##plt.savefig(string + '_h.tiff')
#
##Grafica la imagen de la matriz mat_norm_255
#fig2 = plt.figure()
#
##para el caso del phantomdata (el de ramathibodi
##mat = np.flipud(mat)
##rows,cols = mat.shape
##mat = np.rot90(mat, k=3)
#
#imgplot = plt.imshow(mat, clim=(0, 256),cmap='gray', extent=[float(min_x),float(max_x),float(min_y),float(max_y)],vmin=0.0, vmax=270.0)
# 
## 
#plt.show()
#
#plt.savefig(string + '.tiff')
#
#archivo.close()
#
#
#
#
