from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0
    
    # Metodo de classe ou estático
    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuários no sistema')

    #Metodo estático
    def definicao():
        return 'UXR344'

    # Metdodos de instância
    def __init__(self, nome, sobrenome, email, senha): # -> Construtor
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha = cryp.encrypt(senha, rounds=20000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    
    # metodo privado, pode ser usado somente dentro da classe
    def __gera_usuario(self):
        return self.__email.split('@')[0]
    
user1 = Usuario('Angelina', 'Jolie', 'angelinajolie@gmaill.com', '123456')

Usuario.conta_usuarios() #Forma correta
user1.conta_usuarios() # Possivel mas incorreta
    
"""nome = input('Informe seu nome: ')
sobrenome = input('Informe seu sobrenome: ')
email = input('Informe o e-mail: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirma a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else: 
    print('Senha não confere')
    exit(1)

print('Usuário criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha User Criptograda: {user._Usuario__senha}') # Acesso errado"""