opc=''
n=maior=0
count=1
media=0

n=int(input('Digite um número: '))
opc=str(input('Quer continuar? [S/N] ')).strip().upper()
menor=soma=n


while opc != 'N':
  n=int(input('Digite um número: '))
  opc=str(input('Quer continuar? [S/N] ')).strip().upper()
  count+=1
  soma+=n
  
  if n>maior:
    maior=n
  elif n<menor:
    menor=n

media=soma/count
print('Você digitou {} numeros e a media foi {}'.format(count, media))
print('O maior valor {} foi e o menor {}'.format(maior, menor))