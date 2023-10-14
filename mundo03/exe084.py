pessoas=list()
p=list()
pMenor=list()
pMaior=list()
maior=0
menor=1000

while True:
  p.append(str(input('Nome: ')))
  p.append(float(input('Peso: ')))
  pessoas.append(p[:])

  if len(pessoas)==1:
    menor=p[1]
    print(pessoas)

  if p[1] > maior:
    maior=p[1]
    pMaior.append(p[0])
  if p[1] < menor:
    menor=p[1]
    pMenor.append(p[0])
    print(menor, pMenor)

  p.clear()
  opc=str(input('Quer continuar? [S/N] ')).strip()
  if opc in 'nN':
    break

print(f'Ao todo você cadastrou {len(pessoas)} pessoas')

print(f'O maior peso foi de {maior}Kg. Peso de', end='')
for c in range (0, len(pMaior)):
  print(',',pMaior[c], end='')

print(f'\nO menor peso foi de {menor}Kg. Peso de', end='')
for i in range (1, len(pMenor)):
  print(',', pMenor[i], end='')

  