cadastro= {
  'nome':' ',
  'sexo':' ',
  'idade':' '
}
pessoa=list()
somaIdade=0

while True:
  # ZERANDO VARIAVEIS
  opc=' '
  cadastro['sexo']=' '
  
  # CADASTRO
  cadastro['nome']=str(input('Nome: '))
  while cadastro['sexo'] not in 'MF':
    cadastro['sexo']=str(input('Sexo: [M/F] ')).strip().upper()
    if cadastro['sexo'] not in 'MF':
      print('ERRO! Por favor, digite apenas M ou F')
  cadastro['idade']=int(input('Idade: '))
  pessoa.append(cadastro.copy())

  somaIdade+=cadastro['idade']

  print(pessoa)

  # OPÇÃO PARA CONTINUAR OU NÃO
  while opc not in 'SN':
    opc=str(input('Quer continuar? [S/N] ')).strip().upper()
    if opc not in 'SN':
      print('ERRO! Por favor, digite apenas S ou N')
  if opc in 'Nn':
    break

print(f'A) Ao todo temos {len(pessoa)} pessoas cadastradas.')
print(f'B) A média de idade é de {somaIdade/len(pessoa)} ano')

print(f'C) As mulheres cadastradas foram ', end='')
for f in range (0, len(pessoa)):
  if pessoa[f]['sexo']=='F':
    print(pessoa[f]['nome'], end=' ')

print(f'\nD) Lista de pessoas acima da média: ')

print(pessoa)
