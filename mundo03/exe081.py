num = list()

while True:
  n=num.append(input('Digite um valor: '))
  opc=str(input('Quer continuar? [S/N] ')).strip()
  if opc in 'Nn':
    break

num.sort(reverse=True)
print(f'Você digitou {len(num)} elementos')
print(f'Os valores em ordem decrescente são {num}')
if '5' not in num:
  print('O valor 5 não faz parte da lista')
else:
  print('O valor 5 faz parte da lista')


# 7 2 5 9 1 