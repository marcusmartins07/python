from datetime import date
anoNasc = int(input('Ano de nascimento: '))

anoAtual = date.today().year
idade = anoAtual-anoNasc

print('Quem nasceu em {} tem {} anos em {}'.format(anoNasc, idade, anoAtual))

if idade<18:
    alistamento= 18-idade
    if alistamento == 1:
        print('Ainda falta 1 ano para o alistamento')
        print('Seu alistamento será em {}'.format(anoAtual+1))
    else:
        print('Ainda falta {} anos para o alistamento'.format(alistamento))
        print('Seu alistamento será em {}'.format(anoNasc+18))
elif idade>18:
    alistamento= idade-18
    if alistamento == 1:
        print('Você ja deveria ter se alistado há um ano')
        print('Seu alistamento foi em {}'.format(anoAtual-1))
    else:
        print('Você já deveria ter se alistado há {} anos'.format(idade-18))
        print('Seu alistamento foi em {}'.format(anoAtual-(idade-18)))
elif idade==18:
    print('Você tem que se alistar imediatamente')