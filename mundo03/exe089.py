# Preciso terminar

turmaAlunos=list()


while True:
  nome=str(input('Nome: '))
  na=float(input('Nota 1: '))
  nb=float(input('Nota 2: '))

  opc=str(input('Quer continuar? [S/N] ')).strip()
  if opc in 'nN':
    break