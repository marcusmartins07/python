from tkinter import *

root = Tk()
root.title('Conversor')

# funções 
def executar():
    f = float(temperaturaF.get())
    c = (f-32)*5/6
    final.set(str(round(c,1)) + ' graus Celsius')

final = StringVar()

# widgets
t1 = Label(root, text='Inserir Fahrenheit')
temperaturaF = Entry(root)
temperaturaC = Label(root, textvariable=final)
botao = Button(root, text='Executar', command=executar)

# layout
t1.grid()
temperaturaF.grid()
temperaturaC.grid()
botao.grid()

temperaturaF.focus()

root.mainloop()