from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import time

def start():
    size = 24  # Size in GB
    MB = 1024  # 1 GB = 1024 MB
    total_size = size * MB  # Total size in MB
    speed = 10  # Download speed in MB per iteration
    download = 0  # Downloaded data in MB

    def update_progress():
        nonlocal download
        if download < total_size:
            time.sleep(0.05)  # Simulate download delay
            download += speed
            task_done = download / MB
            progress = (download / total_size) * 100
            bar['value'] = progress
            percent.set(f"{int(progress)}%")
            text.set(f"{task_done:.2f} GB / {size} GB diselesaikan")
            window.after(50, update_progress)  # Schedule next update
        else:
            messagebox.showinfo(title="Info mas!!", message="Download selesai")

    update_progress()  # Start the download process

window = Tk()
window.title("Progress Bar")
window.config(padx=20, pady=10)

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack()

percentLabel = Label(window, textvariable=percent)
percentLabel.pack()

taskLabel = Label(window, textvariable=text)
taskLabel.pack()

button = Button(window, text="Download", command=start)
button.pack()

window.mainloop()