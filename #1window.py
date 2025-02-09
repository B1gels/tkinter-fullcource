from tkinter import *

# window = sebagai penampung untuk membuat widgets
# widgets = Gui elements: buttons,textBoxes,label,images

window = Tk()
window.geometry("420x420")
window.title("Fikar first GUI program")



icon = PhotoImage(file="asset\\mainLogo.png")
window.iconphoto(True,icon)
window.config(background="#ffffff")



window.mainloop()