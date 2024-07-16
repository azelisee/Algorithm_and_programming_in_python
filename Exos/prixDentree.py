# Prix d'entree dans un parc d'amusement en fonction de l'age

#Saisie des donnes:
a=int(input("Entrez votre age svp, a: "))

#Traitement:
if a < 0:
   print("veuillez saisir a nouveau votre age")
a=int(input("Entrez votre age svp, a: "))
if a<5:
   print("le prix est: 0$")
elif a<=9:
   print("le prix est: 5$")
elif a<=17:
   print("le prix est: 7.5$")
elif a<=34:
   print("le prix est: 18.25$")
elif a<=49:
   print("le prix est: 9.75$")
else:
   print("le prix est de 2$")
