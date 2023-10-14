cinquenta=dez=vinte=um=0
n=int(input('Qual valor você quer retirar? R$ '))
while True:
  if n!=0:
    while n>49:
      n=n-50
      cinquenta+=1
    print(f'Total de {cinquenta} cedulas de R$50')
  if n!=0:
    while n>19:
      n=n-20
      vinte+=1
    print(f'Total de {vinte} cedulas de R$20')
  if n!=0:
    while n>9:
      n=n-10
      dez+=1
    print(f'Total de {dez} cedulas de R$10')
  if n!=0:
    while n>0:
      n=n-1
      um+=1
    print(f'Total de {um} cedulas de R$1')
  else:
    break



