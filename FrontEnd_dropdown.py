from operator import mod
from tkinter import *
from PIL import ImageTk,Image
from numpy import eye, var
from modes.eyeModeAlternative import eyeModeAlternative
from modes.eyeMode import eyeMode
from modes.faceMode import faceMode
from modes.presenceMode import presenceMode

root = Tk()
root.title('EyeTrack')
root.geometry("400x400")
modeVar = IntVar()
modeVar.set(1)
lowLight = IntVar()
lowLight.set(0)
pauseDelay = IntVar()
pauseDelay.set(0)

# Will execute selected command in EyeTrack (work in progress)
def backendLink():

   if modeVar.get() == 1:
      eyeMode(lowLight, pauseDelay)
      #eyeModeAlternative(lowLight, pauseDelay)
   elif modeVar.get() == 2:
      faceMode(lowLight, pauseDelay)
   elif modeVar.get() == 3:
      presenceMode(lowLight, pauseDelay)
    
#Closes the popup window
def close_win(top, entry):
   pauseDelay.set(int(entry.get()))
   print("Pause delay: {} seconds".format(pauseDelay.get()))
   top.destroy()

#Creates popup window to enter pause delay
def popupwin(root):
   #Creates a Toplevel window
   top = Toplevel(root)
   top.geometry("250x100")

   #Creates Entry Widget in the Toplevel window
   entry = Entry(top, width= 25)
   entry.pack()
   print(entry.get())

   #Creates Button Widget in the Toplevel Window
   button= Button(top, text="OK", command=lambda:close_win(top, entry))
   button.pack(pady=5, side= TOP)

def mainMenu():

   #Creates dropdown menu
   menubar = Menu(root)
   optionsmenu = Menu(menubar, tearoff = 0)
   optionsmenu.add_radiobutton(label = "Eye Mode", value=1, variable=modeVar)
   optionsmenu.add_radiobutton(label = "Face Mode", value=2, variable=modeVar)
   optionsmenu.add_radiobutton(label = "Presence Mode", value=3, variable=modeVar)
   optionsmenu.add_checkbutton(label = "Low Light On/Off", variable=lowLight)
   optionsmenu.add_command(label = "Set Pause Delay", command = lambda:popupwin(root))
   optionsmenu.add_separator()
   optionsmenu.add_command(label = "Exit", command = root.quit)
   menubar.add_cascade(label = "Options", menu = optionsmenu)

   startButton = Button(root, text="Start", command= lambda:backendLink())
   startButton.place(relx=0.5, rely=0.5, anchor=CENTER)

   root.config(menu=menubar)
   root.mainloop()