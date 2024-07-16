#Titre de l'algorithme: Calcul de la hauteur atteinte par une balle lancée verticalement.

#Affichage du titre:
print("\t",71*"*")
print("\t",2*"*","Calcul de la hauteur atteinte par une balle lancée verticalement ",2*"*")
print("\t",71*"*")

#Déclaration des variables:
#g, l'accélération gravitationnelle en mètre par seconde au carré.
#v0, la vitesse initiale appliquée à la balle en mètre par seconde.
#t, le temps de calcul en millisecondes.
#hballe, la hauteur atteinte par la balle.
#NB: ce sont tous des réelles sauf la durée.

#Affectation de valeur:
g=9.81
d=0
hballe=0.0

#Saisie des données:
v0=float(input("\nSaisissez la valeur de la vitesse v0 en m/s : "))
d=int(input("\nSaisissez la valeur de la durée t en ms : "))

#Traitement:
for t in range(0,d,50):
    hballe=-0.5*g*(t/1000)**2 + v0*(t/1000)
    print("\n\t À t =","%4.0f" %t, " ms la hauteur de la balle est : ", "%3.3f" %hballe, "m")
    if hballe<0:
        break
print("\nFin du programme. ")

    



