from tkinter import *

def drag_start(event):
    kotak = event.widget

    kotak.startX = event.x
    kotak.startY = event.y

def drag_motion(event):
    kotak = event.widget
    x = kotak.winfo_x() - kotak.startX + event.x
    y = kotak.winfo_y() - kotak.startY + event.y
    kotak.place(x=x,y=y)

window = Tk()

label = Label(window,bg="Green",width=10,height=5)
label.place(x=0,y=0)

label1 = Label(window,bg="Green",width=10,height=5)
label1.place(x=100,y=100)



label.bind("<Button-1>",drag_start)
label.bind("<B1-Motion>",drag_motion)

label1.bind("<Button-1>",drag_start)
label1.bind("<B1-Motion>",drag_motion)

window.mainloop()