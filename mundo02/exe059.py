n1=int(input('Primeiro número: '))
n2=int(input('Segundo número: '))
opc=0
result=0

while opc != 5 or not '1,2,3,4':
    print(' ')
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    opc=int(input('Escolha uma opção: '))
    
    if opc==1:
        result=n1+n2
        print('A soma entre {} + {} é {}'.format(n1,n2,result))
    elif opc==2:
        result=n1*n2
        print('O resultado de {} X {} é {}'.format(n1,n2,result))
    elif opc==3:
        if n1>n2:
            print('Entre {} e {} o maior valor é {}'.format(n1,n2,n1))
        else:
            print('Entre {} e {} o maior valor é {}'.format(n1,n2,n2))
    elif opc==4:
        n1=int(input('Primeiro número: '))
        n2=int(input('Segundo número: '))
    elif opc != 5 or not '1,2,3,4':
        print('Opção inválida. Tente novamente')

print('Finalizando...')