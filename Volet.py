
import math

diametre= int(input("Entrez le diametre de l'axe en mm : "))
tours= int(input("Entrez le nombre de tours : "))
print("Calcul de la longueur L par formule :")

l = 0
d = diametre
for i in range(1, tours+1):
    d += 18
    l +=math.pi*(d)
    print(f"Tour : {i} - Diametre [mm]: {d} - Longueur enroulée [mm] : {round(l)}")

print(f"Calcul de la longueur L par formule :\nLongueur [mm] pour 10 tours: {l}")







import math

def d(n):
    return (d0+2*9*n)
    
d0=float(input("entrer le diametre de l'axe en mm"))
n=int(input("entrer le nombre de tours n"))

print("Calcul de la longeur L pour chaque tour:")
L=0
for i in range(n):
    L=L+math.pi*d(i+1)
    print("tour=",i+1,"-""Diametre mm :",round(d(i+1),1),"- Longeur enroulÃ©e [mm]:",round(L))
    
print("calcul de la longeur l par formule:")
c0=math.pi*d(0)
cn=math.pi*d(n-1)
L=(c0+cn)*(n+0)/2
print("Longeur [mm] pour ",n,"tours:", L)
print 
