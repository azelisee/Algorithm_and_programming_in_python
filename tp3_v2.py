#Titre de l'algorithme: Cryptage de message à base de 3 méthodes différentes.


#------------------------------------------ LA FONCTION AFFICHEMENU ----------------------------------------
def affichemenu():
    print(2*"\n","\t",50*"x")
    print(4*"\t","Menu")
    print("\n\t Option 1 = Le Chiffre de César")
    print("\t Option 2 = Le Chiffre de Vigenère")
    print("\t Option 3 = Le Codage à clé alphabet aléatoire")
    print("\t Option 4 = Quitter")
    print("\n\t",50*"x")
    return()

#------------------------------------------    LA FONCTION RÉPONSE   -----------------------------------------
def reponse():
    print("\n\tVoulez-vous coder un autre message ?")
    Rep = input("\n\t Votre réponse SVP : ")
    if  Rep == "oui":
        lg = " "
        lg = input("\nVeuillez entrer la langue dans lequel le message est écrit SVP : ")
        while lg!= "francais":
            if lg!= "francais":
                print("\t\tErreur!!")
            else:
                break
        if lg == "francais":
            mac = input("\n\tTapez votre message SVP : ")
            affichemenu()
            c = 0 # Le choix
            c = int(input("\nChoisir une option (1, 2, 3 ou 4) SVP : "))
        # Traitement fait après le choix de l'usager:
            while c < 1 or c > 4:
                if c < 1 or c > 4:
                    print("\t\tErreur refaite le choix")
                else:
                    break
            if c == 1:
                
                print("\n\tLe message codé avec le chiffre de césar est  :",lechiffredecésar())
                reponse()
            elif c == 2:
                
                print("\n\tLe message codé avec le chiffre de vigenère est :",lechiffredevigenère())
                reponse()
            elif c == 3:
                
                print("\n\tLe message codé avec la clé aléatoire est :",codageclealéatoire())
                reponse()
            else:
                print("\n\tMerci d'avoir utilisé ce programme, à trés bientot")
   
    else:
        print("\nAu Revoir")
    return 

#------------------------------------------    LA FONCTION DU CHOIX 1   ---------------------------------------
def lechiffredecésar():
    cle = int(input("\nSaisir la clé, nombre entier inférieur à 26 SVP : "))
    alphabet = "abcdefghijklmnopqrstuvwxyz" # Alphabet français.
    mcde = " "   # Le message codé ne contient rien au départ.
    i = 0
    NVli = 0
    for car in mac: 
        i = alphabet.find(car)        # Retour le l'indice du caractère du message par rapport à sa position dans l'alphabet.
        Nvli = i + cle                # Nouvel indice obtenu à l'aide la clé.
        if Nvli > 25:                 # Cas où le nouvel indice dépasse 25 (26 lettres dans l'alphabet).
            Nvli = Nvli % 26          # Nouvel indice égale au reste ou au modulo.
        mcde = mcde + alphabet[Nvli]
    return mcde

#------------------------------------------    LA FONCTION DU CHOIX 2   ---------------------------------------
def lechiffredevigenère():
    motcle = " "
    motcle = input("\nSaisir le mot clé SVP : ")
    alphabet = "abcdefghijklmnopqrstuvwxyz" # Alphabet français.
    mcde = " "   # Le message codé ne contient rien au départ.
    p = 0        # Initialisation des indices du mot clé.
    imac = 0
    imotcle = 0
    imcde = 0
    
    for car in mac:
        imac = alphabet.find(car)            # Retour le l'indice du caractère du message par rapport à sa position dans l'alphabet.
        imotcle = alphabet.find(motcle[p])   # Renvoie de l'indice du caractère du mot clé.
        imcde = imac + imotcle + 1           # Nouvel indice obtenu à l'aide de la clé.
        if imcde > 25:                       # Cas où le nouvel indice dépasse 25 (26 lettres dans l'alphabet).
            imcde = imcde - 26               # On retranche 26 de l'indice du message codé.
        mcde = mcde + alphabet[imcde]
        p = p + 1                        # On anticipe l'indice suivant du mot clé.
        if p >= len(motcle):
            p = 0
    return mcde

#------------------------------------------    LA FONCTION DU CHOIX 3   ---------------------------------------
def codageclealéatoire():
    motcle = " "
    motcle = input("\nSaisir le mot clé SVP : ")
    alphabet = "zyxwvutsrqponmlkjihgfedcba" # Alphabet français renversé.
    mcde = " "   # Le message codé ne contient rien au départ.
    p = 0        # Initialisation des indices du mot clé.
    imac = 0
    imotcle = 0
    imcde = 0
    
    for car in mac:
        imac = alphabet.find(car)            # Retour le l'indice du caractère du message par rapport à sa position dans l'alphabet.
        imotcle = alphabet.find(motcle[p])   # Renvoie de l'indice du caractère du mot clé.
        imcde = imac + imotcle + 1           # Nouvel indice obtenu à l'aide de la clé.
        if imcde > 25:                       # Cas où le nouvel indice dépasse 25 (26 lettres dans l'alphabet).
            imcde = imcde - 26               # On retranche 26 de l'indice du message codé.
        mcde = mcde + alphabet[imcde]
        p = p + 1                        # On anticipe l'indice suivant du mot clé.
        if p >= len(motcle):
            p = 0
    
#-----------------------------------------     LE PROGRAMME PRINCIPAL   ----------------------------------------

    
# Affichage du titre de l'algorithme:
print("\n\t",60*"x")
print("\n\t",3*"x","Cryptage de message à base de 3 méthodes différentes",3*"x")
print("\n\t",60*"x")

print("\n\t!!Veuillez mettre les informations nécessaire au cryptage en minuscules et sans espace SVP!!")

# Déclaration des variables:
lg = " "  # Langue de cryptage.
mac = " "        # Message à crypter.
mcde = " "       # Message codé.
Rep = " "        # Réponse de l'usager pour avoir s'il veut recommencer ou pas.

#Saisie des données:
lg = " "
lg = input("\nVeuillez entrer la langue dans lequel le message est écrit SVP : ")
while lg!= "francais":
    if lg!= "francais":
        print("\t\tErreur!!")
    else:
        break
if lg == "francais":
    mac = input("\n\tTapez votre message SVP : ")
    affichemenu()
    c = 0 # Le choix
    c = int(input("\nChoisir une option (1, 2, 3 ou 4) SVP : "))
    # Traitement fait après le choix de l'usager:
    while c < 1 or c > 4:
        if c < 1 or c > 4:
            print("\t\tErreur refaite le choix")
        else:
            break
    if c == 1:
        print("\n\tLe message codé avec le chiffre de césar est  :",lechiffredecésar())
        reponse()
    elif c == 2:
        
        print("\n\tLe message codé avec le chiffre de vigenère est :",lechiffredevigenère())
        reponse()
    elif c == 3:
        
        print("\n\tLe message codé avec la clé aléatoire est :",codageclealéatoire())
        reponse()
    else:
         print("\n\tMerci d'avoir utilisé ce programme, à trés bientot")
        
        
    
        
        
        

        
    

         
        
  

    
    
        
    
        
        


