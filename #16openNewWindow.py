from tkinter import *


def create_window():
    global new_window
    # newWindow = Toplevel() #membuat jendela baru yang berada di atas jendela lain,tersambung dengan jendela dibawahnya (jendela utama)
    new_Window = Tk() #membuat jendela baru yang tidak terhubung dengan jendela manapun (berdiri sendiri)

    old_window.destroy() #menghapus jendela 

old_window = Tk()
new_window = None

Button(old_window,text="create new window",command=create_window).pack()

old_window.mainloop()