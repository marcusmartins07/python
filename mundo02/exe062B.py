primeiro=int(input('Primeiro termo: '))
razao=int(input('Razão da PA: '))
count=0
termo=10

while termo!=0:
  while count < termo:
    print(' {} ->'.format(primeiro), end='')
    primeiro+=razao
    count+=1
  print(' Pausa')
  termo=int(input('Quantos termos você quer mostrar a mais: '))
  if termo==0:
    termo=0
  else:
    termo=termo+count
print('Progressão finalizada com {} termos'.format(count))