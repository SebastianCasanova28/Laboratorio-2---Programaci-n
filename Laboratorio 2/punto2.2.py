import cv2
import numpy as  np
def promedios_color(Img):
    Imgleida=cv2.imread(Img, cv2.IMREAD_COLOR)
    #Matriz de cada color
    MAzul=Imgleida[:,:,0]
    MVerde=Imgleida[:,:,1]
    MRojo=Imgleida[:,:,2]

    #Dimensiones de cada plano
    DAzul=MAzul.shape
    DVerde=MVerde.shape
    DRojo=MRojo.shape

    #Promedio de cada color 
    SAzul=0.0
    for row in MAzul:
        for i in row:
            SAzul+=i
    PAzul=SAzul/(DAzul[0]*DAzul[1])
   
    SVerde=0.0
    for row in MVerde:
        for j in row:
            SVerde+=j
    PVerde=SVerde/(DVerde[0]*DVerde[1])
    
    SRojo=0.0
    for row in MRojo:
        for k in row:
            SRojo+=k
    PRojo=SRojo/(DRojo[0]*DRojo[1])
    
    return PAzul, PVerde, PRojo

def identifyColor(Img):
    PAzul, PVerde, PRojo = promedios_color(Img)
    # Identificar el color dominante
    if PRojo > PAzul and PRojo > PVerde:
        return "Rojo"
    elif PAzul > PRojo and PAzul > PVerde:
        return "Azul"
    elif PVerde > PRojo and PVerde > PAzul:
        return "Amarillo"
    else:
        return "Color no identificado"


Img=input("Ingrese  blue_car.jfif , red_car.jfif o yellow_car.jfif para identificar su color: ")
PAzul, PVerde, PRojo=promedios_color(Img)
print(f"El promedio del plano azul es {PAzul}")
print(f"El promedio del plano Verde es {PVerde}")
print(f"El promedio del plano Rojo es {PRojo}")
color = identifyColor(Img)
print(f"El color del automóvil es: {color}")