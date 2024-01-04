
# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler
# Da mesma forma, se abrirmo um arquivo para escrita, não podemos lê-lo, somente escrever nele.

""" Abrindo um arquivo com modo 'w', se o arquivo não existir será criado,
caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma, todo
o conteúdo no arquivo anterior é perdido
"""


with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em um arquivo.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos\n')
    arquivo.write('Ultima linhas\n')

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

    