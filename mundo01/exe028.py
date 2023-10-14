import random
n1=int(input('Adivinhe um número entre 0 e 5: '))

n2 = random.randint(0, 5)
print(n2)

if n1==n2:
  print('Você adivinhou o numero')
else:
  print('Você errou')
