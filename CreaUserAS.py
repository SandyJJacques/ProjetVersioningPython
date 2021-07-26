ef create_user(ville):
    create=y

    while create =="y" or create == "Y":
        id1 = input("id : ")
        nom = input("Nom : ")
        prenom = input("Prénom :")
        tel = input("N° de téléphone : ")

        mail = (prenom+"."+nom+"@netway.fr")
        mail = (mail.lower())
        print("Mail : ",mail)
        pwd = password_generator()

        print("Mot de passe : ", pwd)
        mdp = hashlib.sha256(pwd.encode()).hexdigest()
        

        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Projet2020!',
            database='python'
        )
        mycursor = db.cursor()
        sql = ("INSERT INTO %s(id, Nom, Prénom, Tel, Mail, Mot de passe)VALUES(%s, %s, %s, %s, %s) ", ville, id1, nom, prenom, tel, mail, mdp)
        mycursor.execute(sql)
        db.commit()
        return("L'utilisateur a été créé")

        create = input("Souhaitez-vous créer un autre utilisateur ? [y] [n] :")
        if create == "y":
            create_user(ville)
        else:
            return("ok")
    return("ok")
