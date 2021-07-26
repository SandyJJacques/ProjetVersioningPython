def scan_port():



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)



ip = input("IP à scanner : ")
port = input("Port à scanner : ")
port2 = int(port)



if s.connect_ex((ip, port2)):
print("Le port est fermé")



else :
print("Le port est ouvert")



choice = input("Souhaitez-vous scanner un autre port ? [y] [n] : ")



if choice == "y" or choice == "Y":
scan_port()



else:
return("ok")
