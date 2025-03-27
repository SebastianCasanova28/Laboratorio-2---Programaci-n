import cv2
import numpy as np

#Generamos la imagen-matriz base
Img_base= np.zeros((480, 640))


#cordenadas para ubicar el cuadrado blanco en el centro del rectangulo
Coor_inicio=(220, 140)
Coor_finales=(420, 340)
color=255

#Generamos el cuadrado blanco
cv2.rectangle(Img_base, Coor_inicio, Coor_finales, color, -1)

cv2.imshow("imagen base", Img_base)

cv2.waitKey()