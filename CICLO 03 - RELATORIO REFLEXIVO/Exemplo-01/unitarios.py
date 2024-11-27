import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_soma(self):
        self.assertEqual(self.calc.soma(2, 3), 5)

    def test_subtrai(self):
        self.assertEqual(self.calc.subtrai(3, 2), 1)

    def test_multiplica(self):
        self.assertEqual(self.calc.multiplica(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        with self.assertRaises(ValueError):
            self.calc.divide(6, 0)

if __name__ == '__main__':
    unittest.main()


