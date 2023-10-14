aluno=dict()

aluno['nome']=str(input('Nome: '))
aluno['media']=float(input(f'Média do {aluno["nome"]}: '))

print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')

if aluno['media']>=7:
  aluno['situacao']='Aprovado'
elif aluno ['media'] < 7 and aluno['media']>=5:
  aluno['situacao']='Recuperação'
elif aluno['media'] < 5:
  aluno['situacao']='Reprovado'


print(f'Situação é igual a {aluno["situacao"]}')