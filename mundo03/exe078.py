valores=[]
maior=menor=0

for c in range(0,5):
  valores.append(int(input(f'Digite um valor para posição {c}: ')))
  if (valores[c])==(valores[0]):
    menor=valores[0]
    print(f'Menor valor declarado {menor}')
  
  if (valores[c])>(maior):
    maior=valores[c]
    print(f'O maior numero é {maior}')  
  
  if (valores[c])<(menor):
    menor=valores[c]
    print(f'O menor numero é {menor}') 
  
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
  if valores[i]==maior:
    print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
  if valores[i]==menor:
    print(f'{i}... ', end='')

# 1 8 3 8 1