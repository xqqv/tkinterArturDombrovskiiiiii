
from tkinter import*

def tehtudvalik(var):
    f=var.get()
    if f:
        texbox.configure(show="")
    else:
        texbox.configure(show="*")
def textpealkirjasse():
    t=texbox.get()
    pealkiri.configure(text=t)
    texbox.delete(0,END)
aken=Tk()
aken.geometry("500x500")
aken.title("Akna pealkiri")
aken.configure(bg="#13e0eb")
aken.iconbitmap("icon3.ico")
pealkiri=Label(aken,
                text="Põhielemendid",
                bg="#9edb8f",
                fg="#18420d",
                cursor="star",
                font="Britanic_Bold 16",
                justify=CENTER,
                height=3,width=26)
raam=Frame(aken)
texbox=Entry(raam,
             bg="#18420d",
             fg="#9edb8f",
             font="Britanic_Bold 16",
             width=16,
             show="*")
pilt=PhotoImage(file="eye.png")
var=BooleanVar() #IntVar(), StringVar()
valik=Checkbutton(raam,
                  image=pilt, #text="Punkt1
                  variable=var,
                  onvalue=True,
                  offvalue=False,
                  command=lambda:tehtudvalik(var))
#valik.deselect()
nupp=Button(raam,
            text="Vajuta mind",
            bg="#9edb8f",
            fg="#18420d",
            font="Britanic_Bold 16",
            width=16,
            command=textpealkirjasse)

pealkiri.pack()
raam.pack()
texbox.grid(row=0,column=0) #raami sees
valik.grid(row=0,column=1) #raami sees
nupp.grid(row=0,column=2) #raami sees
aken.mainloop()
