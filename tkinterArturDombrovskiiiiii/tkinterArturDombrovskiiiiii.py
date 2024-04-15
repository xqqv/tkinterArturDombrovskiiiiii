from tkinter import *

def tehtudvalik(var):
    f = var.get()
    if f:
        parooli_sisestus.configure(show="")
    else:
        parooli_sisestus.configure(show="*")

def textpealkirjasse():
    t = parooli_sisestus.get()
    pealkiri.configure(text=t)
    parooli_sisestus.delete(0, END)

def registreerimine():              
    kasutajanimi = kasutajanime_sisestus.get()
    parool = parooli_sisestus.get()

    if kasutajanimi and parool:
        with open("kasutajad.txt", "a") as f:
            f.write(f"{kasutajanimi},{parool}\n")
        registreerimise_teade.config(text="Kasutaja registreeritud!", fg="green")
    else:
        registreerimise_teade.config(text="Kasutajanimi või parool puudub!", fg="red")

def autoriseerimine():
    kasutajanimi = kasutajanime_sisestus.get()
    parool = parooli_sisestus.get()

    with open("kasutajad.txt", "r") as f:
        kasutajad = f.readlines()

    kasutajad = [kasutaja.strip().split(",") for kasutaja in kasutajad]
    if [kasutajanimi, parool] in kasutajad:
        autoriseerimise_teade.config(text="Kasutaja autoriseeritud!", fg="green")
    else:
        autoriseerimise_teade.config(text="Vale kasutajanimi või parool!", fg="red")

def muuda_parool_window():
    def muuda_parool():
        kasutajanimi = kasutajanimi_entry.get()
        vana_parool = vana_parooli_entry.get()
        uus_parool = uus_parooli_entry.get()
        kinnita_parool = kinnita_parooli_entry.get()

        if uus_parool != kinnita_parool:
            muuda_parooli_teade.config(text="Uued paroolid ei kattu!", fg="red")
            return

        with open("kasutajad.txt", "r") as f:
            kasutajid = f.readlines()

        kasutajid = [kasutaja.strip().split(",") for kasutaja in kasutajid]

        found = False
        for kasutaja in kasutajid:
            if kasutaja[0] == kasutajanimi:
                if kasutaja[1] == vana_parool:
                    kasutaja[1] = uus_parool
                    found = True
                    break

        if found:
            with open("kasutajad.txt", "w") as f:
                for kasutaja in kasutajid:
                    f.write(','.join(kasutaja) + '\n')
            muuda_parooli_teade.config(text="Parool edukalt muudetud!", fg="green")
            muuda_parool_aken.destroy()
        else:
            muuda_parooli_teade.config(text="Kasutajanimi või vana parool on vale!", fg="red")

    muuda_parool_aken = Tk()
    muuda_parool_aken.title("Muuda parool")
    muuda_parool_aken.geometry("300x200")

    kasutajanimi_label = Label(muuda_parool_aken, text="Kasutajanimi:")
    vana_parooli_label = Label(muuda_parool_aken, text="Vana parool:")
    uus_parooli_label = Label(muuda_parool_aken, text="Uus parool:")
    kinnita_parooli_label = Label(muuda_parool_aken, text="Kinnita uus parool:")

    kasutajanimi_entry = Entry(muuda_parool_aken)
    vana_parooli_entry = Entry(muuda_parool_aken, show="*")
    uus_parooli_entry = Entry(muuda_parool_aken, show="*")
    kinnita_parooli_entry = Entry(muuda_parool_aken, show="*")

    muuda_button = Button(muuda_parool_aken, text="Muuda parool", command=muuda_parool)

    kasutajanimi_label.grid(row=0, column=0, padx=10, pady=5)
    vana_parooli_label.grid(row=1, column=0, padx=10, pady=5)
    uus_parooli_label.grid(row=2, column=0, padx=10, pady=5)
    kinnita_parooli_label.grid(row=3, column=0, padx=10, pady=5)

    kasutajanimi_entry.grid(row=0, column=1, padx=10, pady=5)
    vana_parooli_entry.grid(row=1, column=1, padx=10, pady=5)
    uus_parooli_entry.grid(row=2, column=1, padx=10, pady=5)
    kinnita_parooli_entry.grid(row=3, column=1, padx=10, pady=5)

    muuda_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    muuda_parool_aken.mainloop()


aken = Tk()
aken.geometry("500x500")
aken.title("Programma")
aken.configure(bg="#e74c3c")  
aken.iconbitmap("bolt.ico")

pealkiri = Label(aken,
                 text="Tere Tulemast!!",
                 bg="#c0392b",  
                 fg="#ffffff",  
                 cursor="star",
                 font="Times_New_Roman 16",
                 justify=CENTER,
                 height=3, width=26)

raam = Frame(aken, bg="#e74c3c")  

muuda_parool_nupp = Button(raam,
                           text="Muuda parool",
                           bg="#c0392b",  
                           fg="white",  
                           font="Times_New_Roman 14 bold",
                           width=20,
                           command=muuda_parool_window)

registreeri_nupp = Button(raam,
                          text="Registreeri",
                          bg="#c0392b",  
                          fg="white",  
                          font="Times_New_Roman 14 bold",
                          width=20,
                          command=registreerimine)

autoriseeri_nupp = Button(raam,
                          text="Autoriseeri",
                          bg="#c0392b",  
                          fg="white",  
                          font="Times_New_Roman 14 bold",
                          width=20,
                          command=autoriseerimine)

kasutajanime_silt = Label(raam, text="Kasutajanimi:", fg="white", bg="#e74c3c", font="Times_New_Roman 14 bold")  
parooli_silt = Label(raam, text="Parool:", fg="white", bg="#e74c3c", font="Times_New_Roman 14 bold")  

kasutajanime_sisestus = Entry(raam,
                              bg="#ffffff",  
                              fg="#111211",
                              font="Times_New_Roman 14",
                              width=20)

parooli_sisestus = Entry(raam,
                         bg="#ffffff",  
                         fg="#111211",
                         font="Times_New_Roman 14",
                         width=20,
                         show="*")

parooli_naita_checkbox = Checkbutton(raam,
                                     text="Näita parooli",
                                     bg="#e74c3c",  
                                     fg="white",  
                                     font="Times_New_Roman 12",
                                     command=lambda: tehtudvalik(var))

registreerimise_teade = Label(raam, text="", font="Times_New_Roman 12", bg="#e74c3c", fg="white") 
autoriseerimise_teade = Label(raam, text="", font="Times_New_Roman 12", bg="#e74c3c", fg="white")  
muuda_parooli_teade = Label(raam, text="", font="Times_New_Roman 12", bg="#e74c3c", fg="white")  # Red message label

pealkiri.pack(pady=20)
raam.pack(pady=20)
muuda_parool_nupp.grid(row=0, column=0, padx=10, pady=10)
registreeri_nupp.grid(row=1, column=0, padx=10, pady=10)
autoriseeri_nupp.grid(row=2, column=0, padx=10, pady=10)
kasutajanime_silt.grid(row=3, column=0, padx=10, pady=10)
kasutajanime_sisestus.grid(row=3, column=1, padx=10, pady=10)
parooli_silt.grid(row=4, column=0, padx=10, pady=10)
parooli_sisestus.grid(row=4, column=1, padx=10, pady=10)
parooli_naita_checkbox.grid(row=4, column=2, padx=10, pady=10)
registreerimise_teade.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
autoriseerimise_teade.grid(row=6, column=0, columnspan=3, padx=10, pady=10)
muuda_parooli_teade.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

var = BooleanVar()
aken.mainloop()
