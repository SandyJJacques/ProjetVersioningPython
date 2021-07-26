def boite_a_outils():
print("1- Scan de ports")
print("2- Simulation force brute")
print("3- Quitter")

choice = input("Ques ouhaites-vous faire ? ")

if int(choice) == 1:

scan_port()

boite_a_outils()

elif int(choice) == 2:

brute_force()

boite_a_outils()

elif int(choice) == 3:

return("done")

else:

print("Merci de rentrer une valeur valide \n")
boite_a_outils()
