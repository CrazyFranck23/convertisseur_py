POUCE_TO_CM = 2.54
CM_TO_POUCE = 0.394

print(""" Quel conversion souhaitez vous faire ? 
1 - Pouces vers CM
2 - CM vers Pouces """)

choix_int = 0
while choix_int == 0:
    choix_str = input("Choix : ")
    try:
        choix_int = float(choix_str)
    except ValueError:
        print("ERREUR: Veuillez entrer des nombres et non des lettres ou symboles.")
    else:
        if choix_int == 1:
            valeur_int = 0
            while valeur_int == 0:
                valeur_str = input("Entrer la valeur en pouce à convertir vers cm : ")
                try:
                    valeur_int = float(valeur_str)
                except ValueError:
                    print("ERREUR: Veuillez entrer des nombres et non des lettres ou symboles.")
                    print()
                else:
                    reponse = valeur_int * POUCE_TO_CM
                    print(f"Un écran de {valeur_int} pouces de diagonale, correspond à {reponse} cm.")
                    print()
                    valeur_int = 1
                    while valeur_int == 1:
                        choix_continuer = input("Voulez vous continuer ou arreter ('oui' ou 'non') ? ")
                        if choix_continuer == "oui":
                            valeur_int = 0
                        elif choix_continuer == "non":
                            print("Merci et au revoir ! ")
                            break
                        else:
                            print("ERREUR ! Saisir uniquement 'oui' ou 'non'.")
                            print()
                            valeur_int = 1
        elif choix_int == 2:
            valeur_int = 0
            while valeur_int == 0:
                valeur_str = input("Entrer la valeur en cm à convertir vers pouce : ")
                try:
                    valeur_int = float(valeur_str)
                except ValueError:
                    print("ERREUR: Veuillez entrer des nombres et non des lettres ou symboles.")
                    print()
                else:
                    reponse = valeur_int * CM_TO_POUCE
                    print(f"Un écran de {valeur_int} cm, correspond à {round(reponse, 2)} pouces de diagonale.")
                    print()
                    valeur_int = 1
                    while valeur_int == 1:
                        choix_continuer = input("Voulez vous continuer ou arreter ('oui' ou 'non') ? ")
                        if choix_continuer == "oui":
                            valeur_int = 0
                        elif choix_continuer == "non":
                            print("Merci et au revoir ! ")
                            break
                        else:
                            print("ERREUR ! Saisir uniquement 'oui' ou 'non'.")
                            print()
                            valeur_int = 1
        else:
            print("Attention ! Choisissez uniquement entre 1 et 2.")
            choix_int = 0
