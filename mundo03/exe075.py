c=par=0
n=(
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: '))
    )
    
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
  print(f'O valor 3 apareceu na {n.index(3)}° posição')
else:
  print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')
for c in n:
  if c %2==0:
    print(c, end=' ')