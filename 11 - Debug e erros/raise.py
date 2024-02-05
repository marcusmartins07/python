# raise = lança exceções, cria mensagens de erro

# não é uma função, é uma palavra reservada como def

# raise ValueError('Valor incorreto')

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek', 'Azul')

# colore(True, 'Verde')

# colore('Geek', 1)