from random import randint
from time import sleep

numeros=list()

def geraMaior(limitador):
  maior=0
  i=0
  for i in range(0,limitador):
    n=randint(1,9)
    numeros.append(n)
  print('Analisando os valores passados...')
  for num in numeros:
    if num>maior:
      maior=num
    print(num, end=' ')
    sleep(0.2)
  print(f'Foram informados {len(numeros)} ao todo.')
  print(f'O maior valor informado foi {maior}')
  numeros.clear()

  
for r in range (0, 5):
  c=randint(1,9)
  geraMaior(c)
  c=0


