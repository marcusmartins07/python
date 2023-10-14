num = list()

while True:
  n= int(input('Digite um valor: '))
  if n not in num:
    num.append(n)
    print('Valor adicionado com sucesso')
  else:
    print('Valor duplicado')

  
  opc=str(input('Quer continuar? [S/N] ')).strip()
  if opc in 'Nn':
    break

num.sort()
print(f'Você digitou os valores {num}')