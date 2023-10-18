from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Exercício 16')
#menu_inicial.geometry("500x500")

label_a = Label (menu_inicial, text='Label 1', font='Arial 20', bg='red')
label_b = Label (menu_inicial, text='Label 2', font='Arial 20', bg='green')
label_c = Label (menu_inicial, text='Label 3', font='Arial 20', bg='blue')

btn_a = Button(menu_inicial, text='Botão 1')
btn_b = Button(menu_inicial, text='Botão 2')
btn_c = Button(menu_inicial, text='Botão 3')

#label_a.pack()
#label_b.pack()

label_a.grid(row=0, column=0)
label_b.grid(row=0, column=1)
label_c.grid(row=0, column=2)

btn_a.grid(row=1, column=0)
btn_b.grid(row=1, column=1)
btn_c.grid(row=1, column=2)

menu_inicial = mainloop()