from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir='C:\\Users\\ACER\\OneDrive\\Desktop\\python_from_zero_to_hero\\Tkinter\\Tutorial', #mengatur lokasi path file pertama kali dibuka (opsional)
                                          title='open file',
                                          filetypes=(("all files",'*.*'),("text files",'*.txt'),("image",'*.jpg;*.png;*.jpeg'),('HTML File','*.html')) #mengfilter filetype  | gunakan semocolon ; untuk menggabungkan beberapa format
                                          )
    
    if filepath == '':      #error handleing jika user membatalkan pilih file
        return None

    file = open(filepath,'r')
    textArea.insert(1.0,file.read())
    file.close()
    
window = Tk()

button = Button(window,text="open",command=openFile)
button.pack()

textArea = Text(window)
textArea.pack()

window.mainloop()    