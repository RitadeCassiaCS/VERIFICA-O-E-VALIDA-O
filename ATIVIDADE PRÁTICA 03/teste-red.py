import unittest
from media import calcular_media

class TestMedia(unittest.TestCase):
    
    def test_media_simples(self):
        self.assertEqual(calcular_media(5, 5, 5), 5)
    
    def test_media_valores_zero(self):
        self.assertEqual(calcular_media(0, 0, 0), 0)
    
    def test_media_valores_maximos(self):
        self.assertEqual(calcular_media(10, 10, 10), 10)
    
    def test_media_valores_decimais(self):
        self.assertAlmostEqual(calcular_media(5.5, 6.5, 7.5), 6.5)

    def test_media_notas_diferentes(self):
        self.assertEqual(calcular_media(2, 8, 5), 5)

if __name__ == '__main__':
    unittest.main()
