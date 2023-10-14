import random

print('Os numero sorteados foram: ', end='')
numero=(random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))

for n in numero:
    print(n, end=' ')
print(f'\nO maior valor sorteado foi {max(numero)}')
print(f'O menor valor sorteado foi {min(numero)}')