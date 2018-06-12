from tkinter import *
from tkinter import ttk

root = Tk()
root.title('ResistorRating')
root.geometry('500x500')

nb = ttk.Notebook(root)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

bycolors = ttk.Frame(nb)
nb.add(bycolors, text='By Colors')

byrating = ttk.Frame(nb)
nb.add(byrating, text='By Rating')

chart = ttk.Frame(nb)
nb.add(chart, text='Chart')

canvas = Canvas(bycolors, width = 517, height = 160)
canvas.pack()
img = PhotoImage(file="blank-resistor.png")
canvas.create_image(20,20, anchor=NW, image=img)

root.mainloop()