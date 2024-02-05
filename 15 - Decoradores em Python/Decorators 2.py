def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Ola, eu gostaria de {principal} acompanhado de {acompanhamento}, por favor.'

print(saudacao('Felicity'))

print(ordenar('Picanha', 'Batata Frita'))

#Decorator com parametro de entrada

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna
 
@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 * num2

# testando

print(soma_dez(10, 12))
print(soma_dez(1, 21))

print(comida_favorita('pizza', 'churrasco'))
print(comida_favorita('sanduiche', 'camarão'))