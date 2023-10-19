from tkinter import *

root = Tk()

img = PhotoImage(file='C://Users/Marcus Martins/Documents/Estudos/python publico/python/tkinter/images/MarioGrande.png')

label_imagem = Label(root, image=img).pack()

root.mainloop() 