# Résolution d'un système de deux équations à deux inconnues.

#Affichage du titre:
print("\n\t",64*"*")
print("\t","** Résolution d'un système de deux équations à deux inconnues **")
print("\t",64*"*")

#Saisie des données:
a1 =float(input("\nSaisissez la valeur de a1 SVP  : "))
b1 =float(input("Saisissez la valeur de b1 SVP  : "))
c1 =float(input("Saisissez la valeur de c1 SVP  : "))
a2 =float(input("Saisissez la valeur de a2 SVP  : "))
b2 =float(input("Saisissez la valeur de b2 SVP  : "))
c2 =float(input("Saisissez la valeur de c2 SVP  : "))

#Affectation des valeurs:
d=a1*b2 - a2*b1
dx=c1*b2 - c2*b1
dy=a1*c2 - a2*c1

#Traitement:
if d==0:
    if dx==0 or dy==0:
        print("\n\tSystème indeterminé, les deux droites sont confondues")
    elif dx!=0 or dy!=0:
        print("\n\tSystème impossible, les 2 droites sont parallèles")
else:
    print("\n\tSolution du système: (x ; y) =","(",round(dx/d,2)," ; ",round(dy/d,2),")")
print("\n\t---- À bientot ----")
