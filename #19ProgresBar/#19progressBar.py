from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import time

def start():
    size = 24
    MB = 1024
    download = 0
    speed = 1024
    bar["value"] = 0
    text.set(f"0 GB / "+str((size))+" GB diselesaikan")

    while download < (size*MB):
        time.sleep(0.05)
        taskDone= download/MB
        download+=speed
        bar['value'] += (speed/(size*MB))*100
        percent.set(str(int((download/(size*MB))*100))+"%")
        text.set(f"{taskDone:.2f} GB / "+str((size))+" GB diselesaikan")

        window.update_idletasks()

        if percent.get() == "100%":
            messagebox.showinfo(title="Info mas!!",message="Download selesai")



window = Tk()
window.title("progres bar")
window.config(padx=20,pady=10)

# style = Style()
# style.configure("Custom.TLabel",foreground="#ffffff",background="Green",padx=20,pady=20)

percent = StringVar()
text = StringVar()

bar = Progressbar(window,
                  orient=VERTICAL, #mengubah rotasi progresbar [HORIZONTAL] dan [VERTICALl]
                  length=300         #Mengubah panjang progressbar (default : 100)
                  )
bar.pack()

percentLabel = Label(window,textvariable=percent)
percentLabel.pack()
taskLabel = Label(window,textvariable=text)
taskLabel.pack()

button = Button(window,text="Download",command=start).pack()


window.mainloop();