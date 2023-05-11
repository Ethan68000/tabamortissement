
import math

diametre= int(input("Entrez le diametre de l'axe en mm : "))
tours= int(input("Entrez le nombre de tours : "))
print("Calcul de la longueur L par formule :")

l = 0
d = diametre
for i in range(1, tours+1):
    d += 18
    l +=math.pi*(d-18)
    print(f"Tour : {i} - Diametre [mm]: {d} - Longueur enroulée [mm] : {round(l)}")

print(f"Calcul de la longueur L par formule :\nLongueur [mm] pour 10 tours: {l}")