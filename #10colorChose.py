from tkinter import *
from tkinter import colorchooser #submodul


def click():
    color = colorchooser.askcolor()
    colorHex = color[1] #menyimpan nilai hex dari warna yang dipilih
    window.config(bg=colorHex) #akan mengubah warna background berdararkan warna yang kita pilih

window = Tk()
window.geometry("420x420")

button = Button(text="click me!",command=click)
button.pack()

window.mainloop()