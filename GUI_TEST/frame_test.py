from tkinter import *
import webbrowser
t=Tk()
t.title("Frame By Frame GUI")
t.geometry("460x350")
t.grid_columnconfigure(0,weight=1)
t.grid_rowconfigure(1,weight=1)
#main frames
f=Frame(t,bg="light blue",width=460,height=35,pady=5,padx=45)
ff=Frame(t,bg="light gray",width=460,height=280,highlightcolor="black",padx=50,pady=10,highlightbackground="black")
footer=Frame(t,bg="gray93",width=460,height=35,pady=6,padx=42)

f.grid(row=0,sticky="ew")
f.grid_rowconfigure(0,weight=2)
f.grid_columnconfigure(0,weight=1)
f.grid_columnconfigure(2,weight=1)
f.grid_columnconfigure(1,weight=1)

ff.grid(row=1,sticky="nsew")
footer.grid(row=2,sticky="nsew")
def onclickSource():
    webbrowser.open("https://github.com/nikmul19/Python/blob/master/GUI_TEST/frame_test.py")
#top most frame widgets    
source=Button(f,text="View Source code",command=onclickSource,highlightbackground="grey")
source.grid(row=0,column=0,sticky="ew")
login=Button(f,text="Sign-up",padx=10,highlightbackground="grey")
login.grid(row=0,column=1,ipadx=20,sticky="ew")
sign_in=Button(f,text="Sign-in",padx=5,highlightbackground="grey")
Or=Label(f,text="or",bg="grey",pady=4,fg="white")
Or.grid(row=0,column=2,sticky="ew")
sign_in.grid(row=0,column=3,ipadx=20)


heading=Label(ff,text="YouBuild",font="calibri 26 bold  underline",pady=10,height=1,bg="light grey")
heading.pack()
#box object
box=LabelFrame(ff,height=250,width=200,bg="white",bd=5,relief="flat")
box.pack()
box.config(highlightbackground="green")
print(box.winfo_width)
#inside the box

#userframe
user=Frame(box,height=100,width=199,bg="white")
user.grid(row=0,sticky="nsew")

#passwordframe
passFrame=Frame(box,height=70,width=199,bg="white")
passFrame.grid(row=1,sticky="nsew")


#login-button
signbutton=Button(box,text="Login",fg="white",highlightbackground="springgreen2")
signbutton.grid(row=2,column=0,columnspan=2,sticky="ew")

def create_user():
    """ creates username label and an entry field to enter username"""
    username=Label(user,text="Username",fg="black",bg="white")
    username.grid(row=0,column=0,sticky="w")
    #entry field
    userid=Entry(user,width=21)
    userid.grid(row=1,column=0,columnspan=2,sticky="e")



def create_password():
    """creates password label and an entry field to get the password"""
    password=Label(passFrame,text="Password")
    password.grid(row=0,column=0,sticky="w")
    password_entry=Entry(passFrame,width=21,show="*")
    password_entry.grid(row=1,column=0)
    forget=Button(passFrame,text="Forgot password?",width=12,font="calibri 10 underline",)
    forget.grid(row=2,sticky="e")


create_user()
create_password()

#footer part
develop=Label(footer,text="Developer: Nikhil Mulchandani",fg="blue",bg="gray93",width=40)
develop.pack()


t.mainloop()
