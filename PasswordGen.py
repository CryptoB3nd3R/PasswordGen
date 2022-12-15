from random import randint
from tkinter import *
from tkinter.ttk import *
from tkinter import Entry
import win32gui, win32con
from PIL import ImageTk

root = Tk()
root.title('PasswordGen')
root.geometry("500x300+1400+100")
root.resizable(False, False)

bg = ImageTk.PhotoImage(file="bg.jpg")


def new_rand():
    # Clear Our Entry Box

    pw_entry.delete(0, END)
    # Get PW Length and convert to integer

    pw_length = int(my_entry.get())

    # create a variable to hold our password
    my_password = ''

    # Loop through password length
    for x in range(pw_length):
        my_password += chr(randint(33, 126))
    
    my_entry.delete(0, END)
    # Output password to the screen
    pw_entry.insert(0, my_password)
	


    # Copy to clipboard
def clipper():
    # Clear the clipboard
    root.clipboard_clear()
    # Copy to clipboard
    root.clipboard_append(pw_entry.get())
    pw_entry.delete(0, END)
	

# Create canvas
my_canvas = Canvas(root, width=500, height=300)
my_canvas.pack(fill="both", expand=True)

# set image in canvas
my_canvas.create_image(0, 0, image=bg, anchor="nw")

# add a label
my_canvas.create_text(250, 35, text="PasswordGen", font=("Helvetica", 35), fill="green2")
my_canvas.create_text(250, 95, text="How Many Characters?", font=("Helvetica", 18), fill="green2")
# label1 = Label( root, image = bg)
# label1.place(x=0, y=0, relwidth=1, relheight=1)

# add Entry
my_entry = Entry(my_canvas, font=("Helevetica", 25), bg="light grey")
pw_entry = Entry(root, font=("Helevetica", 25), bg="light grey")

my_entry_window = my_canvas.create_window(75, 110, anchor="nw", window=my_entry)
pw_entry_window = my_canvas.create_window(75, 175, anchor="nw", window=pw_entry)


# add Button
button1 = Button(root, text="Generate Strong Password", command=new_rand)
button2 = Button(root, text="Copy to Clipboard", command=clipper)

button1_window = my_canvas.create_window(110, 250, anchor="nw", window=button1)
button2_window = my_canvas.create_window(270, 250, anchor="nw", window=button2)

# Hide Console
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)

root.mainloop()
