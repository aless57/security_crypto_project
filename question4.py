import math


def main():
    print("Test du générateur à congruence linéaireSTM avec 1315")
    graine = 1315
    print("Nombre de base : ")
    print(graine)
    graine = STM(graine)
    print("Apres générateur à congruence linéaire STM : ")
    print(graine)

def STM(graine):
    a = 16807
    b = 0
    m = int(math.pow(2,31) - 1)
    print(m)
    for t in range(0,m):
        graine = (a*graine+b) % m
        print(graine)
    return graine 



if __name__ == "__main__":
    main()