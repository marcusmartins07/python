"""
Decoradores (Decorators)

- São funções
- Envolvem outras funções e aprimora seus comportamentos
- É High Order Functions
- Sintaxe própria usando @ (Syntact Sugar)

"""

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

apresentando()

# Decorator != decorator function

