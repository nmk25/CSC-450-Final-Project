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
import cv2


root = Tk()
root.title('Eye Pause')

# Root window dimensions
w = 300
h = 225 

# Get screen width and height
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

# Calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# Set dimensions and place of window
root.geometry('%dx%d+%d+%d' % (w, h, x, y - 75))

# Background image
image = Image.open("eye.png")
img = ImageTk.PhotoImage(image.resize((275, 200))) 
label = Label(root, image = img)
label.pack(pady=10)

modeVar = IntVar()
modeVar.set(1)
lowLight = IntVar()
lowLight.set(0)
pauseDelay = DoubleVar()
pauseDelay.set(0.5)
filePath = ""

# Mode select from backend
def backendLink(filePath):

   # Web Cam Capture
   cap = cv2.VideoCapture(0)

   # Check capture
   if cap is None or not cap.isOpened():
      # Create a Toplevel window
      top = Toplevel(root)
      top.title("Capture Error")

       # Top window dimensions
      w = 225
      h = 50

      # Calculate x and y coordinates for the Tk root window
      x = (ws/2) - (w/2)
      y = (hs/2) - (h/2)

      # Set dimensions and place of window
      top.geometry('%dx%d+%d+%d' % (w, h, x, y - 75))

      # Text label
      msg = Label(top, text="Error: No camera was detected.")
      msg.pack(pady=10)
   else:
      if modeVar.get() == 1:
         #eyeMode(lowLight, pauseDelay, filePath, cap)
         eyeModeAlternative(lowLight, pauseDelay, filePath, cap)
      elif modeVar.get() == 2:
         faceMode(lowLight, pauseDelay, filePath, cap)
      elif modeVar.get() == 3:
         presenceMode(lowLight, pauseDelay, filePath, cap)
    
# Closes the popup window
def close_win(top, entry, msg):
   try:
      if (double(entry.get()) >= 0):
         pauseDelay.set(double(entry.get()))
         print("Pause delay: {} seconds".format(pauseDelay.get()))
         top.destroy()
      else:
         msg.config(text="Please enter a positive number.")
   except ValueError:
      msg.config(text="Please enter a valid time.")

# Creates popup window to enter pause delay
def popupwin(root):

   # Create a Toplevel window
   top = Toplevel(root)
   top.title("Set Pause Delay")

   # Top window dimensions
   w = 225
   h = 100 

   # Calculate x and y coordinates for the Tk root window
   x = (ws/2) - (w/2)
   y = (hs/2) - (h/2)

   # Set dimensions and place of window
   top.geometry('%dx%d+%d+%d' % (w, h, x, y - 75))

   # Text label for input validation
   msg = Label(top, text="Enter a time in seconds.")
   msg.pack(pady=5)

   # Creates Entry Widget in the Toplevel window
   entry = Entry(top, width= 25)
   entry.pack()

   # Creates Button Widget in the Toplevel Window
   button= Button(top, text="SET", command=lambda:close_win(top, entry, msg))
   button.pack(pady=5, side= TOP)

# File directory
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