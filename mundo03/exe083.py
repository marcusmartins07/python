expressao=str(input('Digite sua expressão: '))
aspasEsquerda=aspasDireita=0

for c in range(0, len(expressao)):
  if expressao[c] == '(':
    aspasEsquerda+=1
  if expressao[c] == ')':
    aspasDireita+=1

print(aspasEsquerda)
print(aspasDireita)

if aspasEsquerda==aspasDireita:
  print('Expressão está correta')
else:
  print('Expressão está incorreta')

# ((a+b)*c)(x+y(3+2/3)*z)