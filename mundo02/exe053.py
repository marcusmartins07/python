frase = str(input('Digite uma frase: ')).strip().upper()

palavras=frase.split()
junto = ''.join(palavras)
inverso=''

for letra in range(len(junto)-1, -1, -1):
  inverso=inverso+junto[letra]
print('O inverso de {} é {}'.format(junto,inverso))
if junto==inverso:
  print('Temos um palindromo')
else:
  print('A frase digitada não é um palindromo')

  # APOS A SOPA
  # A SACADA DA CASA