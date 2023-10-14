import random
count=0
poui=' '

while True:
  playerNum=int(input('Digite um valor: '))
  while poui not in 'PI':
    poui=str(input('Par ou Impar? [P/I] ')).strip().upper()
  pcNum=random.randint(1,10)
  totalNum=playerNum+pcNum
  
  if totalNum%2==0:
    result='PAR'
  else:
    result='IMPAR'
  
  print(f'Você jogou {playerNum} e o computador {pcNum}. Total de {totalNum} é {result}')

  if poui == 'I':
    if result == 'IMPAR':
      print('Você venceu!')
      count+=1
    else:
      print('PERDEU')
      break
  elif poui == 'P':
    if result == 'PAR':
      print('Você venceu!')
      count+=1
    else:
      print('PERDEU')
      break
  poui=' '

print(f'GAME OVER! Você venceu {count} vezes')
