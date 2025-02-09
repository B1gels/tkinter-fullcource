from tkinter import *

def checkButton():
    print(f"Status Checkbutton: {x.get()}")
    if x.get() == 1:
        print("saya menyetujuinya")
    else:
        print("saya akan memikirkannya lagi :)")

window = Tk()

photo = PhotoImage(file='asset\\python.png')

x = IntVar() # Menyimpan status Checkbutton

check_button = Checkbutton(window,
                text="saya menyetujuinya",
                variable=x, #untuk menyimpan nilai [onvalue]  dan nilai [offValue]
                onvalue=1, #untuk menginisialisasi nilai ketika button dicentang
                offvalue=0, #untuk menginisialisasi nilai ketika button tidak dicentang 
                command=checkButton,
                padx=20,
                pady=10,
                image=photo,
                compound=LEFT,
                font=('arial',15),
                background='#000000',
                fg='Green',
                activebackground="#000000",
                activeforeground='Green'
                
                )
check_button.pack()

window.mainloop()