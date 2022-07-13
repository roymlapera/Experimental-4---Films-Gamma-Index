import numpy as np
import cv2
from matplotlib import pyplot as plt

def read_dcm(filename):
    ds = dicom.read_file(filename)

    return ds1.pixel_array

def read_flm(filename):
    archivo = open(filename,'r')
    
    #columna
    
    columna = np.loadtxt(archivo, delimiter='\t', skiprows=7,usecols=(0,))
    
    max_y = columna[-1]
    min_y = columna[1]
    
    archivo.close()
    
    #fila
    
    archivo = open(filename,'r')
    
    filas=archivo.readlines()
    
    v = filas[6].split('\t')
    max_x = v[-1]
    min_x = v[1]
    
    archivo.close()
    
    archivo = open(filename,'r')
    
    mat = np.loadtxt(archivo, delimiter='\t', skiprows=7,usecols=range(1,601))
    #el archivo tiene 602 columnas de datos, la ultima columna tiene '\n' por eso se omite
    
    #Bien! Tenemos la matriz
    
    maximo = np.amax(mat)
    
    mat_norm_255 = mat*255/maximo
    
    archivo.close()

    return mat_norm_255

def read_tif(filename):
    img = cv2.imread(filename,1)
    
    img_R = img[:,:,2]
    
    equ = cv2.equalizeHist(img_R)
    
    #return img_R o equ???
    
    return img_R