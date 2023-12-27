from collections import Counter

lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 66, 66, 43, 44, 34]

res = Counter(lista)

print(type(res))
print(res)

print(Counter('Marcus Martins'))

texto = """ Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et mauris pharetra 
turpis laoreet condimentum. Curabitur vestibulum nulla quis diam commodo, sed cursus lectus 
placerat. Cras vitae nisi a lorem laoreet accumsan. Curabitur lacus nisl, lobortis sed magna nec, 
aliquet auctor eros. Vivamus eget semper purus. Sed elementum rutrum dolor eget maximus. Nullam nec 
dolor eleifend, gravida elit ut, varius est. Sed id dui eros. Proin commodo velit augue, luctus
condimentum ex efficitur vitae. Pellentesque eu neque auctor, viverra erat lacinia, ultrices mauris.
Proin eu mauris purus. """

palavras = texto.split()
#print(palavras) 

res = Counter(palavras)

print(res)