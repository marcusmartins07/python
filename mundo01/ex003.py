n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
name=str(input('Digite seu nome: '))

soma=n1+n2
sub=n1-n2

print ('Ola {}, tudo bem?'.format(name))
print('A soma é',soma)
print('A subtração é {}'.format(sub))

print(type(n1))

""" int, float, bool e str """

print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
print ('A soma entre',n1,'e',n2,'vale',soma)