from tkinter import *

root = Tk()
root.title('Login')

# funções 
def executar():
    la['text']=t1.get()
    lb['text']=t2.get()
    lc['text']=t3.get()

# widgets
t1 = Entry(root)
t2 = Entry(root)
t3 = Entry(root)
la = Label(root)
lb = Label(root)
lc = Label(root)
b = Button(root, text='Executar', command=executar)

# layout
t1.grid()
t2.grid()
t3.grid()
la.grid()
lb.grid()
lc.grid()
b.grid()

t1.focus()

root.mainloop()