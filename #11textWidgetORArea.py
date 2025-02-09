from tkinter import *
#text widget = fungsi nya sama seperti text area bisa memasukkan banyaka baris text

def submit():
    input = textwidget.get("1.0",END).strip()
    print(input)

window = Tk()

textwidget = Text(window,
                  bg='Lightyellow',
                  font=('Ink Free',25),
                  width=20,
                  height=8,
                  padx=20,
                  pady=20,
                  fg="Purple"
                  )
textwidget.pack()


button = Button(window,text="submit!",command=submit)
button.pack()

window.mainloop()