import unittest
from punto1 import generar_imagen 

class TestImagen(unittest.TestCase):
    def test_imagen_no_nula(self):
        img = generar_imagen()
        self.assertIsNotNone(img)

    def test_dimensiones_correctas(self):
        img = generar_imagen()
        self.assertEqual(img.shape, (480, 640))

    def test_centro_es_blanco(self):
        img = generar_imagen()
        self.assertEqual(img[240, 320], 255)

    def test_borde_es_negro(self):
        img = generar_imagen()
        self.assertEqual(img[0, 0], 0)

if __name__ == '__main__':
    unittest.main()
