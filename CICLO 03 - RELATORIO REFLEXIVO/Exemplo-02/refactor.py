import re 

class Palindromo:
    def is_palindromo(self, palavra):
        palavra_formatada = re.sub(r'[^a-zA-Z]', '', palavra).lower()
        return palavra_formatada == palavra_formatada[::-1]



