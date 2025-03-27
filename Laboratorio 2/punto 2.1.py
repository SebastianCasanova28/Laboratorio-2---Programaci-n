# Import OpenCV module
import cv2
import numpy as np

# SE lee la imagen
img = cv2.imread("blue_car.jfif", cv2.IMREAD_COLOR)

# Se Obtienen dimensiones de la imagen
dims=img.shape
print(f'Image has {dims[2]} color planes each having {dims[0]} rows and {dims[1]} columns')
#se obtiene matriz de cada color
bluePlane=img[:,:,0]
greenPlane=img[:,:,1]
redPlane=img[:,:,2]

cv2.imshow("image", img)
cv2.imshow("Blue plane", bluePlane)
cv2.imshow("Green plane", greenPlane)
cv2.imshow("Red plane", redPlane)

planered=redPlane
planeblue=bluePlane
planegreen=greenPlane
#se obtienen dimensiones de cada plano
dims1=planered.shape
print(f'Plane has {dims[0]} rows and {dims[1]} columns')
dims2=planeblue.shape
print(f'Plane blue has {dims2[0]} rows and {dims2[1]} columns')
dims3=planegreen.shape
print(f'Plane green has {dims3[0]} rows and {dims3[1]} columns')

#PROMEDIOS DE CADA PLANO
meanRed=0.0
for row in planered:
    for p in row:    
        meanRed+=p
        
print(f'Mean of plane red is: {meanRed/(dims[0]*dims[1])}')

meanBlue=0.0
for row in planeblue:
    for b in row:    
        meanBlue+=b
   
print(f'Mean of plane blue is: {meanBlue/(dims2[0]*dims2[1])}')

meanGreen=0.0
for row in planegreen:
    for g in row:    
        meanGreen+=g
        
print(f'Mean of plane green is: {meanGreen/(dims3[0]*dims3[1])}')


cv2.waitKey()