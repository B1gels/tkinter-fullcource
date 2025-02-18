#move image with canvas
from tkinter import *

def move_up(event):
    print('kamu menekan : ',event.keysym)
    canvas.move(mobilbalap,0,-10)

def move_down(event):
    canvas.move(mobilbalap,0,10)
    print('kamu menekan : ',event.keysym)

def move_left(event):
    print('kamu menekan : ',event.keysym)
    canvas.move(mobilbalap,-10,0)

def move_right(event):
    print('kamu menekan : ',event.keysym)
    canvas.move(mobilbalap,10,0)


window = Tk()
#keybind
window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

#arrowbind
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

mobil = PhotoImage(file='asset\\mobil.png')

canvas = Canvas(window,width=500,height=500)
canvas.pack()

mobilbalap = canvas.create_image(0,0,image=mobil,anchor=NW)


window.mainloop()