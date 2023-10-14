total=caro=0
prodBarato=' '

produto=str(input('Nome do produto: '))
preco=float(input('Preço: R$'))
barato=preco
set=0

while True:
  opc=' '
  if set==1:
    produto=str(input('Nome do produto: '))
    preco=float(input('Preço: R$'))
  set=1
  total+=preco
  if preco>1000:
    caro+=1
  if preco<=barato:
    barato=preco
    prodBarato=produto

  while opc not in 'SN':
    opc=str(input('Quer continuar? [S/N]')).strip().upper()
  if opc!='S':
    break

print(f'O total da compra foi de {total}')
print(f'Temos {caro} produtos custando mais que R$1000.00')
print(f'O produto mais barato foi {prodBarato} que custa R${barato}')
  