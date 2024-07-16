#Affichage du titre:
print("\n\t",56*"*")
print("\t",2*"*","  Calcul du montant total toutes taxes comprises  ",2*"*")
print("\t",56*"*")

#Déclaration des variables:
p1=float
p2=float
p3=float

#Affectation:
ptht=p1+p2+p3
tps=0.05*ptht
tvq=0.09975*ptht
prttc=ptht+tps+tvq

#Saisie des données:
p1=float(input("\n\t Saisissez le prix de l'article 1 : "))
p2=float(input("\t Saisissez le prix de l'article 2 : "))
p3=float(input("\t Saisissez le prix de l'article 3 : "))

#Affichage de la facture:
print("\n\t le montant total est  :",round(ptht,2))
print("\t la taxe fédérale est  :",round(tps,2))
print("\t la taxe provinciale est  :",round(tvq))

print("\n\t le montant à payer est  :",round(prttc,2))

print(2*"\n","Merci d'avoir magasiné chez nous.")
print("Nous sommes heureux de vous avoir comme client.")
print("Au plaisir de vous servir une autre fois.")
