def main():
    print("Test de VonNeuman avec 1315")
    graine = 1315
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
    return graine


if __name__ == "__main__":
    main()