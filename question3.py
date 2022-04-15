def main():
    vGLOBAL = 1315
    print("Test de VonNeuman avec 1315")
    graine = vGLOBAL
    print("Nombre de base : ")
    print(graine)
    graine = VonNeuman(graine)
    print("Apres algo VonNeuman : ")
    print(graine)

def VonNeuman(graine):
    graine = graine * graine
    while not (graine<9999 and graine>0):
        res = str(graine)
        res = res[1:-1]    
        graine = int(res)
    fichier = open("test.txt","w")
    fichier.write(str(graine))
    fichier.close()
    return graine


if __name__ == "__main__":
    main()