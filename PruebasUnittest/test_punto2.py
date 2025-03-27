import unittest
from punto2 import promedios_color, identifyColor

class TestColorPromedio(unittest.TestCase):

    def test_promedios_color(self):
        # Comprobar que los promedios devueltos sean valores positivos
        azul, verde, rojo = promedios_color("blue_car.jfif")
        self.assertTrue(azul >= 0)
        self.assertTrue(verde >= 0)
        self.assertTrue(rojo >= 0)

    def test_identificar_color_azul(self):
        # Verificar que se identifique correctamente el color azul
        color = identifyColor("blue_car.jfif")
        self.assertEqual(color, "Azul")

    def test_identificar_color_rojo(self):
        # Verificar que se identifique correctamente el color rojo
        color = identifyColor("red_car.jfif")
        self.assertEqual(color, "Rojo")

    def test_identificar_color_amarillo(self):
        # Verificar que se identifique correctamente el color amarillo
        color = identifyColor("yellow_car.jfif")
        self.assertEqual(color, "Amarillo")

unittest.main()
