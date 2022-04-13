import math


def main():
    print("Test du générateur à congruence linéaire RANDU avec 1315")
    graine = 1315
    print("Nombre de base : ")
    print(graine)
    graine = RANDU(graine)
    print("Apres générateur à congruence linéaire RANDU : ")
    print(graine)

def RANDU(graine):
    a = 65539
    b = 0
    m = int(math.pow(2,31))
    print(m)
    for t in range(0,m):
        graine = (a*graine+b) % m
        print(graine)
    return graine 



if __name__ == "__main__":
    main()