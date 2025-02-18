from tkinter import *

def doSomething(event):
    print(f"mouse klik coordinate : [{event.x},{event.y}]")

window = Tk()
window.geometry("200x200")
window.resizable(False,False)

window.bind("<Button-1>",doSomething)           #untuk mentrigger klik kiri
# window.bind("<Button-2>",doSomething)         #untuk mentrigger scroll atau tombol tengah
# window.bind("<Button-3>",doSomething)         #untuk mentrigger klik kanan
# window.bind("<ButtonRelease>",doSomething)    #ketriger saat button dilepas
# window.bind("<Enter>",doSomething)            #saat cursor masuk ke window
# window.bind("<Leave>",doSomething)            #saat cursor keluar dari window
window.bind("<Motion>",doSomething)             #saat cursor bergerak didalam window

window.mainloop()