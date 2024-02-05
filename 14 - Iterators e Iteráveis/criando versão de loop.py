def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for('Geek University')
numeros = [1, 2, 3, 4, 5]
meu_for(numeros)