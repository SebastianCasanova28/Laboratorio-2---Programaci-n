import cv2
# Esta funcion se encarga de obtener los contornos de cada imagen, ademas de mostrar en pantalla los lugares

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
def camara(): 
    
    # Get the default frame width and height
    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))


while True:
    # Read frame from camera
    ret, frame = cam.read()

    #print(len(frame))

    # Display the captured frame after flipping
    cv2.imshow('Parking Lot Camera', cv2.flip(frame,1))  

    # Wait for 10ms and exit if any key is pressed
    if cv2.waitKey(10) != -1:
        break
def contornos(a,b):
    image_color=cv2.imread(a)
    if image_color is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen: {image_color}")
    cv2.imshow(b,image_color)
    image=cv2.imread(a, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen: {image}")
    Borde= cv2.Canny (image, 100, 200)
    Contorno, _=cv2.findContours(Borde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return len(Contorno)
#Esta funcion se encarga de identificar los lugares ocupados o desocupados utilizando los contornos obtenidos de la funcion contornos(a,b)
def identifyspot(Contorno_Azul, Contorno_Rojo, Contorno_Amarillo, Contorno_Vacio):
    if Contorno_Azul>Contorno_Vacio:
        print("lugar 1: ocupado")
    else:
        print("Lugar 1: desocupado")
    
    if Contorno_Rojo>Contorno_Vacio:
            print("lugar 2: ocupado")
    else:
        print("Lugar 2: desocupado")
    
    if Contorno_Amarillo>Contorno_Vacio:
        print("lugar 3: ocupado")
    else:
        print("Lugar 3: desocupado")
    
    if Contorno_Vacio>=Contorno_Vacio:
        print("lugar 4: desocupado")

#Se llama la funcion de contornos, en donde se almacenan los contornos calculados apartir de las diferentes imagenes
Contorno_Azul=contornos("blue_car.jfif", "Lugar 1, Auto azul")
Contorno_Rojo=contornos("red_car.jfif", "Lugar 2, Auto Rojo")
Contorno_Amarillo=contornos("yellow_car.jfif", "Lugar 3, Auto Amarillo")
Contorno_Vacio=contornos("empty.jfif", "Lugar 3")

# Se llama a la funcion para que se ejecute
identifyspot(Contorno_Azul, Contorno_Rojo, Contorno_Amarillo, Contorno_Vacio)


cv2.waitKey(0)
cv2.destroyAllWindows()