c=1
while c<5:
	print(c)
	c+=1
print('fim')

r = 's'
while r == 's':
    n=int(input('Digite um valor: '))
    r=str(input('Quer continuar? [S/N] '))
print('fim')

n=1
par=impar=0
while n !=0:
    n=int(input('Digite um numero: '))
    if n != 0:
        if n%2 == 0:
            par+=1
        else:
            impar+=1
print('Você digitou {} numeros pares e {} numeros impares'.format(par, impar))