from tkinter import *


window = Tk()

title = Label(window,text="Enter your info",font=('Arial',25)).grid(row=0,column=0,columnspan=2)

FirstNameLabel = Label(window,text="FirstName:",bg="Red",width=30)
FirstNameLabel.grid(row=1,column=0)
FirstNameEntry = Entry(window)
FirstNameEntry.grid(row=1,column=1)

lastNameLabel = Label(window,text="LastName:",bg="Green")
lastNameLabel.grid(row=2,column=0)
lastNameEntry = Entry(window)
lastNameEntry.grid(row=2,column=1)

EmailLabel = Label(window,text="Email:",bg="Blue",width=20)
EmailLabel.grid(row=3,column=0)
EmailEntry = Entry(window)
EmailEntry.grid(row=3,column=1)

submitButton = Button(window,text='Submit').grid(row=4,column=0,columnspan=2)

window.mainloop()