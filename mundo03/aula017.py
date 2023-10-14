num = [2, 5, 9, 1] #lista
num[2]=3 #modificando valor na lista
num.append(7) #adicionando valor
num.sort(reverse=True) #organizando de forma decrescente 
print(num)
print(f'Essa lista tem {len(num)} elementos')

num.insert(3, 7) # inseri um numero (posição, valor)
print(num)
num.pop(1) #elimina o ultimo número, posso definir a posição ou não
print(num)
num.remove(7) #remove sómente um elemento
print(num)

if 4 in num:
  num.remove(4)
else:
  print('Não achei o numero 4')

valores = [] # adicionando valores
for cont in range (0, 3):
  valores.append(input('Digite um valor: '))

for c, v in enumerate(valores): # enumerando valores
  print(f'Na posição {c} encontrei o valor {v}')
print('Fim')

b = valores # atribuindo
b[2] = 8
print(f'Lista a: {valores}')
print(f'Lista b: {b}')

c= [3, 5, 9, 1]

b = c[:] # copiando valores sem relacionar
print(b)