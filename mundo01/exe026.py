frase=str(input('Digite uma frase: ')).lower()

print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A letra A aparece na posição {}.'.format(frase.find('a')))
print('A ultima letra A aparece na posição {}.'.format(frase.rfind('a')))