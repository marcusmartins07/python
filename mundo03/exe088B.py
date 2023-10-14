import random
numeros=list()
n=cont=0

num=int(input('Quantos jogos você quer que eu sorteie? '))

for c in range(0, num):
  
  while True:
    n=random.randint(1, 60)
    if n not in numeros:
      numeros.append(n)
      cont+=1
      if cont==6:
        break
  
  numeros.sort()
  print(f'Jogo {c}: {numeros}')
  numeros.clear()
  cont=0
print('Boa sorte')