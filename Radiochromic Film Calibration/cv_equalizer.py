# Lee una imagen en python y la equaliza interactivamente

import cv2
import pydicom as dicom

def nothing(x):
    pass

plan = dicom.read_file('CIRS Phantom IMRT.dcm')
img = plan.pixel_array*plan.DoseGridScaling

min_x = img.min()
max_x = img.max()

#enlarge image by 2
img_large = cv2.resize(img, (0,0), fx=2.0, fy=2.0) 

img_large_equ = 1/(max_x - min_x)*(img_large - max_x) + 1

cv2.namedWindow('image')

# create trackbars for color equalization
cv2.createTrackbar('min','image',0,255, nothing)
cv2.createTrackbar('max','image',255,255, nothing)


while True:
    
    cv2.imshow('image',img_large_equ)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
    new_min_x = max_x*cv2.getTrackbarPos('min','image')/255.0
    
    new_max_x = max_x*cv2.getTrackbarPos('max','image')/255.0
    
    if not new_min_x == new_max_x:
        img_large_equ = 1/(new_max_x - new_min_x)*(img_large - new_max_x) + 1

    
cv2.destroyAllWindows()