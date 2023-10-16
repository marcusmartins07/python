from tkinter import *

menu_inicial = Tk()
menu_inicial.geometry('500x300')
menu_inicial.title('Exercicio 11')

label_a = Label(menu_inicial, 
                text='Frase 1\nsolid',
                font='Arial 20',
                bd=5,
                relief='solid'
).pack()

label_b = Label(menu_inicial, 
                text='flat',
                font='Arial 20',
                bd=5,
                relief='flat'
).pack()

label_b = Label(menu_inicial, 
                text='groove',
                font='Arial 20',
                bd=5,
                relief='groove'
).pack()

label_b = Label(menu_inicial, 
                text='raised',
                font='Arial 20',
                bd=5,
                relief='raised'
).pack()

label_b = Label(menu_inicial, 
                text='ridge',
                font='Arial 20',
                bd=5,
                relief='ridge'
).pack()

label_b = Label(menu_inicial, 
                text='sunken',
                font='Arial 20',
                bd=5,
                relief='sunken'
).pack()



menu_inicial = mainloop()