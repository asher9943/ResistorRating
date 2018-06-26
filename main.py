from tkinter import *
from tkinter import ttk

# dictionary with band values and corresponding colors
bands01 = {
    0 : 'black',
    1 : 'brown',
    2 : 'red',
    3 : 'orange',
    4 : 'yellow',
    5 : 'green',
    6 : 'blue',
    7 : 'pink',
    8 : 'grey',
    9 : 'white'
}
band2 = {
    .01 : 'silver',
    .1 : 'gold',
    1 : 'black',
    10 : 'brown',
    100 : 'red',
    1000 : 'orange',
    10000 : 'yellow',
    100000 : 'green',
    1000000 : 'blue'
}
band3 = {
    1 : 'brown',
    2 : 'red',
    5 : 'gold',
    10 : 'silver',
}
# setup main window
root = Tk()
root.title('ResistorRating')
root.geometry('500x250')

# setup notebook (tabbed view)
nb = ttk.Notebook(root)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

# tab for resistor raing by color
bycolors = ttk.Frame(nb)
nb.add(bycolors, text='By Colors')

# canvas for resistor image
colorcanvas = Canvas(bycolors, width=500, height=160)
colorcanvas.pack()

# add resistor as background image of canvas
img = PhotoImage(file="blank-resistor.png")
colorcanvas.create_image(250, 20, anchor=N, image=img)

# list holding band numerical values
bandvals = [0, 0, .01, 1]

# function to advance band values
def advbandval(band, bandnum):
    if bandnum == 0 or bandnum == 1:
        if bandvals[bandnum] == 9:
            bandvals[bandnum] = 0
        else:
            bandvals[bandnum] += 1
        band.configure(bg=bands01[bandvals[bandnum]])
    elif bandnum == 2:
        if bandvals[bandnum] == 1000000:
            bandvals[bandnum] = .01
        else:
            bandvals[bandnum] *= 10
        band.configure(bg=band2[bandvals[bandnum]])
    elif bandnum == 3:
        if bandvals[bandnum] == 2:
            bandvals[bandnum] = 5
        elif bandvals[bandnum] == 10:
            bandvals[bandnum] = 1
        else:
            bandvals[bandnum] *= 2
        band.configure(bg=band3[bandvals[bandnum]])

#function to calculate resistor rating
def calcrating(calcbutton):
    rating = (bandvals[0] + bandvals[1]) * bandvals[2]
    calcbutton.configure(text='Rating: ' + "{0:.2f}".format(rating) + 'Ω, ' + str(bandvals[3]) + '% Tolerance')

#function to set resistor bands based
def setresistor():
    print('set resistor')

# buttons for resistor bands
colorbutton0 = Button(colorcanvas, bg=bands01[bandvals[0]], command = lambda: advbandval(colorbutton0, 0))
colorbutton0.pack()
colorbutton0.place(x=175, y=35, bordermode = OUTSIDE, height=50, width=10)
colorbutton1 = Button(colorcanvas, bg=bands01[bandvals[1]], command = lambda: advbandval(colorbutton1, 1))
colorbutton1.pack()
colorbutton1.place(x=200, y=35, bordermode = OUTSIDE, height=50, width=10)
colorbutton2 = Button(colorcanvas, bg=band2[bandvals[2]], command = lambda: advbandval(colorbutton2, 2))
colorbutton2.pack()
colorbutton2.place(x=225, y=35, bordermode = OUTSIDE, height=50, width=10)
colorbutton3 = Button(colorcanvas, bg=band3[bandvals[3]], command = lambda: advbandval(colorbutton3, 3))
colorbutton3.pack()
colorbutton3.place(x=300, y=35, bordermode = OUTSIDE, height=50, width=10)
calcbutton = Button(bycolors, text = 'Calculate', command = lambda: calcrating(calcbutton))
calcbutton.pack()

# tab for resistor colors by rating
byrating = ttk.Frame(nb)
nb.add(byrating, text='By Rating')

# canvas for resistor image
ratingcanvas = Canvas(byrating, width=500, height=160)
ratingcanvas.pack()

# add resistor as background image of canvas
ratingcanvas.create_image(250, 20, anchor=N, image=img)

# buttons for resistor bands
ratingbutton0 = Button(ratingcanvas, bg='black', state=DISABLED)
ratingbutton0.pack()
ratingbutton0.place(x=175, y=35, bordermode = OUTSIDE, height=50, width=10)
ratingbutton1 = Button(ratingcanvas, bg='black', state=DISABLED)
ratingbutton1.pack()
ratingbutton1.place(x=200, y=35, bordermode = OUTSIDE, height=50, width=10)
ratingbutton2 = Button(ratingcanvas, bg='silver', state=DISABLED)
ratingbutton2.pack()
ratingbutton2.place(x=225, y=35, bordermode = OUTSIDE, height=50, width=10)
ratingbutton3 = Button(ratingcanvas, bg='brown', state=DISABLED)
ratingbutton3.pack()
ratingbutton3.place(x=300, y=35, bordermode = OUTSIDE, height=50, width=10)
ratingentry = Entry(byrating)
ratingentry.pack()
resistorsetbutton = Button(byrating, text = 'Begin')
resistorsetbutton.pack()

# tab for chart of resistor colors
chart = ttk.Frame(nb)
nb.add(chart, text='Chart')

root.mainloop()