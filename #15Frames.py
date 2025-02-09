from tkinter import *

# frame = wadah persegi panjang yang memuat dan mengelompokkan widget
# widgets = Gui elements: buttons,textBoxes,label,images

window = Tk()
frame = Frame(window,       #memasukkan frame kedalam window
              bg="Pink",    #mengubah warna background frame
              padx=25,      #menambahkan paddng [kiri dan kanan]
              pady=25,      #menambahkan padding [Atas dan Bawah]
              bd=5,         #menentukkan ketebalan border
              relief=SUNKEN #memilih tipe border [SUNKEN:seperti masuk kedalam] dan [RAISED : seperti menonjol]
              )
frame.place(x=100,y=100)

'''menggunakan cara cepat membuat button (tanpa variable)'''
Button(frame,text="W",font=("Consolas",25),width=3,relief=RAISED,bd=5).pack(side=TOP)
Button(frame,text="A",font=("Consolas",25),width=3,relief=RAISED,bd=5).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",25),width=3,relief=RAISED,bd=5).pack(side=LEFT)
Button(frame,text="D",font=("Consolas",25),width=3,relief=RAISED,bd=5).pack(side=LEFT)
window.mainloop()