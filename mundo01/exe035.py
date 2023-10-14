n1=float(input('Primeiro segmento: '))
n2=float(input('Segundo segmento: '))
n3=float(input('Terceiro segmento: '))

if (n1+n2)>n3 and (n2+n3)>n1 and (n1+n3)>n2:
    print('Os segmentos podem formar um trinagulo')
else:
    print('Os segmentos NÂO podem formar um trinagulo')