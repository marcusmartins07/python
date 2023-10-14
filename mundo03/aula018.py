pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(pessoas)
print(pessoas[0][0]) #Pedro
print(pessoas[1][1]) #19
print(pessoas[2][0]) #João
print(pessoas[1]) #['Maria', 19]

for p in pessoas:
  print(f'{p[0]} tem {p[1]} de idade')

teste = list()
teste.append('Gustavo')
teste.append(40)
pessoas= list()
pessoas.append(teste[:])
teste[0]='Maria'
teste[1]=22
pessoas.append(teste[:])
print(teste)
print(pessoas)