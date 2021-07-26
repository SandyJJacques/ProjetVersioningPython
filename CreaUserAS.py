import csv
import random
import string
import hashlib

##Création de la condition de lancement de création de user
create='Y'                                                                      

##Verification de condition de creation de user
while create == 'Y' or create == 'y':

    ##Attribution du csv en fonction du site saisi par l'admin
    site=input("Site de l'utilisateur [GRE] [REN] [STR]: ")
    if site != 'GRE' or site != 'REN' or site != 'STR':
        site=input('Veuillez saisir un site correct [GRE, REN ou STR] : ')
    siteuser=('User'+site+'.csv')                                               

    ##Saisie des informations du user  
    Nom=input("NOM de l'utilisateur : ")                                            
    Prenom=input("Prénom de l'utilisateur : ")
    Tel=input("N° de telephone de l'utilisateur :")
    longueur=len(Tel)
    if longueur != 10:
        Tel=input("Le numéro de téléphone n'est pas valide. Merci de la saisir à nouveau : ")

    ##Creation du mail en fonction du nom et prenom
    Mail=(Prenom+'.'+Nom+'@netway.fr')
    Mail=(Mail.lower())
    print(Mail)

    ##Génération du pwd                        
    mot_de_passe=string.ascii_letters+string.digits
    ##Initialisation du pwd aléatoire
    passwd=""
    for i in range(12):         ##pwd de taille 12
        passwd+=mot_de_passe[random.randint(0,len(mot_de_passe)-1)]
    salt='Netway'

    ##Ajout du nouveau user au fichier csv de son site
    with open(siteuser,'a',newline='', encoding='utf-8') as fichiercsv:
        writer=csv.writer(fichiercsv, delimiter=';')
        writer.writerow([Nom, Prenom, Mail, Tel, passwd])

    ##Demande si ajout d'un nouveau user ou non
    create=input("Voulez-vous créer un autre utilisateur ? [Y] [N] ")

fichiercsv.close() ##Fermeture du fichier csv
