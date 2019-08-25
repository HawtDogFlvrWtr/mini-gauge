#!/usr/bin/env python

# Initial attempt at a display of random numbers over time on a pi
from Tkinter import *
from ttk import Progressbar
from ttk import Style
import random
import time

window = Tk()
text = StringVar()
text.set('loading...')
status = IntVar()
window.configure(background='black')
window.wm_attributes('-type', 'splash')
window.geometry('350x200')
def changeText():
    randomNum = random.randrange(1,15, 1)
    text.set(randomNum)
    progress['value'] = randomNum * .15 * 100
    window.after(100, changeText)

lbl = Label(window, compound=CENTER, textvariable=text, bg="black", fg="orange", font=("Arial Bold", 50))
lbl.place(x=175, y=100, anchor="center")
style = Style()
style.theme_use('default')
style.configure("orange.Horizontal.TProgressbar", troughcolor='black', foreground='orange', background='orange', troughrelief="flat" )
progress=Progressbar(window, orient=HORIZONTAL, style='orange.Horizontal.TProgressbar', length=200, mode='determinate')
progress.pack()
window.after(100, changeText)
window.mainloop()
