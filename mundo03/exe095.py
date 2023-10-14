pessoa=[{'nome': 'Marcus', 'sexo': 'M', 'idade': 22},
 {'nome': 'Fernanda', 'sexo': 'F', 'idade': 23},
 {'nome': 'Gabriela', 'sexo': 'F', 'idade': 56}
 ]

print(f'C) As mulheres cadastradas foram ', end='')
for f in range (0, len(pessoa)):
  if pessoa[f]['sexo']=='F':
    print(pessoa[f]['nome'], end=' ')