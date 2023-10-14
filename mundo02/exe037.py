n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[1] Converter para BÍNARIO')
print('[2] Converter para OCTAL')
print('[3] Converter para HEXADECIMAL')
opc = int(input('Sua opção: '))

if opc == 1:
    print('{} convertido para binário = {}'.format(n, bin(n)[2:]))
elif opc == 2:
    print('{} convertido para binário = {}'.format(n, oct(n)[2:]))
elif opc == 3:
    print('{} convertido para binário = {}'.format(n, hex(n)[2:]))