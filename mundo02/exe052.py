n = int(input('Digite um número: \033[32m'))
cont=0

for c in range(1, n+1):
  if n%c==0:
    print('\033[32m', c, end=' ')
    cont+=1  
  else:
    print('\033[31m', c, end=' ')
print('\033[37m\nO numero {} foi divisivel {}X'.format(n, cont))

if cont==2:
  print('E por isso é um número primo')
else:
  print('E por isso não é um número primo')