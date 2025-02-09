from tkinter import *

def openFile():
    print("File terbuka")

def saveFile():
    print("File Disimpan")

window = Tk()

fileIcon = PhotoImage(file="asset\\file.png")
saveIcon = PhotoImage(file="asset\\save.png")
exitIcon = PhotoImage(file="asset\\exit.png")

'''membuat file menu'''
menuBar = Menu(window) #membuat menu bar
window.config(menu=menuBar) #memasangkan menu bar ke jendela utama

'''membuat dropdown file menu'''
fileMenu = Menu(menuBar,tearoff=0,font=("MV Boli",10))  #membuat file menu 
menuBar.add_cascade(label="File",menu=fileMenu)         #menambahkan file menu kedalam menu bar
fileMenu.add_command(label="Open",command=openFile,image=fileIcon,compound=LEFT) #menambahkan dropdown yang dapat melakukan seuatu
fileMenu.add_command(label="Save",command=saveFile,image=saveIcon,compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,image=exitIcon,compound=LEFT)



'''membuat edit menu'''
editMenu=Menu(menuBar,tearoff=0,font=("MV Boli",10)) #membuat edit menu 
menuBar.add_cascade(label="edit",menu=editMenu)

'''membuat dropdown dalam edit menu'''

editMenu.add_command(label="Undo")
editMenu.add_command(label="Redo")

'''menambahkan dropdown didalam dropdown edit menu'''
editorFile = Menu(editMenu,tearoff=0,font=("MV Boli",10))
editMenu.add_cascade(label="Editor Layout",menu=editorFile)
editorFile.add_command(label="Split Up")
editorFile.add_command(label="Split Down")
editorFile.add_command(label="Split Left")
editorFile.add_command(label="Split Right")

window.mainloop()