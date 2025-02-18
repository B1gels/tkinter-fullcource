from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import messagebox
import time

def start():
    size = 24  # Ukuran file dalam GB
    MB = 1024 * 1024  # 1 MB dalam bytes
    download = 0
    speed = 1024 * 512  # Kecepatan download (512 KB per iterasi)

    bar["value"] = 0  # Reset progress bar di awal
    percent.set("0%")
    text.set("0.00 GB / {} GB diselesaikan".format(size))

    while download < (size * MB):
        time.sleep(0.05)
        download += speed
        task_done = download / MB  # Konversi ke MB
        progress_value = (download / (size * MB)) * 100  # Hitung persentase
        
        bar["value"] = progress_value
        percent.set("{:.0f}%".format(progress_value))
        text.set("{:.2f} GB / {} GB diselesaikan".format(task_done / 1024, size))  # Konversi ke GB

        window.update_idletasks()

    messagebox.showinfo(title="Info", message="Download selesai!")

window = Tk()
window.title("Progress Bar")
window.config(padx=20, pady=10)

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300, mode="determinate")
bar.pack(pady=10)

percent_label = Label(window, textvariable=percent)
percent_label.pack()

task_label = Label(window, textvariable=text)
task_label.pack()

button = Button(window, text="Download", command=start)
button.pack(pady=10)

window.mainloop()
