from tkinter import *
from PIL import ImageTk,Image

# Will execute selected command in EyeTrack (work in progress)
def backendLink():
    x = 0

root = Tk()
root.title('EyeTrack')
root.geometry("400x400")

#Closes the popup window
def close_win(top):
   top.destroy()

#Creates popup window to enter pause delay
def popupwin():
   #Creates a Toplevel window
   top = Toplevel(root)
   top.geometry("250x100")

   #Creates Entry Widget in the Toplevel window
   entry = Entry(top, width= 25)
   entry.pack()

   #Creates Button Widget in the Toplevel Window
   button= Button(top, text="OK", command=lambda:close_win(top))
   button.pack(pady=5, side= TOP)

#Creates dropdown menu
menubar = Menu(root)
optionsmenu = Menu(menubar, tearoff = 0)
optionsmenu.add_radiobutton(label = "Eye Mode", command = lambda:backendLink())
optionsmenu.add_radiobutton(label = "Face Mode", command = lambda:backendLink())
optionsmenu.add_radiobutton(label = "Presence Mode", command = lambda:backendLink())
optionsmenu.add_checkbutton(label = "Low Light On/Off", command = lambda:backendLink())
optionsmenu.add_command(label = "Set Pause Delay", command = lambda:popupwin())
optionsmenu.add_separator()
optionsmenu.add_command(label = "Exit", command = root.quit)
menubar.add_cascade(label = "Options", menu = optionsmenu)


root.config(menu=menubar)
root.mainloop()