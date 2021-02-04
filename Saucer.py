from tkinter import *
import random

window = Tk()

window.title("Saucer by Fostrullik")

window.geometry('450x300')

lbl = Label(window, text="Welcome to Saucer! Feel free to be happy today!")

lbl.grid(column=0, row=0)

def random():

    lbl.configure(random.range(1, 10))

btn = Button(window, text="I want some random", command=random)

btn.grid(column=1, row=0)

menu = Menu(window)

new_item = Menu(menu)

new_item.add_command(label='New')

new_item.add_separator()

new_item.add_command(label='Quit', command=window.destroy)

menu.add_cascade(label='File', menu=new_item)

window.config(menu=menu)

window.mainloop()