import cv2

# Esta función se encarga de obtener los contornos de cada imagen, además de mostrar en pantalla los lugares
def contornos(a, b):
    image_color = cv2.imread(a)
    if image_color is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen: {a}")
    
    cv2.imshow(b, image_color)  # Solo se ejecuta si se llama desde main
    image = cv2.imread(a, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen: {a}")
    
    Borde = cv2.Canny(image, 100, 200)
    Contorno, _ = cv2.findContours(Borde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return len(Contorno)

# Esta función identifica los lugares ocupados o desocupados usando los contornos obtenidos
def identifyspot(Contorno_Azul, Contorno_Rojo, Contorno_Amarillo, Contorno_Vacio):
    if Contorno_Azul > Contorno_Vacio:
        print("lugar 1: ocupado")
    else:
        print("Lugar 1: desocupado")

    if Contorno_Rojo > Contorno_Vacio:
        print("lugar 2: ocupado")
    else:
        print("Lugar 2: desocupado")

    if Contorno_Amarillo > Contorno_Vacio:
        print("lugar 3: ocupado")
    else:
        print("Lugar 3: desocupado")

    if Contorno_Vacio >= Contorno_Vacio:
        print("lugar 4: desocupado")

if __name__ == "__main__":
    Contorno_Azul = contornos("blue_car.jfif", "Lugar 1, Auto azul")
    Contorno_Rojo = contornos("red_car.jfif", "Lugar 2, Auto Rojo")
    Contorno_Amarillo = contornos("yellow_car.jfif", "Lugar 3, Auto Amarillo")
    Contorno_Vacio = contornos("empty.jfif", "Lugar 4")

    identifyspot(Contorno_Azul, Contorno_Rojo, Contorno_Amarillo, Contorno_Vacio)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
