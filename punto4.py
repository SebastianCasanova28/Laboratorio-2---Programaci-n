import cv2
import numpy as np

# Esta función se encarga de obtener los contornos de cada imagen
def contornos(video):
    # Leer la imagen en escala de grises
    image = cv2.imread(video, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen: {video}")
    # Detectar bordes con Canny
    Borde = cv2.Canny(image, 100, 200)
    # Encontrar contornos
    Contorno, _ = cv2.findContours(Borde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return len(Contorno)

# Configuración del rectángulo y video
Coor_inicio = (220, 140)  # Esquina superior izquierda del rectángulo
Coor_finales = (420, 340)  # Esquina inferior derecha del rectángulo
color = (255, 255, 255)  # Color del rectángulo
video = cv2.VideoCapture("http://192.168.198.5:8080/video")

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    # Dibujar el rectángulo en cada cuadro
    cv2.rectangle(frame, Coor_inicio, Coor_finales, color, 2)

    # Extraer la región de interés (ROI) dentro del rectángulo
    x_inicio, y_inicio = Coor_inicio
    x_final, y_final = Coor_finales
    roi = frame[y_inicio:y_final, x_inicio:x_final]  # Recortar la región del rectángulo

    # Guardar la ROI temporalmente para usarla con la función contornos()
    temp_image = "temp_roi.jpg"
    cv2.imwrite(temp_image, roi)

    # Calcular el número de contornos dentro de la ROI
    num_contornos = contornos(temp_image)

    # Determinar si el espacio está ocupado o vacío en función del número de contornos
    umbral_contornos = 10  # Umbral de contornos para decidir si el espacio está ocupado
    estado = "Ocupado" if num_contornos > umbral_contornos else "Libre"

    # Mostrar el estado en el cuadro
    color_estado = (0, 0, 255) if estado == "Ocupado" else (0, 255, 0)  # Rojo para ocupado, verde para libre
    cv2.putText(frame, estado, (x_inicio, y_inicio - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color_estado, 2)

    # Mostrar el video en la ventana con los resultados
    cv2.imshow("DETECTOR", frame)

    # Salir del bucle al presionar la tecla '1'
    if cv2.waitKey(1) & 0xFF == ord('1'):
        break

# Liberar recursos y cerrar ventanas
video.release()
cv2.destroyAllWindows()
