'dient der suche von IP Adressen im gleichen netzwerk. Nur leider etwas Langsam'
import subprocess
import socket

# Suchradius
von = 0
bis = 255

# local Host
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

Zaehler = 0     # zähler der gefundenen Netzwerkteilnehmer
outList = []    # Lister der Netzwerkteilnehmer



for ping in range(von, bis):
    address = "192.168.0." + str(ping)

    res = subprocess.call(['ping', '-w', '1', address])
    if res == 0:

        sockInfo = socket.getnameinfo((str(address), 443), socket.NI_NOFQDN);
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        print("ping to", address, " OK ", sockInfo)
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        outList.append( address+" "+str(sockInfo))
        Zaehler = Zaehler + 1
    elif res == 2:
        print("no response from", address)
    else:
        print("ping to", address, "failed!")


for i in range (von, Zaehler+1):
    print("----------------------------------------------")
    print(i + 1, "/", Zaehler, " ", outList[i])


beenden = input("Zum beenden beliebiege Taste druecken.")