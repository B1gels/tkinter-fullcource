from tkinter import *

count = 0
def click():
    # global count #global digunakan untuk Mengakses variabel global 'count',tanpa "global",maka variable count local dianggap variable baru yang berbeda dengan global
    count += 1
    print(count)
#button ,ketika di click akan melakukan sesuatu

window = Tk()
window.title("button")

buttonImage = PhotoImage(file='asset\\likeButton.png')

button = Button(window,
                text="click  me!", 
                command=click,  #menambahkan perintah saat tombol di klick
                font=("Comic sans",40),
                fg='Green',
                bg='#000000',
                activeforeground='#000000', #warna teks saat tombol aktif
                activebackground='Green', #warna background saat tombol aktif
                state=ACTIVE, #ketika [ACTIVE] maka nilainya default tombol bisa di klik oleh siapapun
                              #tetapi ketika [DISABLED] tombol tidak akan bisa di klik oleh siapapun
                image=buttonImage,
                compound="top"
                   
                )
button.pack()

window.mainloop()