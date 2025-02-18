from tkinter import *

def doSomething(event): #dibutuhkan parameter event
    # print("kau menekan : " + event.keysym)
    label.config(text=event.keysym)

window = Tk()

window.bind("<Key>",doSomething) #digunakan untuk melakukan keyEvent atau mouse | argumennya hanya duar {event} dan {function}
label = Label(window,font=("Helvetica",100))
label.pack()


window.mainloop()