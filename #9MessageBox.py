from tkinter import *
from tkinter import messagebox #mengimpor messagebox library

def click():
    '''show message'''
    # messagebox.showinfo(title='ini adalah kotak informasi',message="kau adalah seseorang")
    # messagebox.showwarning(title='WARNING!',message="YOU HAVE A VIRUS!!")
    # messagebox.showerror(title='ERROR!',message="something went wrong :(")

    '''ask message'''
    # if messagebox.askokcancel(title='ask ok cancel',message="apa anda yakin melakukannya?"):
    #     print("kau telah melakukannya ")
    # else: 
    #     print("sepertinnya anda berubah pikiran")

    # if messagebox.askretrycancel(title="ask retry cancel",message="sepertinya ada yang salah :("):
    #     print("anda mengulanginya ")
    # else: 
    #     print("sepertinnya anda berubah pikiran")

    # if messagebox.askyesno(title="ask yes no",message="kau suka dia?"):
    #     print("ya saya suka dia")
    # else:
    #     print("kayaknya tidak deh")


    '''berbeda dengan message box yang sebelumnya [askquestion] tidak mengembalikan boolean tetapi [yes/no]'''
    # answer = messagebox.askquestion(title="Ask my question",message="kau suka makan ikan?")

    # if answer == 'yes':
    #     print("ya saya suka makan ikan")
    # else:
    #     print("gamau deh bau amis")
    

    '''[askyesnocancel] mengembalikan nilai boolean [yes = True] [No=false] [cancel=None]'''
    answer = messagebox.askyesnocancel(title="yes no cancel",message="do u like code?",icon='error')

    if answer == True:                     
        print("ya saya suka ngoding")
    elif answer == False:
        print("Saya gak suka ngoding")
    else:
        print("saya pikir pikir lagi deh")






window = Tk()

button = Button(window,text="click me",command=click)
button.pack()

window.mainloop()