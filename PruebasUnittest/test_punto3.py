import unittest
from punto3 import contornos

class TestContornosImagen(unittest.TestCase):

    def test_contorno_azul(self):
        try:
            resultado = contornos("blue_car.jfif", "Prueba azul")
            print("Contornos azul:", resultado)
            self.assertNotEqual(resultado, None)
        except FileNotFoundError as error:
            self.fail(f"Imagen no encontrada: {error}")

    def test_contorno_rojo(self):
        try:
            resultado = contornos("red_car.jfif", "Prueba rojo")
            print("Contornos rojo:", resultado)
            self.assertNotEqual(resultado, None)
        except FileNotFoundError as error:
            self.fail(f"Imagen no encontrada: {error}")

    def test_contorno_amarillo(self):
        try:
            resultado = contornos("yellow_car.jfif", "Prueba amarillo")
            print("Contornos amarillo:", resultado)
            self.assertNotEqual(resultado, None)
        except FileNotFoundError as error:
            self.fail(f"Imagen no encontrada: {error}")

    def test_contorno_vacio(self):
        try:
            resultado = contornos("empty.jfif", "Prueba vacío")
            print("Contornos vacío:", resultado)
            self.assertNotEqual(resultado, None)
        except FileNotFoundError as error:
            self.fail(f"Imagen no encontrada: {error}")

    def test_imagen_no_existe(self):
        with self.assertRaises(FileNotFoundError):
            contornos("imagen_inexistente.jfif", "No existe")

if __name__ == "__main__":
    unittest.main()
