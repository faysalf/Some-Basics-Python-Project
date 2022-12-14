from tkinter import *
from tkinter.ttk import *

# importing strftime function to
# retrieve system's time
from time import strftime

# creating tkinter window
root = Tk()
root.title("HELLO! I'M FAYSAL AHMED")


# This function is used to
# display time on the label
def time():
    string = strftime('%I:%M:%S %p')    #if I wrote %H instead of %I then it's showing 24 hors format
    lbl.config(text=string)
    lbl.after(1000, time)


# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font=('ds-digital', 120, 'bold'),
            background='black',
            foreground='red')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()