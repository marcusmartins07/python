n=int(input('Digite um numero: '))

numero = str(n)

print('''
unidade: {}
dezena: {}
centena: {}
milhar: {}'''
.format(numero[3], numero[2], numero[1], numero[0]))