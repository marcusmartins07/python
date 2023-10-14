from random import randint
from time import sleep

numeros=list()
par=list()

def somaPar(*pares):
  print('\nSomando os valores pares,', end=' ')
  for k in pares:
    print(k, end=' ')
  print(f'temos a soma {sum(par)}')
  par.clear()

def geraMaior(limitador):
  print(' ')
  maior=0
  i=0
  for i in range(0,limitador):
    n=randint(1,9)
    numeros.append(n)
    if n%2==0:
      par.append(n)
  print('Analisando os valores passados...')
  for num in numeros:
    if num>maior:
      maior=num
    print(num, end=' ')
    sleep(0.2)
  print(f'Foram informados {len(numeros)} ao todo.')
  print(f'O maior valor informado foi {maior}')
  somaPar(par)
  numeros.clear()

  
for r in range (0, 5):
  c=randint(1,9)
  geraMaior(c)
  c=0


