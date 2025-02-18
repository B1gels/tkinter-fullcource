from tkinter import *
import time

WIDTH   = 500
HEIGHT  = 500

xVelocity = 2
yVelocity = 3

window = Tk()
window.title("space animation")
window.resizable(False,False)

myImage = PhotoImage(file="asset\\ufo.png")
background = PhotoImage(file="asset\\space.png")

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

background_space = canvas.create_image(0,0,image=background)
ufo = canvas.create_image(0,0,image=myImage,anchor=NW)

ufo_width  = myImage.width()
ufo_height = myImage.height()  

while True:
    coordinate = canvas.coords(ufo)
    print(coordinate)
    if coordinate[0] >= (WIDTH-ufo_width) or coordinate[0] < 0:
        xVelocity = -xVelocity
    if coordinate[1] >= (HEIGHT-ufo_height) or coordinate[1] < 0:
        yVelocity = -yVelocity
    
    canvas.move(ufo,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)



window.mainloop()