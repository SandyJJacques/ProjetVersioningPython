def brute_force():
    mdp_a_touver = ""                                           # La variable est definie
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789&é(-è_çà)=^$*ù!:;,<>°+£¨%µ§/.?~#'{[|`\^@]}¤" # Caractères possibles

    chars_list = list(chars)                                    # Defini la variable chars en liste

    mdp = input("Entrez votre mot de passe : ")                 # L'utilisateur doit rentrer son mot de passe

    while (mdp_a_touver != mdp):                                
        mdp_a_touver = random.choices(chars_list, k=len(mdp))   #tant que le mdp à trouver est different du bon

        print(str(mdp_a_touver))                                

        if (mdp_a_touver == list(mdp)):                         #condition d'arret si mdp trouvé
            print("Le mot de passe est : ", mdp_a_touver)       
            break       
