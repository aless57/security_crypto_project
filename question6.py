import xlwt
import math
import random
from xlwt import Workbook

wb = Workbook()

sheetRAND = wb.add_sheet('RAND')
sheetVonNeumann = wb.add_sheet('VonNeumann')
sheetSTM = wb.add_sheet('STM')
sheetRANDU = wb.add_sheet('RANDU')

def VonNeuman(graine):
    graine = graine * graine
    while not (graine<9999 and graine>0):
        res = str(graine)
        res = res[1:-1]    
        graine = int(res)
    return graine

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

fichier = open("test.txt","w")
fichier.write("Von Neumann:\n")
nbMax = 1000
vGLOBAL = 1315
valVonNeuman = VonNeuman(vGLOBAL)
fichier.write(str(valVonNeuman)+"\n")
tabRANDU = RANDU(vGLOBAL,nbMax)
tabSTM = STM(vGLOBAL,nbMax)


for i in range(1,nbMax):
    sheetRAND.write(i-1,0,random.randint(0,9999))
    sheetVonNeumann.write(i-1,0,valVonNeuman)
    sheetSTM.write(i-1,0,tabSTM[i-1])
    sheetRANDU.write(i-1,0,tabRANDU[i-1])
    valVonNeuman = VonNeuman(valVonNeuman)
    fichier.write(str(valVonNeuman)+"\n")

fichier.write("RANDU:\n")
for i in tabRANDU:
    fichier.write(str(i)+"\n")
fichier.write("STM:\n")
for i in tabSTM:
    fichier.write(str(i)+"\n")

fichier.close()
wb.save('excel_question6.xls')