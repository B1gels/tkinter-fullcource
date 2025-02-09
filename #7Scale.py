from tkinter import *

def submit():
    print("suhu sekarang adalah : " + str(scale.get()) + " derajat celcius")
    if scale.get() == 50:
        scale.config(troughcolor='#ffffff')
    elif scale.get() < 50 :
        scale.config(troughcolor='Cyan')
    elif scale.get() > 50 :
        scale.config(troughcolor='Red')
    else:
        print("Huh?")

window = Tk()

hotImage = PhotoImage(file="asset\\panas.png")
hotLabel = Label(window,image=hotImage)
hotLabel.pack()



scale = Scale(window,
              from_=100,
              to=0,
              length=500,
              orient=VERTICAL, #orientasi [HORIZONTAL] atau [VERTICAL] scale
              font=('Consolas',15),
              tickinterval=10, #menambahkan indikator nomor untuk nilai scale
            #   showvalue=0, #[0] menghilangkan atau [1] memunculkan informasi nilai di tombol
              resolution=5, # nilai tambah dari penggeser(slider) [5] berarti menambahkan kelipatan 5 saja
              troughcolor='#ffffff', #backgroudnd scale slider indicator
              fg='Green',
              bg='#000000'
              )
              
# scale.set(50)
scale.set(((scale['from']-scale['to'])/2)) #mengatur posisi awal slider di nilai mana

scale.pack()

coldImage = PhotoImage(file="asset\\dingin.png")
coldLabel = Label(window,image=coldImage)
coldLabel.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()