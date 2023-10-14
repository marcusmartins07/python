s=' '
pessoasMaiores=homem=mulherVinte=0

while True:
  opc=' '
  idade=int(input('Idade: '))
  while s not in 'MF':
    s=str(input('Sexo: [M/F] ')).strip().upper()

  if idade>18:
    pessoasMaiores+=1
  if s == 'M':
    homem+=1
  elif idade<20:
    mulherVinte+=1
  s=' '

  while opc not in 'SN':
    opc=str(input('Quer continuar? [S/N] ')).strip().upper()
  if opc == 'N':
    break

print(f'Total de pessoas com mais de 19 anos: {pessoasMaiores}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulherVinte} mulheres com menos de 20 anos')
  
