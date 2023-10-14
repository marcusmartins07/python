km=float(input('Digite a distância da sua viagem: '))

if km<200:
    valor=km*0.5
else:
    valor=km*0.45

print('O preço da pasagem será R$ {}'.format(valor))