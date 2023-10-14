n=int(input('Digite um número para calcular o fatorial: '))
print('Calculando {}! = '.format(n),end='')

result=1

while n !=0:
  print('{}'.format(n), end='')
  print(' X ' if n>1 else ' = ', end='')
  result=result*n
  n-=1
print(result)