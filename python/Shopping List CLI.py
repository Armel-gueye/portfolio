"""Programme de liste de course qui permet à l'utilisateur d'éditer sa liste de course"""


liste = []                                                                              # Initialisation de la liste vide

while True:                                                                             # Initialisation de la boucle

    choix = int(input("_______________________________________________________________________________ \n Choisissez parmi les 5 options suivantes : \n 1: Ajoutez un élément à la liste \n 2: Rétirer un élément de la liste \n 3: Afficher la liste \n 4: Vider la liste \n 5: Quitter \n 👉 Votre choix : "))

    if choix == 1:                                                                      # Ajout élément
            choixAjout = input("Saisissez l'élément à ajouter : ")
            liste.append(choixAjout)
            print(f"L'élémént {choixAjout} a bien été ajouté")
    elif choix == 2:                                                                    # Retirer élément
            choixRetire = input("Saisissez l'élément à retirer : ")
            if choixRetire in liste:                                                    # Condition pour vérifier que l'input de l'user est valide
                liste.remove(choixRetire)
                print(f"L'élément {choixRetire} a bien été rétirer")
            else:                                                                       # Si l'input n'est pas valide, afficher une erreur et reprendre la boucle
                print("Cet élément n'est pas dans la liste. Veuillez rééssayer !")
                continue
    elif choix == 3:                                                                    # Afficher la liste
        print(f"Voici la liste actuelle : \n {liste}")
    elif choix == 4:                                                                    # Vider la liste
        listeVide = liste.clear()
        print("La liste a été vidé avec succès !")
    elif choix == 5:                                                                    # Quitter la boucle et afficher un message d'au-revoir à l'utilisateur
        print("A bientôt !")
        break
    else:
        print("Saisie incorrecte. Veuillez vérifier que vous avez entré le bon numéro") # Afficher un message d'erreur lors d'une saisie incorrecte de l'utilisateur
        continue