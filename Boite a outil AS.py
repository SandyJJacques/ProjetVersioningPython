from tkinter import *
from tkinter.messagebox import * # boîte de dialogue


# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('Boite à outils')

# Création d'un widget Label (texte ' 1- Scan port')
bouton1 = Button(Mafenetre, text = ' 1- Scan port ')
bouton1.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Label (texte '2- Attaque force brute')
bouton2 = Button(Mafenetre, text = ' 2- Attaque force brute ')
bouton2.pack(side = LEFT, padx = 5, pady = 4)

# Création d'un widget Label (texte '0- Quitter')
bouton3 = Button(Mafenetre, text = ' 0- Quitter ')
bouton3.pack(side = LEFT, padx = 5, pady = 2)


