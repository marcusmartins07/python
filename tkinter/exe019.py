from tkinter import *

root = Tk()
root.title('Login')

Label(root, width=20, bg='red').grid(column=0)
Label(root, width=20, bg='blue').grid(column=1)
Label(root, width=20, bg='orange').grid(column=2)
Label(root, width=40, bg='green').grid(columnspan=3, sticky='we')



root.mainloop()