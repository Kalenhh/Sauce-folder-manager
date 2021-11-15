#coding:utf-8

from tkinter import*
from tkinter.filedialog import *
import random

app = Tk()
app.title("Sauce Folder")
app.minsize(600,400)

main_frame = Frame(app,bg="yellow")
main_frame.pack(fill=BOTH,expand=1)


#-----------------------------------------------------------------------------------------------------------------

directory = "archive.txt"
quantite = IntVar()
resultat = StringVar()
sauce = StringVar()
randomV = StringVar()


#Fonction data :----------------------------------------------------------------------------------------------------------

def comparer_doublon() :
	with open(directory,"r") as liste_number :
		liste_number_lignes = liste_number.readlines()
		for element in liste_number_lignes :
			if int(element) == int(sauce.get()) :
				resultat.set("deja dans la liste")
				return
		resultat.set("pas dans  liste")

def eliminer_doublon() :
	global resultat
	with open(directory,"r") as liste_number :
		liste_number_lignes = liste_number.readlines()
		liste_clear = []
		nombre_doublon = 0
		for element in liste_number_lignes :
			if element not in liste_clear :
				liste_clear.append(element)
				continue
			else :
				nombre_doublon = nombre_doublon+1
		resultat.set(str(nombre_doublon) +" sauce en doublon ont été enlevé de l'Archive")

	with open(directory,"w") as liste_number :
		liste_number.writelines(liste_clear)

def quantity() :
	global quantite
	with open(directory,"r") as liste_number :
		liste_number_lignes = liste_number.readlines()
		quantite.set(int(len(liste_number_lignes)))

def randomF() :
	global randomV
	with open(directory,"r") as liste_number :
		liste_number_lignes = liste_number.readlines()
		randomV.set(random.choice(liste_number_lignes))
		"""(liste_number_lignes[Random.randint(0, 4)])"""

def ajouter() :
	global sauce
	with open(directory,"r") as liste_number :
		liste_number_lignes = liste_number.readlines()
		liste_number_lignes.append("\n"+sauce.get())
	with open(directory,"w") as liste_number :
		liste_number.writelines(liste_number_lignes)
		resultat.set(sauce.get()+"ajouté à l'Archive")

#Fonction Tk.Frame :-------------------------------------------------------------------------------------------------------------

def menu():
	FrameMenu = Frame(main_frame,bg="blue",borderwidth=10)
	FrameMenu.pack(side="left",fill=BOTH)

	comparer = Button(FrameMenu,text="Comparer",command=frame_comparer).pack(fill=BOTH)

	doublon = Button(FrameMenu,text="clear",command=frame_doublon).pack(fill=BOTH)

	stat = Button(FrameMenu,text="stat",command=frame_stat).pack(fill=BOTH)

	ajout = Button(FrameMenu,text="Ajouter",command=frame_ajout).pack(fill=BOTH)

	randomVee = Button(FrameMenu,text="random",command=frame_random).pack(fill=BOTH,side="bottom")

	fen = Button(FrameMenu,text="new",command=frame_frame).pack(fill=BOTH)

def frame_frame() :
	recreate()
	new = Tk()
	new.title("ok")
	new.minsize(200,200)
	fr = Frame(new,bg="blue")
	fr.pack(fill=BOTH,expand=1)
	sp = Label(fr,text="newwwwwwwwwww").pack()  #A VOIR 
	new.mainloop()

def recreate():
	global frame_affichage
	global sauce
	global resultat

	sauce.set("")
	resultat.set("")

	frame_affichage.destroy()
	frame_affichage = Frame(main_frame)
	frame_affichage.pack(side="right",fill=BOTH,expand=1)


def frame_stat():
	recreate()
	quantity()
	stat = Label(frame_affichage,text=("il y a " + str(quantite.get()) + " sauce")).pack()

def frame_comparer():
	recreate()
	entre= Entry(frame_affichage,textvariable=sauce).pack()
	comparer = Button(frame_affichage,text="comparer",command= comparer_doublon).pack()
	sortie = Label(frame_affichage,textvariable=resultat).pack()
	sorti = Label(frame_affichage,textvariable=sauce).pack()

def frame_doublon():
	recreate()
	elim = Button(frame_affichage,text="clear rrrrr",command=eliminer_doublon).pack()
	s4 = Label(frame_affichage,textvariable=resultat).pack()
		
def frame_random() :
	recreate()
	randomV.set("")
	b1 = Button(frame_affichage,text="generer un random",command=randomF).pack()
	s5 = Label(frame_affichage,textvariable=randomV).pack()



def frame_ajout():
	recreate()
	entre = Entry(frame_affichage,textvariable=sauce).pack()
	ajoutereeeeee = Button(frame_affichage,text="Ajouter",command=ajouter).pack()
	lop = Label(frame_affichage,textvariable=resultat).pack()

#Programme :---------------------------------------------------------------------------------------------------------

menu()

frame_affichage = Frame(main_frame)
frame_affichage.pack(side="right",fill=BOTH,expand=1)



app.mainloop()