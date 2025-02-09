from tkinter import *

# Listbox  = list dari beberapa text yang bisa dipilih,yang berada dalam  container atau jendela utama


'''fungi untuk submit one item'''
# def submit():
#     print("kau memsan : ")
#     print(listbox.get(listbox.curselection()))

'''fungsi untuk submit multiple item'''
def submit():
    Food = []

    for index in listbox.curselection():
        Food.insert(index,listbox.get(index))

    print("kau memsan : ")
    for food in Food:
        print(food)


def add():
    if not entryBox.get().strip():     
        print("you can't do anything")
    else:
        listbox.insert(listbox.size(),entryBox.get().strip())  #strip() gunanya untuk menhilangkan baris baru didepan atau dibelakang
        listbox.config(height=listbox.size())


'''Fungsi untuk menghapus satu item'''
# def delete():
#     listbox.delete(listbox.curselection())
#     listbox.config(height=listbox.size())

'''Fungsi untuk menghapus beberapa item'''
def delete():
    for index in reversed(listbox.curselection()): #gunakan reversed agar penghapusan lebih efisien #dikarenakan saat kita menghaopus sati list maka nilai index nya berubah
        listbox.delete(index)
    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('Constantia',35),
                  width=15,
                  selectmode=MULTIPLE  # [MULTIPLE] mengizinkan memilih lebih dari satu listbox,[SINGLE] hanya dapat memilih satu
                  )
listbox.pack()


'''untuk menambahkan listbox dari luar '''
listbox.insert(1,'pizza')
listbox.insert(2,'pasta')
listbox.insert(3,'roti bawang')
listbox.insert(4,'sup')
listbox.insert(5,'salad')

listbox.config(height=listbox.size()) #coinfig digunakan untuk merubah protperti dari luar

entryBox = Entry(window,width=15)
entryBox.pack()

submitButon = Button(window,text='submit',command=submit,width=15)
submitButon.pack()

addButon = Button(window,text='Add',command=add,width=15)
addButon.pack()

deleteButon = Button(window,text='delete',command=delete,width=15)
deleteButon.pack()

window.mainloop() #agar program utama terus berjalan