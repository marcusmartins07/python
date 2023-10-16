from tkinter import *

menu_inicial = Tk()
menu_inicial.geometry('500x300')
menu_inicial.title('Exercicio 11')

label_a = Label(menu_inicial, 
                text='Este é o label 1',
                font='Arial 20',
                bg='red',
                width=20
                )
label_a.pack()

label_a = Label(menu_inicial, 
                text='Este é o label 2',
                font='Arial 40',
                bg='green',
                width=20
                )
label_a.pack()

menu_inicial = mainloop()