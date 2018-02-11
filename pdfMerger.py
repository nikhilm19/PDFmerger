from tkinter import *
from tkinter import messagebox
import os,subprocess,sys
from PyPDF2 import PdfFileMerger
class merge(Tk):
    def __init__(self):
        """intialize"""
        Tk.__init__(self)
        self.files=[]
        self.geometry("500x400")
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
        self.middle.grid(row=1,column=0,sticky="nsew")
        self.footer=Frame(self,width=500,height=100,bg="grey")
        self.footer.grid(row=2,column=0,sticky="nsew")
        
    def saveAs(self):
        self.completed=messagebox.askyesno(title="Merged",message="selected all files?")
        while self.completed is False :
            self.selectFiles()
            self.completed=messagebox.askyesno(title="Merged",message="selected all files?")
        
            
        merged=True
        self.fileName=filedialog.asksaveasfilename(title="Select saveAs filename",filetypes=(("Pdf files","*.pdf"),))
        #print(self.fileName)
        self.merger=PdfFileMerger()
        try:
            for pdf in self.files:
                self.merger.append(pdf)
            self.merger.write(self.fileName)
        except AttributeError:
            merged=False
            self.err=messagebox.showerror(title="No files Selected", message="Please select PDF files")
        if merged==True:
            self.completed=messagebox.askokcancel(title="Merged",message="All files merged")
            self.open=messagebox.askyesno(title="Open Output file?",message="Do you want to open "+self.fileName+"?")
            print(self.open)
            if(self.open is True):
                os.system("start "+self.fileName)
                subprocess.call(["xdg-open",self.fileName])
                
    def selectFiles(self):
        self.newFiles=list((filedialog.askopenfilenames(initialdir="/",title="Select Files",filetypes=(("Pdf files", "*.pdf"),))))
        self.files+=self.newFiles
        if(len(self.newFiles)==len(self.files)):
            self.list.delete(0)
        print(self.files)
        for i in range(len(self.newFiles)):
            self.list.insert(END,str(len(self.files)-len(self.newFiles)+i+1)+". "+str(os.path.split(self.newFiles[i])[1]))
        setattr(self.selectLabel,"text","Selected Files"+str(len(self.files)))
    def deleteFiles(self):
        self.deleteList=list(self.list.curselection())
        
        print(self.deleteList)
        self.confirm=messagebox.askyesno(title="Delete Files",message="Are you sure you want to delete the selected files?")
        if self.confirm is True :
            for i in self.deleteList.sort(reverse=True):
                print(i)
                self.list.delete(i,i)
    def createWidgets(self):
        """creates Button,Label and entry field
        """
        self.developer=Label(self.header,text="PDFMerger",bg="grey90",fg="red",font=("Courier",26,"underline"),width=26)
        self.developer.pack(expand=True,fill="x")
        self.box=LabelFrame(self.middle,height=450,width=150,bg="white",bd=5,relief="flat")
        self.box.pack(expand=True)
        self.box.config(highlightbackground="green")
        self.grid_rowconfigure(1,weight=1)
        self.save=Button(self.box,text="Save as",bg="light grey",height=2,command=self.saveAs)
        self.save.pack(fill="x"
                       )
        self.select=Button(self.box,text="Select Files",bg="light blue",height=2,width=25,command=self.selectFiles,font=("Arial",12))
        self.select.pack(fill="x")
        self.developer=Label(self.footer,text="Developed by Nikhil Mulchandani    M:8758583958 Email: nikmul19@gmail.com",fg="blue",height=2,width=52,bg="white")
        self.developer.pack(expand=True,fill="x")
        self.selectLabel=Label(self.box,text="Selected files",font=("Arial",12,"bold"),width=20,bd=0,height=2,bg="#fbffff",anchor="w",highlightbackground="blue",highlightthickness=1)
        self.selectLabel.pack(fill="x")
        self.list=Listbox(self.box,bg="grey",selectmode=MULTIPLE,fg="white")
        self.list.insert(0,"No files selected")
        self.list.pack(fill="both")
        self.delete=Button(self.box,text="Delete files",bg="blue",width=30,command=self.deleteFiles)
        self.delete.pack()
file=merge()
file.mainloop()
