num=[[], []]

for c in range(1,8):
  n=int(input(f'Digite o {c}° valor: '))

  if n%2==0:
    num[0].append(n)
  else:
    num[1].append(n)

num[0].sort()
num[1].sort()

print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')

# 9 1 5 6 8 3 2