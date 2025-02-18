from tkinter import *
from ball import *
import time

window = Tk()
window.title("multiple animation")

WIDTH  = 500
HEIGHT = 500

myBall = Canvas(window,width=WIDTH,height=HEIGHT)
myBall.pack()

volleyBall  = ball(myBall,0,0,100,1,1,"White")
tenisBall   = ball(myBall,0,0,50,2,3,"Green")
myBalls     = ball(myBall,0,0,150,4,3,"Pink")

while True:
    myBalls.move()
    tenisBall.move()
    volleyBall.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
