# script mot_de_passe.py
import csv
from tkinter import *
from tkinter.messagebox import *  # boîte de dialogue



# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('Identification requise')

# Création d'un widget Label (texte 'Login')
Label2 = Label(Mafenetre, text='Login ')
Label2.pack(side=LEFT, padx=5, pady=5)

# Création d'un widget Entry (champ de saisie)
login = StringVar()
Champ = Entry(Mafenetre, textvariable=login, show="", bg='bisque', fg='maroon')
Champ.focus_set()
Champ.pack(side=LEFT, padx=5, pady=5)

# Création d'un widget Label (texte 'Mot de passe')
Label1 = Label(Mafenetre, text='Mot de passe ')
Label1.pack(side=LEFT, padx=5, pady=5)

# Création d'un widget Entry (champ de saisie)
mdp = StringVar()
Champ = Entry(Mafenetre, textvariable=mdp, show='*', bg='bisque', fg='maroon')
Champ.focus_set()
Champ.pack(side=LEFT, padx=5, pady=5)

# Création d'un widget Button (bouton Valider)
Button = Button(Mafenetre, text='Valider', command=verification)
Button.pack(side=LEFT, padx=5, pady=5)

Mafenetre.mainloop()
