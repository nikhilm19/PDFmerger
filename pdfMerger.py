from tkinter import *
from tkinter import messagebox
import os
from PyPDF2 import PdfFileMerger
class merge(Tk):    
    def __init__(self):
        """intialize"""
        Tk.__init__(self)
        self.geometry("420x350")
        self.configure(bg="grey")
        self.title("Pdfmerger: Merge Pdfs with ease")
        self.frames()
        self.createWidgets()
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)

    def frames(self):
        """
           creates 3 frames: header,middle & footer
        """
        self.update()
        self.header=Frame(self,width=420,height=1)
        self.header.grid(row=0,column=0,sticky="nsew")
        self.middle=Frame(self,width=420,height=2,padx=10,bg="#002240")
        self.middle.grid(row=1,column=0,sticky="nsEW")
        """self.middle.grid_rowconfigure(0,weight=2)
        #self.middle.grid_rowconfigure(1,weight=1)
        self.middle.grid_columnconfigure(0,weight=1)    
        self.middle.grid_columnconfigure(1,weight=2)
        self.middle.grid_columnconfigure(2,weight=1)
        """

        self.footer=Frame(self,width=500,height=100,bg="grey")
        self.footer.grid(row=2,column=0,sticky="nsew")
        
    def saveAs(self):
        #print("filename:")
        self.fileName=filedialog.asksaveasfilename(title="Select saveAs filename",filetypes=(("Pdf files","*.pdf"),))
        #print(self.fileName)
        self.merger=PdfFileMerger()
        try:
            for pdf in self.files:
                self.merger.append(pdf)
            self.merger.write(self.fileName)
        except AttributeError:
            self.err=messagebox.showerror(title="No files Selected", message="Please select PDF files")   
    def selectFiles(self):
        print("hi")
        self.files=list(filedialog.askopenfilenames(title="Select Files",filetypes=(("Pdf files", "*.pdf"),)))
        self.exts=[]
        self.incompatible=[]
        for file in self.files:
            self.name,self.ext=os.path.splitext(file)
            self.exts.append(self.ext)
            if(self.ext!=".pdf"):
                #self.error=messagebox.showerror(title="Incompatible file type",message="File: "+file+" is not a PDf file")
                self.incompatible.append(file)
        if(len(self.incompatible)!=0):
            self.out="\n".join(self.incompatible)
            self.error=messagebox.showerror(title="Incompatible file type",message="File: "+self.out+" is not a PDf file")   
    
    def createWidgets(self):
        """creates Button,Label and entry field
        """
        self.developer=Label(self.header,text="PDFMerger",bg="grey80",fg="red",font=("Courier",20,"underline"),width=26)
        self.developer.pack(expand=True,fill="x")

        self.box=LabelFrame(self.middle,height=250,width=150,bg="white",bd=5,relief="raised")
        self.box.pack(expand=True)
        self.box.config(highlightbackground="green")
    
        self.grid_rowconfigure(1,weight=1)
        self.save=Button(self.box,text="Save as",bg="light grey",height=2,command=self.saveAs)
        self.save.pack(fill="x",expand=True)
        #self.save.grid(row=0,column=0,columnspan=2,rowspan=3,sticky="ew")
        self.select=Button(self.box,text="Select Files",bg="light blue",height=2,width=25,command=self.selectFiles,font=("Arial",12))
        self.select.pack(fill="both")#self.select.grid(row=4,column=0,columnspan=2)
        self.developer=Label(self.footer,text="Developed by Nikhil Mulchandani    M:8758583958",fg="blue",height=2,width=52,bg="white")
        self.developer.pack(expand=True,fill="x")
file=merge()
file.mainloop()
