lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche)
print(lanche[1])
print(lanche[2:])

# TUPLAS SÃO IMUTÁVEIS
# lanche[1] = 'Refrigerante' = não é possível

for c in range (0, len(lanche)):
  print(f'Eu vou comer {lanche[c]}')
print('Comi pra caramba')

for comida in lanche:
  print(f'Não vou comer {comida}')

for pos,comida in enumerate(lanche):
  print(f'Comi {comida} na posição {pos}')

print(sorted(lanche)) # ordenado

a=(2, 5, 4)
b=(5, 8, 1, 2)
c=b+a
print(c)
print(len(c))
print(c.count(5)) #conta quantos numeros tem
print(c.index(2)) # mostra a posição

pessoa=('Marcus', 39, 'm', 79.76)
print(pessoa)
#del(pessoa) #exclui tupla
