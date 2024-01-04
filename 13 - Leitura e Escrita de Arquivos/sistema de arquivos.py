# Sistema de navegação utilizando OS

import os

print(os.getcwd()) # Imprime o diretorio atual

# mudar diretorio
os.chdir('..')
print(os.getcwd()) 
os.chdir('..')
print(os.getcwd()) 

# Checando diretorio absoluto ou relativo
print(os.path.isabs('C://Users/Marcus Martins/Documents/Estudos/python publico/python')) # True = Absoluto

#identificando sistema operacional
print(os.name) # posix = Linux ou Mac e nt = Windows

#Ir ate diretorio especifico

print(os.getcwd())
res = os.path.join(os.getcwd(), 'Estudos', 'python publico')

os.chdir(res)
print(os.getcwd())

#listar diretorios
res = os.path.join(os.getcwd(), 'python')
os.chdir(res)
print(os.listdir())

print(len(os.listdir())) # Quantidade de diretorios




