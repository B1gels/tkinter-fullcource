from tkinter import *

# entry widget = textbox yang memungkinkan menanganmbil satu baris dari inputan pengguna

def submit():
    username = entry.get()
    print("hallo " + username)
    # entry.config(state=DISABLED,bg='red') #menambahkan configurasi baru ketika di submit maka entry tidak bisa digunakan

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

window = Tk()

entry = Entry(window,
              font=("Arial",50),
              fg='Green',
              background='#000000'
            #   show='*' #hanya menampilkan karakter tertentu saja di box entry ,tetapi nilainya tetap berdasarkan apa yang kita ketik
              ) 

# entry.insert(0,'Spongebob') #menamnbahkan default teks dari index 0

entry.pack(side=LEFT)

submit_button = Button(window,text="submit!!",command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="delete",command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text="backspace",command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()