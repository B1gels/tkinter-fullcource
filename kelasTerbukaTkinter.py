import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="#fff")
window.geometry("400x400")
window.resizable(False,False)
window.title("Form")

input_frame = ttk.Frame(window)
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

NAMA_DEPAN = tk.StringVar()
Label_nama_depan = ttk.Label(input_frame,text="Nama Depan :")
Label_nama_depan.pack(padx=10,fill="x",expand=True)

input_depan = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
input_depan.pack(padx=10,fill="x",expand=True)


NAMA_BELAKANG = tk.StringVar()
Label_nama_belakang = ttk.Label(input_frame,text="Nama Belakang :")
Label_nama_belakang.pack(padx=10,fill="x",expand=True)

input_belakang = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
input_belakang.pack(padx=10,fill="x",expand=True)

# tombol
def tombol_click():
    pesan = f"Hallo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()},Selamat datang"
    showinfo(title="Pesan",message=pesan)


button = ttk.Button(input_frame,text="ENTER",command=tombol_click)
button.pack(padx=10,pady=10,fill="x",expand=True)

window.mainloop()
