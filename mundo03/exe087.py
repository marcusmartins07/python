matriz=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar=somaTerceira=maior=0

for l in range (0, 3):
  for c in range (0, 3):
    matriz[l][c]=int(input(f'Digite um valor: [{l}, {c}] '))
    
    if matriz[l][c]%2==0:
      somaPar+=matriz[l][c]

    somaTerceira+=matriz[l][2]

    if matriz[1][c] > maior:
      maior=matriz[1][c]


for l in range (0, 3):
  for c in range (0, 3):
    print(f'[{matriz[l][c]:^5}]', end='')
  print()

print(f'A soma dos valores pares é {somaPar}')
print(f'A soma dos valores da terceira coluna é {somaTerceira}')
print(f'O maior valor da segunda linha é {maior}')

