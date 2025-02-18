from tkinter import *
from tkinter import ttk

window = Tk()

noteBook = ttk.Notebook(window) #widget yang mengatur sekumpulan widget yang berada dalam windows/display

tab1 = Frame(noteBook) #frame baru untuk tab 1
tab2 = Frame(noteBook) #frame baru untuk tab 2

noteBook.add(tab1,text='tab 1')
noteBook.add(tab2,text='tab 2')
noteBook.pack(expand=True,fill="both") #expand = mengisi ruang yang tidak terpakai
                                       #fill = mengisi ke arah x atau y bahkan bisa keduanya [both]

Label(tab1,text="ini adalah text untuk tab 1",width=50,height=25).pack()
Label(tab2,text="ini adalah text untuk tab 2",width=50,height=25).pack()


window.mainloop()