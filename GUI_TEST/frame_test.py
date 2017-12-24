from tkinter import *
import webbrowser
t=Tk()
t.title("Frame By Frame GUI")
t.geometry('{}x{}'.format(460, 350))
f=Frame(t,bg="black",width=460,height=35,pady=5,padx=45)
ff=Frame(t,bg="cyan",width=460,height=280,highlightcolor="black",highlightbackground="black")
footer=Frame(t,bg="grey",width=460,height=35,pady=10)
footer.grid(row=2)

ff.grid(row=1)
f.grid(row=0,sticky="ew")
def onclickSource():
    webbrowser.open("https://github.com/nikmul19/Python/blob/master/GUI_TEST/gui_test.py")
    
source=Button(f,text="View Source code",command=onclickSource,highlightbackground="grey")
source.grid(row=0,column=0)
login=Button(f,text="Sign-up",padx=10,highlightbackground="grey")
login.grid(row=0,column=1,ipadx=20)
sign_in=Button(f,text="Sign-in",padx=5,highlightbackground="grey")
Or=Label(f,text="or",bg="grey",pady=4,fg="white")
Or.grid(row=0,column=2)
sign_in.grid(row=0,column=3,ipadx=20)
t.mainloop()
