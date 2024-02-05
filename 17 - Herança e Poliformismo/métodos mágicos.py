"""
POO - Métodos Mágicos = todos os metodos que utilizam dunder

dunder repr (__repr__) ou (__str__) = Representação do objeto
"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return self.titulo

    def __str__(self):
        return self.titulo
    
    def __len__(self):
        return self.paginas
    
    def __add__(self, outro):
        return f'{self} - {outro}'

livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)

print(livro1)
print(len(livro1))

print(livro2)
print(len(livro2   ))


print(livro1 + livro2)

