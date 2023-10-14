print('=====LOJA PRINCIPAL=====')
valorCompra = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[1] á vista dinheiro/pix')
print('[2] á vista cartão')
print('[3] 2X no cartão')
print('[4] 3x ou mais no cartão')
opc = int(input('Qual sua opção: '))

if opc==1:
  valorFinal = valorCompra-(valorCompra*0.10)
elif opc==2:
  valorFinal = valorCompra-(valorCompra*0.05)
elif opc==3:
  valorFinal = valorCompra
  valorParcela = valorFinal/2
  print('Sua compra será parcelada em 2X de {} sem juros'. format(valorParcela))
elif opc==4:
  parcela=int(input('Número de parcelas: '))
  valorFinal = valorCompra*1.20
  valorParcela = valorFinal/parcela
  print('Sua compra será parcelada em {}X de {} com juros'. format(parcela, valorParcela))

print('Sua compra de {} vai custar {} no final'.format(valorCompra, valorFinal))