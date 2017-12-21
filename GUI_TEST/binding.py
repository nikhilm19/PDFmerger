from tkinter import *
def clicked(self):
    print("hi")

b=Button(None,text="click")
b.pack()
b.focus_set()
b.bind("<Return>",clicked)

b.mainloop()

