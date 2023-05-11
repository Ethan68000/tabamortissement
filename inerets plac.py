placement = int(input("Entrez le placement de départ : "))
versementmen= int(input("Entrez le montant du versement mensuel : "))
taux = float(input("Entrez le taux annuel en % : "))
annees = int(input("Entrez le nombre d'années : "))
banque = placement

for i in range(annees):
    banque += 12*versementmen
    banque *= (1+taux/100)

#for i in range(annees*12):
    #banque += versementmen
    #banque *= (1+taux/12/100)

print(f"Le capital acquis avec intérêts est de {round(banque, 2)} euros au bout de {round(annees)} avec des versements mensuels de {round(versementmen, 2)} euros")
print(f"Les intérêts gagnés au taux annuel de {round(taux, 2)} % sont de {round(banque - placement - 12*annees*versementmen, 2)}")
print(f"Sans placement avec interets le capital acquis serait de {round(placement + 12*annees*versementmen)} euros")
