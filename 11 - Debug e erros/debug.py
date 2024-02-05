
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema {err}'

print(dividir(4, 7))

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()

nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)


"""
COMANDOS PDB
l - Listar onde estamos no código
n - próxima linha
p - imprime variável
c - continua a execução
"""
