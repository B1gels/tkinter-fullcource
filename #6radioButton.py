from tkinter import *

#radioButton hampir sama dengan checkbutton tetapi hanya bisa memilih salah satu dari beberapa pilihan dalam grup

makanan = ['pizza','hamburger','hotdog']

def order():
    if x.get()==0:
        print("kamu memesan pizza")
    elif x.get()==1:
        print("kamu memesan burger")
    elif x.get()==2:
        print("kamu memesan hotdog")
    else:
        print("Huh?")


window = Tk()

pizza = PhotoImage(file='asset\\pizza.png')
burger = PhotoImage(file='asset\\burger.png')
hotdog = PhotoImage(file='asset\\hotdog.png')

foodImages = [pizza,burger,hotdog]

x = IntVar()

for i in range(len(makanan)):
    radiobutton = Radiobutton(window,
                              text=makanan[i], #menanmbahkan teks ke radioButton
                              variable=x,   #menyimpan nilai value,mengelompokkan radiobuttons ketika memiliki variable yang sama
                              value=i,   #memberikan radiobutton masing masing nilai yang berbeda
                              padx=25,
                              font=('Impact',40),
                              image=foodImages[i], #menambahkna gambar ke radioButton
                              compound=LEFT, #memindahkan gambar ke posisi [left] kiri
                              indicatoron=1, #menmghilangkan [0] atau memunculkan [1] indicator bulat
                            #   width=375, #mengatur lebarr radio buttons
                              command=order

                              )
    radiobutton.pack(anchor=W)


window.mainloop()