import sys
import string
from tkinter import *
from tkinter import messagebox
class login(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.bind("<Return>",self.onclickLogin)
        self.signup=Label(self,text="if new user then click signup else sign-in")
        self.loginbutton=Button(self,text="Login",width=25,height=5)
        self.loginbutton.grid(row=2,column=0,columnspan=2)
        self.logintext=Label(self,text="username",width=25,height=5)
        self.username=Entry(self)
        self.logintext.grid(row=0,column=0)
        self.username.grid(row=0,column=1)
        self.passwordtext=Label(self,text="enter password",width=25,height=10)
        self.password=Entry(self,show="*")
        self.passwordtext.grid(row=1,column=0)
        self.loginbutton.focus_set()
        self.loginbutton.bind("<Return>",self.onclickLogin)
        self.password.grid(row=1,column=1)
        

    def onclickLogin(self,event):
        print(sys.argv)
        user=(self.username.get())
        user=user.strip(string.whitespace)
        password=self.password.get()
        print(password)
        
        f=open("login_details.txt","r")
        for i in f:
            i=i.strip("\n")
            u,p=i.split(" ")
            if(user==u):
                print("username is correct")
                if(password==p):
                    self.error=messagebox.showinfo("login successful","redirecting..")
                    flag=True
                
       
            
            
            
                       

file=login()
file.mainloop()
