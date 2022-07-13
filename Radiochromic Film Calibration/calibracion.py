import numpy as np
from pylab import *
import pylab as py 

# CALIBRACION CON FUNCION POLINOMICA

# importacion de datos

filename = 'dosis_vs_intensidad.txt'

archivo = open(filename,'r')
x = np.loadtxt(archivo, delimiter='\t', skiprows=1,usecols=(0,))
archivo.close()

archivo = open(filename,'r')
intensidades = np.loadtxt(archivo, delimiter='\t', skiprows=1,usecols=(1,))
archivo.close()

# ajuste

a,b,c,d,e,f,g,h = polyfit(x, intensidades, 7) 

archivo_calibracion = open('calibracion.txt','w')
archivo_calibracion.write('Coeficientes del ajuste:\n')
archivo_calibracion.write('a = ' + '\t%.3e\n' % a)
archivo_calibracion.write('b = ' + '\t%.3e\n' % b)
archivo_calibracion.write('c = ' + '\t%.3e\n' % c)
archivo_calibracion.write('d = ' + '\t%.3e\n' % d)
archivo_calibracion.write('e = ' + '\t%.3e\n' % e)
archivo_calibracion.write('f = ' + '\t%.3e\n' % f)
archivo_calibracion.write('g = ' + '\t%.3e\n' % g)
archivo_calibracion.write('h = ' + '\t%.3e\n' % h)
archivo.close()

# ploteo

plt.figure()
plot(x, intensidades, 'ro', x, a*x**7+b*x**6+c*x**5+d*x**4+e*x**3+f*x**2+g*x+h, '-k')
py.xlim([-10,325])
py.xlabel('Dosis [cg]')
py.ylabel('Intensidad de pixel [U.a.]')
py.xlim([-10,325])
py.savefig('calibracion.tiff')
show() 


