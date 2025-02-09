from tkinter import *

window = Tk()
# window.geometry("240x240")

photo = PhotoImage(file='asset\\programer.png') #mengubah format image yang didukung tkinter

label = Label(window,#mengatur jendela mana label di tempatkan
              text="FikarGUI", #menambahkan teks kedalam label
              font=('Arial',40,"bold"), #font text
              fg='Green', #warna text
              bg='black', #warna backgroudn text
              relief=RAISED, #menambahkan tipe border
              bd=10, #ketebalan border
              padx=20, #padding kiri dan kanan
              pady=40, #padding atas dan bawah
              image=photo, #untuk memasukkan image ke label(tetapi akan menimpa teks)
              compound="bottom" #mengatur posisi image agar tidak menimpa teks
              ) 
# label.place(x=0,y=0)
label.pack()



window.mainloop()