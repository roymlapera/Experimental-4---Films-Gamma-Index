import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func1(netOD, a, b):
  return a*netOD*netOD+b*netOD
  
def func2(netOD, a, b):
  return a*(netOD**2.5)+b*netOD

def func3(netOD, a, b,c):
  return a*netOD*netOD*netOD+b*netOD*netOD+c*netOD

def func4(netOD, a, b,c):
  return (a+b*netOD)/(netOD-c)

#-------------------------------------------------------------------------------

# importacion de datos

data = np.loadtxt('dosis_vs_intensidad.txt', skiprows=1)

dosis = data[:,0].astype(np.float64) #dosis
intensidad_pixel = data[:,1].astype(np.float64) # intensidad de pixel

if dosis[0] == 0.0:
    netOD = np.log10(intensidad_pixel[0]/intensidad_pixel)

# ajuste

popt, pcov = curve_fit(func1, netOD, dosis)

netOD_adj = np.arange(netOD[0],netOD[-1],0.01)
dosis_adj = func1(netOD_adj,popt[0],popt[1])

desvio_dosis = np.std(dosis)
varianza_dosis = desvio_dosis*desvio_dosis

residuos_alcuadrado = np.square(dosis - func1(netOD, popt[0], popt[1]))
varianza_residual = np.sum(residuos_alcuadrado)/len(residuos_alcuadrado)

r_cuadrado = 1 - varianza_residual/varianza_dosis

# ploteo de las curvas

fig = plt.figure()

plt.plot(netOD,dosis,'b*', label = 'puntos experimentales')

plt.plot(netOD_adj,dosis_adj,'g', label = 'ajuste')

plt.xlabel('netOD', fontsize=14)
plt.ylabel('Dosis [$cGy$]', fontsize=14)

plt.legend(loc=2,prop={'size':14})

plt.show()

archivo = open('parametros(func1).txt','w')
archivo.write('a\t%lf\n' % popt[0])
archivo.write('b\t%lf\n' % popt[1])
#esto esta para cuando tengas un tercer parametro de ajuste
#archivo.write('c\t%lf\n' % popt[2]) 
archivo.write('R2\t%lf\n' % r_cuadrado)
archivo.close()

#-------------------------------------------------------------------------------

popt, pcov = curve_fit(func2, netOD, dosis)

netOD_adj = np.arange(netOD[0],netOD[-1],0.01)
dosis_adj = func2(netOD_adj,popt[0],popt[1])

desvio_dosis = np.std(dosis)
varianza_dosis = desvio_dosis*desvio_dosis

residuos_alcuadrado = np.square(dosis - func2(netOD, popt[0], popt[1]))
varianza_residual = np.sum(residuos_alcuadrado)/len(residuos_alcuadrado)

r_cuadrado = 1 - varianza_residual/varianza_dosis

# dibujo de las curvas

fig = plt.figure()

plt.plot(netOD,dosis,'b*', label = 'puntos experimentales')

plt.plot(netOD_adj,dosis_adj,'g', label = 'ajuste')

plt.xlabel('netOD', fontsize=14)
plt.ylabel('Dosis [$cGy$]', fontsize=14)

plt.legend(loc=2,prop={'size':14})

plt.show()

archivo = open('parametros(func2).txt','w')
archivo.write('a\t%lf\n' % popt[0])
archivo.write('b\t%lf\n' % popt[1])
#esto esta para cuando tengas un tercer parametro de ajuste
#archivo.write('c\t%lf\n' % popt[2]) 
archivo.write('R2\t%lf\n' % r_cuadrado)
archivo.close()

#-------------------------------------------------------------------------------

popt, pcov = curve_fit(func3, netOD, dosis)

netOD_adj = np.arange(netOD[0],netOD[-1],0.01)
dosis_adj = func3(netOD_adj,popt[0],popt[1],popt[2])

desvio_dosis = np.std(dosis)
varianza_dosis = desvio_dosis*desvio_dosis

residuos_alcuadrado = np.square(dosis - func3(netOD, popt[0], popt[1],popt[2]))
varianza_residual = np.sum(residuos_alcuadrado)/len(residuos_alcuadrado)

r_cuadrado = 1 - varianza_residual/varianza_dosis

# dibujo de las curvas

fig = plt.figure()

plt.plot(netOD,dosis,'b*', label = 'puntos experimentales')

plt.plot(netOD_adj,dosis_adj,'g', label = 'ajuste')

plt.xlabel('netOD', fontsize=14)
plt.ylabel('Dosis [$cGy$]', fontsize=14)

plt.legend(loc=2,prop={'size':14})

plt.show()

archivo = open('parametros(func3).txt','w')
archivo.write('a\t%lf\n' % popt[0])
archivo.write('b\t%lf\n' % popt[1])
#esto esta para cuando tengas un tercer parametro de ajuste
archivo.write('c\t%lf\n' % popt[2]) 
archivo.write('R2\t%lf\n' % r_cuadrado)
archivo.close()

#-------------------------------------------------------------------------------

popt, pcov = curve_fit(func4, netOD, dosis)

netOD_adj = np.arange(netOD[0],netOD[-1],0.01)
dosis_adj = func4(netOD_adj,popt[0],popt[1],popt[2])

desvio_dosis = np.std(dosis)
varianza_dosis = desvio_dosis*desvio_dosis

residuos_alcuadrado = np.square(dosis - func4(netOD, popt[0], popt[1],popt[2]))
varianza_residual = np.sum(residuos_alcuadrado)/len(residuos_alcuadrado)

r_cuadrado = 1 - varianza_residual/varianza_dosis

# dibujo de las curvas

fig = plt.figure()

plt.plot(netOD,dosis,'b*', label = 'puntos experimentales')

plt.plot(netOD_adj,dosis_adj,'g', label = 'ajuste')

plt.xlabel('netOD', fontsize=14)
plt.ylabel('Dosis [$cGy$]', fontsize=14)

plt.legend(loc=2,prop={'size':14})

plt.show()

archivo = open('parametros(func4).txt','w')
archivo.write('a\t%lf\n' % popt[0])
archivo.write('b\t%lf\n' % popt[1])
#esto esta para cuando tengas un tercer parametro de ajuste
archivo.write('c\t%lf\n' % popt[2]) 
archivo.write('R2\t%lf\n' % r_cuadrado)
archivo.close()