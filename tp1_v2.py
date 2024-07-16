# Titre de l'algorithme: Calcul de l'aire et du volume d'une canette.

#Declaration des variables:
#pi, r, h  Avec "pi" le rapport constant de la circonférence d'un cercle à son diamètre, r" le rayon de la canette et "h" sa hauteur.

#Affichage du titre de l'algorithme:
print("\n","\t",58*"*")
print("\n","\t",2*"*","\t","Calcul de l'aire et du volume d'une canette","\t",2*"*")
print("\n","\t",58*"*")
print("\n")

pi=float(3.14159) #Affectation de valeur à pi.

#Saisie des variables:
r=float(input("Saisissez le rayon (m) SVP   : "))
h=float(input("Saisissez la hauteur (m) SVP : "))
print("\n","\t",42*"-")

aire=float(2*pi*r**2+2*pi*r*h) #Affectation de valeur à l'aire (sa formule de calcul).
volume=float(pi*r**2*h) #Affectation de valeur au volume (sa formule de calcul).
Quitter=str("Au revoir")

#On demande à l'utilisateur de choisir une des options du menu suivant:
#Affichage du Menu:
print(2*"\t","     Menu : Choix de calcul")
print("\n","\t","Option 1 = Calcul et affichage de l'aire")
print("\t","Option 2 = Calcul et affichage du volume")
print("\t","Option 3 = Quitter")
print("\t",42*"-")

#Entrée du choix de l'utilisateur:
c=int(input("\nSaisissez une option (1, 2 ou 3)  SVP : ")) #"c",le choix de l'utilisateur.

#Traitement fait après choix de l'utilisateur:
if c==1:
   print("\n","\t","l'aire est = ",round(aire,2),"m2")
elif c==2:
     print("\n","\t","le volume est = ",round(volume,2),"m3")
elif c==3:
     print("\n","\t","Au revoir")
else:
     print("\n","\t","Erreur")
     c=int(input("\nSaisissez une option (1, 2 ou 3)  SVP : "))
   
       

