n=count=result=0
while n!=999:
    n=int(input('Digite um número [999 para parar]: '))
    if n!=999:
        result=result+n
        count+=1

print('Você digitou {} números e a soma entre eles foi {}'.format(count,result))