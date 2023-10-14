valores=list()
par=list()
impar=list()

while True:
  n=valores.append(int(input('Digite um número: ')))
  
  if valores[-1]%2==0:
    par.append(valores[-1])
    print('par')
  else:
    impar.append(valores[-1])
    print('Impar')

  opc=str(input('Quer continuar? [S/N] ')).strip()
  if opc in 'Nn':
    break

print(f'A lista completa é {valores}')
print(f'A list de pares é {par}')
print(f'A lista de impar é {impar}')

# 7 9 2 6 8