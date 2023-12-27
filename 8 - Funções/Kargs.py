# **kwargs = exige parametros nomeados e transforma parametros extra em dicionários

def cores_favoritas (**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernada='azul', vanessa='branco')

# Os parâmetro *args e **kargs não são obrigatórios

cores_favoritas()
cores_favoritas(geek='navy')

"""
Ordem da função
- Parametro obrigatório
- *args
- Parâmetro default (não obrigatórios):
- **kwargs
"""
def minha_funcao (idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)



