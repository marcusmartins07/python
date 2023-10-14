contMaior=0

n=int(input('Numero de pessoas que será analisado: '))

contMenor=float(input('Peso da 1° pessoa: '))
peso=contMenor

for c in range (2, n+1):
    if peso > contMaior:
        contMaior=peso
    elif peso < contMenor:
        contMenor=peso
    peso=float(input('Peso da {}° pessoa: '.format(c)))
print('O maior peso lido foi de {}Kg'.format(contMaior))
print('O menor peso lido foi de {}Kg'.format(contMenor))