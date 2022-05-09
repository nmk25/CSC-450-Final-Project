from operator import mod
from tkinter import *
from PIL import ImageTk,Image
from numpy import double, eye, var
from modes.eyeModeAlternative import eyeModeAlternative
from modes.eyeMode import eyeMode
from modes.faceMode import faceMode
from modes.presenceMode import presenceMode
import tkinter as tk
from tkinter import filedialog


root = Tk()
root.title('Eye Pause')
root.geometry("300x225")

image = Image.open("eye.png")
img = ImageTk.PhotoImage(image.resize((275, 200))) 
label = Label(root, image = img)
label.pack()

# Create a Label Widget to display the text or Image

modeVar = IntVar()
modeVar.set(1)
lowLight = IntVar()
lowLight.set(0)
pauseDelay = DoubleVar()
pauseDelay.set(0.5)
filePath = ""

# Mode select from backend
def backendLink(filePath):

   if modeVar.get() == 1:
      #eyeMode(lowLight, pauseDelay, filePath)
      eyeModeAlternative(lowLight, pauseDelay, filePath)
   elif modeVar.get() == 2:
      faceMode(lowLight, pauseDelay, filePath)
   elif modeVar.get() == 3:
      presenceMode(lowLight, pauseDelay, filePath)
    
# Closes the popup window
def close_win(top, entry):
   try:
      if (double(entry.get()) >= 0):
         pauseDelay.set(double(entry.get()))
         print("Pause delay: {} seconds".format(pauseDelay.get()))
         top.destroy()
      else:
         print("Please enter a positive number.")
   except ValueError:
      print("Please enter a valid number.")
   

# Creates popup window to enter pause delay
def popupwin(root):
   # Creates a Toplevel window
   top = Toplevel(root)
   top.geometry("250x100")
   top.title("Set Pause Delay")

   # Creates Entry Widget in the Toplevel window
   entry = Entry(top, width= 25)
   entry.pack()

   # Creates Button Widget in the Toplevel Window
   button= Button(top, text="OK", command=lambda:close_win(top, entry))
   button.pack(pady=5, side= TOP)

def openDirectory():
   root = tk.Tk()
   root.withdraw()
   videoTypes = ".avchd .avi .bik .f4v .flv .h264 .m1v .m2v .m4v .mjpg .mp4 .mpeg1 .mpeg4 .mpg2 .mpv .mts .nsv .nuv .ogv .pss .svi .tod .trp .ts .vp6 .vro .webm"
   filePath = filedialog.askopenfilename(filetypes=[("Video files", videoTypes)])
   root.destroy()
   if (len(filePath) > 0):
      backendLink(filePath)
   

def mainMenu():

   # Creates dropdown menu
   menubar = Menu(root)
   fileMenu = Menu(menubar, tearoff=0)
   fileMenu.add_radiobutton(label = "Open File...", command = lambda:openDirectory())
   optionsmenu = Menu(menubar, tearoff = 0)
   optionsmenu.add_radiobutton(label = "Eye Mode", value=1, variable=modeVar)
   optionsmenu.add_radiobutton(label = "Face Mode", value=2, variable=modeVar)
   optionsmenu.add_radiobutton(label = "Presence Mode", value=3, variable=modeVar)
   optionsmenu.add_checkbutton(label = "Low Light On/Off", variable=lowLight)
   optionsmenu.add_command(label = "Set Pause Delay", command = lambda:popupwin(root))
   optionsmenu.add_separator()
   optionsmenu.add_command(label = "Exit", command = root.quit)
   menubar.add_cascade(label = "Media", menu = fileMenu)
   menubar.add_cascade(label = "Options", menu = optionsmenu)


   root.config(menu=menubar)
   root.mainloop()