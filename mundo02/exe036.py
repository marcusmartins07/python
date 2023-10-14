valorCasa = float(input('Valor da casa: R$'))
salComp = float(input('Salário do comprador: R$'))
tempo = int(input('Quantos anos de financiamento? '))

prest = (valorCasa/(tempo*12))

if prest<(salComp*0.3):
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado!')

print('Para pagar uma casa de R${} em {} anos e a prestação será de R$ {:.2F}'.format(valorCasa, tempo, prest))