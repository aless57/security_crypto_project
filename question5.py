import math

def main():
    vGLOBAL = 1315
    print("Test du générateur à congruence linéaire RANDU avec 1315 pendant 1000 tours")
    graine = vGLOBAL
    print("Nombre de base : ")
    print(graine)
    tabRes = RANDU(graine,1000)
    print("Apres générateur à congruence linéaire RANDU : ")
    print(tabRes)

def RANDU(graine,nbMax):
    a = 65539
    b = 0
    m = int(math.pow(2,31))
    tab = [graine]
    fichier = open("test.txt","w")
    for t in range(0,nbMax-1):
        graine = (a*graine+b) % m
        tab.append(graine)
        fichier.write(str(graine)+"\n")
    fichier.close()
    return tab 



if __name__ == "__main__":
    main()