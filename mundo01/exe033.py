n1=int(input('Primeiro valor: '))
n2=int(input('Segundo valor: '))
n3=int(input('Terceiro valor: '))

if n1>n2 and n1>n3:
    maior=n1
else:
    if n2>n3 and n2>n3:
        maior=n2
    else:
        maior=n3

if n1<n2 and n1<n3:
    menor=n1
else:
    if n2<n3 and n2<n3:
        menor=n2
    else:
        menor=n3

print('Maior valor {}'.format(maior))
print('Menor valor {}'.format(menor))