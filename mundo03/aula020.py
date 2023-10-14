def soma(a, b):
  print(f'A = {a} e B = {b}')
  result = a + b
  print(f'A soma de A + B = {result}') 

soma(a=2, b=3)
soma(5, 7)

print(' ')
#numero indefinido de parametros
def contador(*num):
  for valor in num:
    print(f'{valor}', end=' ')
  print('FIM!')

contador(2, 1, 7)
contador(4, 4, 7, 6, 2)
