import fractions
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
    print(str(Runs(tabRANDOM,10)))
    fichier.write(str(Runs(tabRANDOM,10))+"\n")
    print("Von Neumann:")
    fichier.write("Von Neumann:\n")
    tabVonNeuman = VonNeuman(graine,1000)
    print(str(Runs(tabVonNeuman,10)))
    fichier.write(str(Runs(tabVonNeuman,10)) +"\n")
    print("RANDU:")
    fichier.write("RANDU:\n")
    tabRANDU = RANDU(graine,1000)
    print(str(Runs(tabRANDU,10)))
    fichier.write(str(Runs(tabRANDU,10)) + "\n")
    print("STM:")
    fichier.write("STM:\n")
    tabSTM = STM(graine,1000)
    print(str(Runs(tabSTM,10)))
    fichier.write(str(Runs(tabSTM,10)) + "\n")
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

def Runs(x, nb):
    pvalue = []
    for nombre in x:
        chaine = ""
        val = 0
        un=0
        cbin = format(nombre, "b")
        for chiffre in cbin:
            if (chiffre == "1"):
                un +=1
        res = un / nb
        if((res - 0.5 ) >= (2 / math.sqrt(nb))):
            pvalue.append(0)
        else:
            for i in range(0, len(chaine)-1):
                if (chaine[i] != chaine[i+1]):
                    val +=1
            val += 1
            num = abs(val - (2*nb*res*(1-res)))
            den = 2*math.sqrt(nb)*res*(1-res)
            if den==0.0:
                break
            fraction = num/den
            pvalue.append(2*(1-stats.norm.cdf(fraction, loc=0, scale=1)))
    pvaluefinale = 0
    for pval in pvalue:
        pvaluefinale += pval
    pvaluefinale = pvaluefinale / len(pvalue)
    return pvaluefinale

if __name__ == "__main__":
    main()