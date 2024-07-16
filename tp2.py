#Titre de l'algorithme: Calcul de la moyenne à l'aide d'une liste de notes (en %) saisies au clavier.


#Affichage du titre:
print("\n\t",84*"*")
print("\t","*"," Calcul et affichage de la moyenne et de la mention à l'aide des listes et menu ","*")
print("\t",84*"*")

#Saisie des données:
N=int(input("\n\t Saisir le nombre de notes pour le calcul de la moyenne : ")) #L'utilisateur rentre le nombre de notes. 
print()
ListeNotes=[] #La liste des notes est vide au départ.
for i in range(N):
    print("Saisir la note",i+1, "en %", end = " : ") #On lui permet de mettre autant de notes qu'il veut en fonction.
    n=float(input()) 
    ListeNotes.append(round(n)) #Ajout successif des notes dans la liste. 
    ListeNotes=(ListeNotes) #La liste vide au départ est maintenant remplie des notes qu'on y a ajouté.
print("\n\t","ListeNotes = ",ListeNotes) #Affichage de la liste des notes final.

print("\n\t",52*"-")
print("\t","            Menu : Choix de calcul de la moyenne")

#Enumération des options, éléments du menu:
print("\n\t","Option 1 = Pondération égale")
print("\t","Option 2 = Pondération différente")
print("\t","Option 3 = Quitter")
print("\t",52*"-")


#Traitement fait après le choix de l'utilisateur:
#Cas ou le choix n'est pas dans l'option:
c=0
#Tant que le choix ne fait pas parti du menu on redemandera à l'utilsateur de saisir.
while c<1 or c>3:
    c=int(input("\nSaisissez une option (1, 2 ou 3) SVP : ")) #Saisie du choix de l'utilisateur ( avec "c" le choix fait par l'utilisateur).
    if c<1 or c>3:
        print("\n\t","Erreur, choisissez une option s'il vous plait !") 
    else:
        break

#Cas de l'option 1:
if c==1:
    ListeNotes=(ListeNotes) #On reprend les notes saisies au départ pour le calcul de la moyenne.
    sn=0
    m=0
    k=0
    x=len(ListeNotes)
    for k in range(x):
        sn=sn+ListeNotes[k] #Cumule des notes pour faire la somme.
        m=round(sn/N)
    if m<60:
        print("\n\tla moyenne est : ",(m),"% --->  Cours échoué")
    elif m>=60 or m<=69:
        print("\n\tla moyenne est : ",(m),"% --->  Cours réussi avec mention acceptable")
    elif m>=70 or m<=79:
        print("\n\tla moyenne est : ",(m),"% --->  Cours réussi avec mention assez bien")
    elif m>=80 or m<=89:
        print("\n\tla moyenne est : ",(m),"% --->  Cours réussi avec mention bien")
    else:
        print("\n\tla moyenne est : ",(m),"% --->  Cours réussi avec mention très bien")
    
    
#Cas de l'option 2:
elif c==2:
     print("\n\t!!! Attention, la somme des pondérations doit etre égale à 100% !!!")
     ListePondérations=[] #La liste des pondérations est également vide au départ. 
     sp=0 # La somme des pondération initialisée à zéro.
     r=0
     mp=0 # La moyenne pondérée initialisée à zéro.
     for j in range(len(ListeNotes)): #Le nombre de pondérations sera le meme que le nombre de note.
         print("\nSaisir la pondération ",j+1, "en %",end = " : ") #Saisie des pondérations l'une aprés l'autre.
         p = float(input())
         r = r + ListeNotes[j]*p
         mp = round(r/100,)
         ListePondérations.append(round(p)) #Ajout successif des pondérations dans la liste des pondérations.
         ListePondérations=ListePondérations #Liste des pondérations remplie.
         sp=sp+ListePondérations[j] #Cumule des pondérations pour trouver la nouvelle somme des pondérations.
     
     while sp!=100:
             print("\n\t","La somme des pondérations est : ",sp," ----> Recommencez")
             ListePondérations=[]
             sp=0
             r=0
             mp=0
             for j in range(len(ListeNotes)):
                 print("\nSaisir la pondération ",j+1, "en %",end = " : ") #Saisie des pondérations l'une aprés l'autre.
                 p = float(input())
                 r = r + ListeNotes[j]*p
                 mp = round(r/100,)
                 ListePondérations.append(round(p))  
                 ListePondérations=ListePondérations
                 sp=sp+ListePondérations[j]
     if sp==100:
         print("\n\t","ListePondérations = ",ListePondérations)
         if mp<60:
             print("\n\tla moyenne est : ",(mp),"% --->  Cours échoué")
         elif mp<70:
             print("\n\tla moyenne est : ",(mp),"% --->  Cours réussi avec mention acceptable")
         elif mp<80:
             print("\n\tla moyenne est : ",(mp),"% --->  Cours réussi avec mention assez bien")
         elif mp<=90:
             print("\n\tla moyenne est : ",(mp),"% --->  Cours réussi avec mention bien")
         else:
             print("\n\tla moyenne est : ",(mp),"% --->  Cours réussi avec mention très bien")
             
#Cas de l'option 3:
else:
    print("\n\t","Au revoir, c'est la fin du programme")
             
        
        
        
        
    
    
        
    

        
    
    
        
    




