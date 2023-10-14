from time import sleep

def contagem(inicio, fim, passo):
  print('=-'*15)
  print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')

  if inicio>fim:
    passo=-passo
    fim=-2
  
  for c in range (inicio, fim+1, passo):
    print(c, end=' ')
    sleep(0.25)
  print(' ') 

contagem(1,10,1)
contagem(10,0,2)

print('=-'*15)
numa=int(input('\nInicio: '))
numb=int(input('Fim: '))
numc=int(input('Passo: '))

contagem(numa, numb, numc)