import requests
from tkinter import *
from tkinter import messagebox
def downloader():
    r = requests.get(Url_entry.get())
    with open(filename_entry.get()+ext_entry.get(), "wb") as file:
        file.write(r.content)
    if(r.status_code == 200):
        messagebox.showinfo("process status", "download complete")
        quit()

mainbox=Tk()
mainbox.title("MY DOWNLOADER")
nameurl=Label(mainbox,text = "Enter Url")
filename=Label(mainbox,text = "file name :")
ext=Label(mainbox,text = "file extention :")

Url_entry = Entry(mainbox)
filename_entry = Entry(mainbox)
ext_entry=Entry(mainbox)

download = Button(mainbox,text="start download",fg="red",bg="black",command = downloader)

nameurl.grid(row = 0,column=0,sticky=W+E+N+S )
Url_entry.grid(row = 0,column = 1,columnspan=5,sticky=W+E+N+S )
filename.grid(row = 1,column = 0,sticky=W+E+N+S )
filename_entry.grid(row = 1,column = 1,columnspan=5,sticky=W+E+N+S )
ext.grid(row=2,column=0,sticky=W+E+N+S )
ext_entry.grid(row=2,column=1,sticky=W+E+N+S )
download.grid(columnspan = 8,sticky=W+E+N+S )

mainbox.mainloop()