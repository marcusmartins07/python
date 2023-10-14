termo=int(input('Quantos termos você quer mostrar? '))
count=fiboa=fiboc=0
fibob=1

while termo>count:
  print(' {} ->'.format(fiboa), end='')
  fiboc=fiboa+fibob
  fiboa=fibob
  fibob=fiboc
  count+=1
print(' FIM')  