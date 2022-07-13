import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(dosis, a, b):
  return (a + b*dosis)/(a + dosis)

def func_inv(aux,a,b):
    return a*(1-aux)/(aux-b)

# ingreso de datos

data = np.loadtxt('dosis_vs_intensidad(test).txt', skiprows=1)

dosis = data[:,0].astype(np.float64) #dosis
intensidad_pixel = data[:,1].astype(np.float64) # intensidad de pixel

if dosis[0] == 0.0:
    netOD = np.log10(intensidad_pixel[0]/intensidad_pixel)

#ajuste

popt, pcov = curve_fit(func, dosis, np.exp(-1.0*netOD))

dosis_adj = np.arange(dosis[0],dosis[-1],0.01)
netOD_adj = -np.log(func(dosis_adj, popt[0], popt[1]))

desvio_dosis = np.std(dosis)
varianza_dosis = desvio_dosis*desvio_dosis

residuos_alcuadrado = np.square(dosis - func_inv(np.exp(-1.0*netOD),popt[0],popt[1]))
varianza_residual = np.sum(residuos_alcuadrado)/len(residuos_alcuadrado)

r_cuadrado = 1 - varianza_residual/varianza_dosis

# ploteo de las curvas

fig = plt.figure()

plt.plot(dosis, netOD,'b*', label = 'puntos experimentales')

plt.plot(dosis_adj, netOD_adj,'g', label = 'ajuste')

plt.xlabel('Dosis [$cGy$]', fontsize=14)
plt.ylabel('netOD', fontsize=14)

plt.legend(loc=2,prop={'size':14})

plt.show()
plt.savefig('ajuste_siriraj.jpg')

archivo = open('parametros(func5).txt','w')
archivo.write('a\t%lf\n' % popt[0])
archivo.write('b\t%lf\n' % popt[1])

#esto esta para cuando tengas un tercer parametro de ajuste
#archivo.write('c\t%lf\n' % popt[2]) 
archivo.write('R2\t%lf\n' % r_cuadrado)
archivo.close()