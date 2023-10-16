from tkinter import *

menu_incial=Tk()
menu_incial.title('Label')

label_a = Label(menu_incial, text='Este é o label 1')
label_b = Label(menu_incial, text='Este é o label 2')
button_a = Button(menu_incial, text='Executar')

# pack define a ordem que sera mostrado os objetos
label_b.pack()
label_a.pack()
button_a.pack()

menu_incial.mainloop()
