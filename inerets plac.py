placement = float(input("Entrez le placement de départ : "))
versementmen= float(input("Entrez le montant du versement mensuel : "))
taux = float(input("Entrez le taux annuel en % : "))
annees = int(input("Entrez le nombre d'années : "))
banque = placement

a = int(input("Entrez 1 pour annuel ou 2 pour mensuel"))

while True:
    if a == 1:
        for i in range(annees):
            banque += 12*versementmen
            banque *= (1+taux/100)
        break
    elif a == 2:
        for i in range(annees*12):
             banque += versementmen
             banque *= (1+taux/12/100)

print(f"Le capital acquis avec intérêts est de {round(banque, 2)} euros au bout de {round(annees)} avec des versements mensuels de {round(versementmen, 2)} euros")
print(f"Les intérêts gagnés au taux annuel de {round(taux, 2)} % sont de {round(banque - placement - 12*annees*versementmen, 2)}")
print(f"Sans placement avec interets le capital acquis serait de {round(placement + 12*annees*versementmen)} euros")






pour le 2
placement= float(input("Entrez le placement de départ : "))
versement=float(input("Entrez le montant du versement annuel en % : "))
taux = float(input("Entrez le taux annuel en % : "))
annees = int(input("Entrez le nombre d'années : "))
banque = placement
for i in range(annees):
    banque += versement
    banque += (1+taux/12/100)

print(f"Le capital acquis avec des intérêts est de {round(banque, 2)} euros au bout de {round(annees)} avec des versements mensuels de {round(versement, 2)} euros ")
print(f"Les intérêts gagné au tax annuel de {round(taux, 2)} % sont de {round(banque - placement - 12*annees*versement, 2)}")
print(f"Sans placement avec intérêts le capital acquis serait de {round(placement + 12*annees*versement)} euros")
