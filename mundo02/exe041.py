from datetime import date

anoNasc = int(input('Ano de nascimento: '))

anoAtual = date.today().year
idade = anoAtual-anoNasc

print('O atleta tem {} anos'.format(idade))

if idade<10:
    print('CLASSIFICAÇÃO: Mirim')
elif idade<15:
    print('CLASSIFICAÇÃO: Infantil')
elif idade<20:
    print('CLASSIFICAÇÃO: Junior')
elif idade<26:
    print('CLASSIFICAÇÃO: Senior')
elif idade>25:
    print('CLASSIFICAÇÃO: Master')
    
