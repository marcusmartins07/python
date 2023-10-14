import random
num=int(input('Adivinhe um numero entre 1 e 10: '))
n=random.randint(1, 10)
print(n)
count=0

while n != num:
    num=int(input('Tente mais uma vez: '))
    count+=1
print('Você acertou com {} tentativas'.format(count))