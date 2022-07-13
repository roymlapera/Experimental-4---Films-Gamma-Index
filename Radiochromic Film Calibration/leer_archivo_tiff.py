import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Srinacharindosimetr.tif',-1)
 
img_R = img[:,:,2]
#img_R = img

#equ = cv2.equalizeHist(img_R)

#color = ('b','g','r')
#for i,col in enumerate(color):
#    histr = cv2.calcHist([img],[i],None,[256],[0,256])
#    plt.plot(histr,color = col)
#    plt.xlim([0,256])
#plt.show()

plt.figure()
plt.hist(img_R.ravel(),256); 
#plt.hist(equ.ravel(),256,[0,256]);
#plt.xlim([0,256]) 
plt.show()

plt.figure()
#imgplot = plt.imshow(img)
imgplot = plt.imshow(img_R, cmap= 'gray', clim=(0.0,2500.0))
plt.show()
#imgplot3 = plt.imshow(equ)

#cv2.imshow('img_R',img_R)
#cv2.imshow('equ',equ)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

