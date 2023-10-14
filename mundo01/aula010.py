tempo=int(input('Quantos anos tem seu carro: '))

if tempo <=3: 
    print('Carro novo')
else:
    print('carro velho')
print('-FIM-')

tempo=int(input('Quantos anos tem seu carro: '))
print('Carro novo'if tempo<=3 else'carro velho')
print('-FIM-')

nome=str(input('Qual seu nome? '))
if nome == 'Marcus':
  print('Que lindo nome')
print('Bom dia {}'.format(nome))