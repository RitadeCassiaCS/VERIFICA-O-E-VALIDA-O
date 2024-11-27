import unittest
from palindromo import Palindromo

class TestPalindromo(unittest.TestCase):
    def test_palindromo(self):
        p = Palindromo()
        self.assertTrue(p.is_palindromo("radar")) 
        self.assertFalse(p.is_palindromo("python")) 

if __name__ == "__main__":
    unittest.main()



