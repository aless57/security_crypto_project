import scipy.stats as stats
import math
import random

def main():
    vGLOBAL = 1315
    fichier = open("test.txt","w")
    print("Test de Frequency sur VonNeumann")
    graine = vGLOBAL
    print("Nombre de base : ")
    print(graine)
    tabRANDOM = [random.randint(0,999)]
    for i in range(0,998):
        tabRANDOM.append(random.randint(0,999))
    print("RANDOM:")
    fichier.write("RANDOM:\n")
    print(str(Frequency(tabRANDOM)))
    fichier.write(str(Frequency(tabRANDOM))+"\n")
    print("Von Neumann:")
    fichier.write("Von Neumann:\n")
    tabVonNeuman = VonNeuman(graine,1000)
    print(str(Frequency(tabVonNeuman)))
    fichier.write(str(Frequency(tabVonNeuman)) +"\n")
    print("RANDU:")
    fichier.write("RANDU:\n")
    tabRANDU = RANDU(graine,1000)
    print(str(Frequency(tabRANDU)))
    fichier.write(str(Frequency(tabRANDU)) + "\n")
    print("STM:")
    fichier.write("STM:\n")
    tabSTM = STM(graine,1000)
    print(str(Frequency(tabSTM)))
    fichier.write(str(Frequency(tabSTM)) + "\n")
    fichier.close()

def VonNeuman(graine,nbMax):
    tabRes = [graine]
    for i in range (0,nbMax-1):
        graine = graine * graine
        while not (graine<9999 and graine>0):
            res = str(graine)
            res = res[1:-1]    
            graine = int(res)
        tabRes.append(graine)
    return tabRes
    
def RANDU(graine,nbMax):
    a = 65539
    b = 0
    m = int(math.pow(2,31))
    tab = [graine]
    for t in range(0,nbMax-1):
        graine = (a*graine+b) % m
        tab.append(graine)
    return tab

def STM(graine,nbMax):
    a = 16807
    b = 0
    m = int(math.pow(2,31) - 1)
    tab = [graine]
    for t in range(0,nbMax-1):
        graine = (a*graine+b) % m
        tab.append(graine)
    return tab 

def Frequency(x, nb = 1):
    incr = 0
    pvalue = []
    incr = 0
    for nombre in x:
        cbin = format(nombre, "b")
        for chiffre in cbin:
            if (chiffre == "0"):
                incr -= 1
            elif (chiffre == "1"):
                incr += 1
        
        Sobs = abs(incr) / math.sqrt(nb)
        pvalue.append(2*(1-stats.norm.cdf(Sobs, loc=0, scale=1)))
        incr = 0
        
    pvaluefinale = 0
    for pval in pvalue:
        pvaluefinale += pval
    pvaluefinale = pvaluefinale / len(pvalue)
    return pvaluefinale

if __name__ == "__main__":
    main()