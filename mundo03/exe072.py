numero=('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
n=0

while True:
    n=int(input('Digite um numero entre 0 e 10: '))
    if n<=10 and n>=0:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o numero {numero[n]}')