import random
from tkinter import *

value = 1

def generate(val):
    for i in range(0, val):
        key1 = random.randint(0, 999)
        key2 = random.randint(0, 9999999)
        while (key2 % 7 != 0):
            key2 = random.randint(0, 9999999)
        key = '{:03}'.format(key1) + "-" + '{:07}'.format(key2)
        box.config(state=NORMAL)
        box.delete(0, 'end')
        box.insert(1, key)
        box.config(state='readonly')

master = Tk()
master.title("winkey95")

canvas = Canvas(master, width=320, height=200)
canvas.pack(fill=BOTH, expand=0)

text = Label(text="Windows 95 OEM Key Generator", font = ("Segoe UI", 14))
text.place(relx=.5, rely=.15, anchor="center")
button = Button(text = "Generate!", command=lambda: generate(1), bd=3)
button.place(relx=.5, rely = .8, anchor="center")

box = Entry(justify=CENTER, readonlybackground="#ffffff", state='readonly')
box.place(relx=.5, rely=.5, anchor="center", width=240, height=24)

master.mainloop()

'''
#Filter the input (integer only)
try:
    val = int(value)
    if (val > 0):
        generate(val)
    else:
        print("Error : Input is not a positive integer!")
except ValueError:
    print("Error : Input is not a positive integer!")
'''