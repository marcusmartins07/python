palavra=(
  'aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
  'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro'
)

for p in palavra:
  print(f'\nNa palavra {p.upper()} temos', end='')
  for letra in p:
    if letra.lower() in 'aàáâãeéêiíìou':
      print(letra, end=' ')
