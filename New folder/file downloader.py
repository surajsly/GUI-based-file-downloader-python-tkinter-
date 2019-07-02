import requests
from tkinter import *
from tkinter import messagebox

#downloader funtion is responsible for downloading the file

def downloader():
    r = requests.get(Url_entry.get())
    with open(filename_entry.get()+ext_entry.get(), "wb") as file:
        file.write(r.content)
    if(r.status_code == 200): # if downloaded then show this 
        messagebox.showinfo("process status", "download complete")
        quit()

# main window
mainbox=Tk()
mainbox.title("MY DOWNLOADER") #main windows name
mainbox.geometry("1024x250")   #main windos size
photo = PhotoImage(file = r"alpha.png") #creating a object (photot) for a image (alpha.png) into memory
mainbox.configure(background="light sky blue")# setting background
mainbox.iconbitmap("fire.ico") #setting icon 

 
# creating the lables in memory
nameurl=Label(mainbox,text = "Enter Url",anchor="center",font = ('Comic Sans MS',10),bg="plum1") 
filename=Label(mainbox,text = "file name :",anchor="center",font = ('Comic Sans MS',10),bg="plum1")
ext=Label(mainbox,text = "file extension :",anchor="center",font = ('Comic Sans MS',10),bg="plum1")


#creating the entry fields in memory
Url_entry = Entry(mainbox,bg="peach puff",font = ('Comic Sans MS',10))
filename_entry = Entry(mainbox,bg="peach puff",font = ('Comic Sans MS',10))
ext_entry=Entry(mainbox,bg="peach puff",font = ('Comic Sans MS',10))

#creating a button in memory and linking it to downloader
download = Button(mainbox,text="  start download",fg="black",compound=LEFT,command = downloader,anchor="center",image = photo,font = ('Comic Sans MS',10),bg="plum1")

#managing all the widgits to the main window
nameurl.grid(row = 0,column=0,sticky=W+E+N+S,pady=15,padx=10 )
Url_entry.grid(row = 0,column = 1,columnspan=5,sticky=W+E+N+S,ipadx=400,pady=15)
filename.grid(row = 1,column = 0,sticky=W+E+N+S,pady=15,padx=10 )
filename_entry.grid(row = 1,column = 1,columnspan=5,sticky=W+E+N+S,ipadx=400,pady=15 )
ext.grid(row=2,column=0,sticky=W+E+N+S,pady=15,padx=10 )
ext_entry.grid(row=2,column=1,sticky=W+E+N+S,ipadx=400,pady=15 )
download.grid(row=4,pady=20,columnspan = 5,sticky=N+W+E)


# creating an infinite loop
mainbox.mainloop()
