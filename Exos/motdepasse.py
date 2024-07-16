# Validation d'un mot de passe

#Affichage du titre:
print("\n\t", 32* "=")
print("\t = Validation d'un mot de passe =")
print("\t", 32* "=", "\n")

#Saisie des donnees:
motDePasse=str(input("\n\t Saisissez le mot de passe : "))
k=len(motDePasse)

if k<=8:
       print("\n\t Le mot de passe est trop court.")
elif k<12 or k==12:
       print("\n\t Le mot de passe est acceptable.")
elif k<16 or k==16:
       print("\n\t Le mot de passe est fort.")      
else:
       print("\n\t Le mot de passe est très fort.")
print("\n\t----  Au revoir  ----")

