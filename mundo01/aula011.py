
#       /-=style
# \033[X:XX:XXm
#	       |   \-= back
#	        \-= text

# exe.: \033[0:33:44m

# tyle = estilo de texto
# 0 = none
# 1 = bold
# 4 = underline
# 7 = negative 

# text = cor do texto
# 30 = branco
# 31 = vermelho
# 32 = verde
# 33 = amarelo
# 34 = azul
# 35 = roxo
# 36 = turquesa
# 37 = cinza

# back = cor de fundo
# 40 = branco
# 41 = vermelho
# 42 = verde
# 43 = amarelo
# 44 = azul
# 45 = roxo
# 46 = turquesa
# 47 = cinza

n1=10
n2=20
print('Os numeros são \033[32m{} e \033[31m{} para esta conta'.format(n1, n2))

nome='Marcus'

cores={
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'pretoebranco':'\033[7:30m'}

print('Ola! muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))