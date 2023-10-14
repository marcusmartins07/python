import random
from time import sleep

print('Suas opções:')
print('[1] PEDRA')
print('[2] PAPEL')
print('[3] TESOURA')

jj = int(input('Escolha sua jogada: '))
jc = random.randint(1, 3)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('-='*13)

if jc==1:
  print('Computador jogou PEDRA')
elif jc==2:
  print('Computador jogou PAPEL')
elif jc==3:
  print('Computador jogou TESOURA')

if jj==1:
  print('Jogador jogou PEDRA')
elif jj==2:
  print('Jogador jogou PAPEL')
elif jj==3:
  print('Jogador jogou TESOURA')

print('-='*13)
print('===RESULTADO===')

if jj==jc:
  print('EMPATOU')
elif jj==1 and jc==2 or jj==3 and jc==1 or jj==2 and jc==3:
  print('COMPUTADOR GANHOU')
else:
  print('JOGADOR GANHOU')
