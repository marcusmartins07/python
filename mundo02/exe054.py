from datetime import date

anoAtual = date.today().year
maiorIdade = anoAtual-18
contMaior=0
contMenor=0

n=int(input('Numero de pessoas que será analisado: '))

for c in range (1, n+1):
    ano=int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    
    if ano >= maiorIdade:
        contMaior=contMaior+1
    else:
        contMenor=contMenor+1
print('Ao todo tivemos {} pessoas maiores de idade'.format(contMaior))
print('E também tivemos {} pessoas menores de idade'.format(contMenor))