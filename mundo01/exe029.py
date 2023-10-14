v=float(input('Qual é a velocidade atual do carro? '))

if v>80:
    multa=((v-80)*7)
    print('Voce deve pagar uma multa de R${}'.format(multa))
else:
    print('Você não foi multado')