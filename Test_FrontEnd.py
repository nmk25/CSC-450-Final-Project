from ctypes import resize
from email.mime import image
from tkinter import *
from PIL import Image, ImageTk

#Creates basic window and size
root = Tk()
root.title('Eye Pause Options')
root.geometry("500x300")

#def validNumber():
 #   try:
  #      int(delay.get())
   #     delay_button.configure("New delay set!")
    #except ValueError:
     #   delay_button.configure("Invalid input.")

#creates background image and resizes it to window
img = Image.open("Images/simple-background.jpg")
resize_img = img.resize((500, 300), Image.ANTIALIAS)
back_img = ImageTk.PhotoImage(resize_img)

#button image
#img_button = PhotoImage(file ='black-button.png')
#img_button = Image.open('black-button.png')
#img_button = img_button.resize((240,120), Image.ANTIALIAS)
#new_button = ImageTk.PhotoImage(img_button)

#places resized bakground image
back_label = Label(root, image = back_img)
back_label.place(x=0,y=0, relwidth=1, relheight=1)

#Title
label_title=Label(root, text="Eye Pause", font=("Comic Sans", 20,),background ='white', relief = "solid")
label_title.pack(pady=10)

#keeps track of the radio button choice for the function
choice = IntVar()

#buttons for chosing the different modes of the media player - tracking eyes, tracking only face, and tracking only the user's presence
Radiobutton(root, text = "Eye Mode", variable = choice, value = 1).pack()
Radiobutton(root, text = "Face Mode", variable = choice, value = 2).pack()
Radiobutton(root, text = "Presence Mode", variable = choice, value = 3).pack()

#button for adjusting the camera to handle darker rooms - if possible
button_light=Button(root, text="Dark Light Mode")
button_light.pack(pady=10)

delay = Entry(root, width = 20)
delay.pack()
delay_button = Button(root, text = "Set a Pause Delay:", background ='white')
delay_button.pack()


#simple exit button.  Will quit the window, but move onto the media player.
#only quits the window until back-end linked.
button_quit = Button(root, text="Exit Eye Pause", command= root.quit)
button_quit.pack(pady = 10)

#function for adjusting the recognition sesnsor
def changeMode():
    return 0

#function for adjusting sensitivity of the camera for light if possible
def darklightClick():
    return 0

#passes input back to change pause delay
def changeDelay(input):
    return 0


root.mainloop()