from datetime import datetime
pessoa=dict()

pessoa['nome']=str(input('Nome: '))
nasc=int(input('Ano de nascimento: '))
pessoa['ctps']=int(input('Carteira de Trabalho (0 não tem):'))
if pessoa['ctps']!=0:
  pessoa['contratação']=int(input('Ano de contratação:'))
  pessoa['salario']=int(input('Salário: R$'))

pessoa["idade"]=datetime.now().year-nasc
pessoa["aposentadoria"]=pessoa['idade']+((pessoa["contratação"]+23)-datetime.now().year)

print(f'Nome tem o valor {pessoa["nome"]}')
print(f'Idade tem o valor {pessoa["idade"]}')

if pessoa['ctps']!=0:
  print(f'ctps tem o valor {pessoa["ctps"]}')
  print(f'contratação tem o valor {pessoa["contratação"]}')
  print(f'salário tem o valor {pessoa["salario"]}')
  print(f'Aposentadoria tem o valor {pessoa["aposentadoria"]}')

else:
  print(f'ctps tem o valor {pessoa["ctps"]}')