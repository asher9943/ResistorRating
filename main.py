from tkinter import *
from tkinter import ttk

# setup main window
root = Tk()
root.title('ResistorRating')
root.geometry('500x500')

# setup notebook (tabbed view)
nb = ttk.Notebook(root)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

# tab for resistor raing by color
bycolors = ttk.Frame(nb)
nb.add(bycolors, text='By Colors')

# canvas for resistor image
canvas = Canvas(bycolors, width=500, height=160)
canvas.pack()
img = PhotoImage(file="blank-resistor.png")
canvas.create_image(250, 20, anchor=N, image=img)
colorbutton1 = Button(canvas, bg='black')
colorbutton1.pack()
colorbutton1.place(x=175, y=35, bordermode = OUTSIDE, height=50, width=10)
colorbutton2 = Button(canvas, bg='black')
colorbutton2.pack()
colorbutton2.place(x=200, y=35, bordermode = OUTSIDE, height=50, width=10)
colorbutton3 = Button(canvas, bg='black')
colorbutton3.pack()
colorbutton3.place(x=225, y=35, bordermode = OUTSIDE, height=50, width=10)
colorbutton4 = Button(canvas, bg='black')
colorbutton4.pack()
colorbutton4.place(x=300, y=35, bordermode = OUTSIDE, height=50, width=10)

# tab for resistor colors by rating
byrating = ttk.Frame(nb)
nb.add(byrating, text='By Rating')

# tab for chart of resistor colors
chart = ttk.Frame(nb)
nb.add(chart, text='Chart')

root.mainloop()