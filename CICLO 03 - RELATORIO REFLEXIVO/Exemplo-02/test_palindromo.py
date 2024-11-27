import unittest
from palindromo import Palindromo

class TestPalindromo(unittest.TestCase):
    def test_palindromo_simples(self):
        p = Palindromo()
        self.assertTrue(p.is_palindromo("radar"))
        self.assertFalse(p.is_palindromo("python"))
    
    def test_palindromo_com_espacos(self):
        p = Palindromo()
        self.assertTrue(p.is_palindromo("a man a plan a canal panama")) 

    def test_palindromo_maiusculas(self):
        p = Palindromo()
        self.assertTrue(p.is_palindromo("Radar")) 

    def test_palindromo_com_caracteres_especiais(self):
        p = Palindromo()
        self.assertTrue(p.is_palindromo("A man, a plan, a canal: Panama!"))

if __name__ == "__main__":
    unittest.main()
