from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title('Made in Bangladesh')    #Header of this clock


def time():
    string = strftime('%I:%M:%S %p')    #Time format
    l.config(text=string)
    l.after(1000, time)


l = Label(root, font=('ds-digital', 120),   #font style
            background='black', #Background color
            foreground='red')   #Foreground color that means font color

l.pack(anchor='center')
time()

mainloop()