from tkinter import *

def sapa():
    first_name = firstName.get().strip()
    last_name = lastName.get().strip()
    Email = email.get()
    Password = password.get()

    if not first_name or not last_name or not Email or not Password :
        return None

    print(f"\n[LOGGIN SUCCES] \nHalo {first_name} {last_name}\nyour email \t: {Email}\nPasword \t: {Password}\n") 

window = Tk()
window.geometry("400x500")
window.resizable(False,False)
window.title("Login Form")

#Icon app
appIcon = PhotoImage(file="asset\\user.png")
window.iconphoto(True,appIcon)

# Frame utama
mainFrame = Frame(window)
mainFrame.pack(pady=40,padx=20) 

# Title
Label(mainFrame, text="Registration", font=('Verdana', 11, 'bold')).pack(pady=10,anchor=W)

# Form
Label(mainFrame,text="FirstName*").pack(anchor=W)
firstName = Entry(mainFrame, width=40,font=("Verdana",12))
firstName.pack(ipady=3,anchor=W,padx=(0,10),pady=(0,20))

Label(mainFrame,text="LastName*").pack(anchor=W)
lastName =  Entry(mainFrame, width=40,font=("Verdana",12))
lastName.pack(ipady=3,anchor=W,padx=(0,10),pady=(0,20))

Label(mainFrame,text="Email*").pack(anchor=W)
email =  Entry(mainFrame, width=40,font=("Verdana",12))
email.pack(ipady=3,anchor=W,padx=(0,10),pady=(0,20))

Label(mainFrame,text="Password*").pack(anchor=W)
password =  Entry(mainFrame, width=40,font=("Verdana",12),show="#")
password.pack(ipady=3,anchor=W,padx=(0,10),pady=(0,20))

#button
Button(mainFrame,text='Register Now',fg="#ffffff",command=sapa,bg="#1878f5",height=2,font=('Verdana', 10, 'bold')).pack(pady=15,expand=True,fill="x",padx=(0,10))

window.mainloop()