import cv2
import numpy as np

def generar_imagen():
    # Generamos la imagen-matriz base
    Img_base = np.zeros((480, 640))

    # Coordenadas para ubicar el cuadrado blanco en el centro del rectángulo
    Coor_inicio = (220, 140)     # Esquina superior izquierda
    Coor_finales = (420, 340)    # Esquina inferior derecha
    color = 255

    # Generamos el cuadrado blanco
    cv2.rectangle(Img_base, Coor_inicio, Coor_finales, color, -1)

    return Img_base

if __name__ == '__main__':
    img = generar_imagen()
    cv2.imshow("imagen base", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
