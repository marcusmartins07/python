import random
numeros=list()
n=0

n=int(input('Quantos jogos você quer que eu sorteie? '))

for c in range(0, n):
  for i in range(0, 6):
    numeros.append(random.randint(1, 60))
  
  
  print(f'Jogo {c}: {numeros}')
  numeros.clear()
print('Boa sorte')