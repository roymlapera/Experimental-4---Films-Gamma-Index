import cv2
import numpy as np
from matplotlib import pyplot as plt

Dosis = '100'

filename = 'siriraj' + Dosis + '.tif'
orig = cv2.imread(filename,-1)
#                               <-------      OJO CON ESTO, NO ESTA ELIGIENDO EL CANAL ROJOOOOOO
image = orig[:,:,2]

drawing = False # true if mouse is pressed
refPt = []

# mouse callback function
def draw_rectangle(event,x,y,flags,param):
   # grab references to the global variables
   global refPt, drawing

   # if the left mouse button was clicked, record the starting
   # (x, y) coordinates and indicate that drawing is being
   # performed
   if event == cv2.EVENT_LBUTTONDOWN:
  	refPt = [(x, y)]
  	drawing = True

   # check to see if the left mouse button was released
   elif event == cv2.EVENT_LBUTTONUP:
  	# record the ending (x, y) coordinates and indicate that
  	# the cropping operation is finished
  	refPt.append((x, y))
  	drawing = False

  	# draw a rectangle around the region of interest
  	cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
  	#cv2.imshow("image", image)

# construct the argument parser and parse the arguments

# load the image, clone it, and setup the mouse callback function
#image = cv2.imread(filename,1)


##Caso Ramathibodi
#image = orig

#image = np.array(image)

image = np.array(image)

#image = cv2.imread(filename,-1)

clone = image.copy()
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

# keep looping until the 'q' key is pressed
while True:
    # display the image and wait for a keypress
    cv2.imshow('image', image)
    key = cv2.waitKey(1) & 0xFF

    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
  	image = clone.copy()

    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break

# if there are two reference points, then crop the region of interest
# from the image and display it
if len(refPt) == 2:
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    cv2.imshow("ROI", roi)
    cv2.waitKey(0)
    
# close all open windows
cv2.destroyAllWindows()

vector = roi.ravel() 
contador = 0
nro_pixeles = 0

promedio = np.mean(roi)

archivo = open('dosis_vs_intensidad(test).txt','a')

#archivo.write("Dosis[cg]\tIntensidad[pixeles]\n")

#archivo.write(Dosis + '\t%d\n' % promedio)

archivo.close()

#color = ('b','g','r')
#for i,col in enumerate(color):
#    histr = cv2.calcHist([image],[i],None,[5000],[0,65536])
#    plt.plot(histr,color = col)
#    #plt.xlim([-10,65600])
#plt.show()