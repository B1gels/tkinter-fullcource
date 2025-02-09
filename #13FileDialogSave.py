from tkinter import *
from tkinter import filedialog

def saveButton():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\ACER\\OneDrive\\Desktop\\python_from_zero_to_hero\\Tkinter\\Tutorial",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("file text",".txt"),
                                        ("HTML File",".html"),
                                        ("All Files",".*")
                                    ])
     
    if file is None: #error handleing jika user membatalkan save file
        return None

    # fileText = str(textArea.get(1.0,END)) #untuk mendapatkan value dari textWidget
    fileText = input("ketikkan sesuatu : ") # cara alternative untuk mendapatkan value dari terminal
    file.write(fileText)
    file.close()

window = Tk()

button = Button(window,text="save",command=saveButton)
button.pack()

textArea = Text(window)
textArea.pack()


window.mainloop()