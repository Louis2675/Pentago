from tests_alignements import test_grille_pleine
from tour_de_jeu import jouer_tour
from initialisation import initialisation_grille, initialisation_joueurs, test_victoire, alignement_victoire, charger_grille, sauvegarder_grille
from affichage import afficher_grille, bienvenue
from os import remove
from parametres import symboles


def jouer(symboles):
    bienvenue()
    a = input("Appuyez sur entrée pour commencer la partie ou entrez 'charger' pour charger une sauvegarde (ne fonctionne que si un fichier sauvegarde existe) : ")
    if a == "charger":
        try:
            fichier = open("partie_en_cours.txt", "r")
            fichier.close()
            print("Une sauvegarde a été trouvée")
            grille_info, dernier_joueur, nb_joueurs = charger_grille()
            symboles_joueurs = symboles[:-1]
            while len(symboles_joueurs) > nb_joueurs:
                symboles_joueurs.pop()
            print(grille_info)
        except FileNotFoundError:
            a = None

    if a != "charger":
        symboles_joueurs = symboles[:-1]
        grille_info = initialisation_grille()
        info_joueurs = initialisation_joueurs(symboles_joueurs)
        dernier_joueur = 0
        nb_joueurs = info_joueurs

    victoire = test_grille_pleine(grille_info)
    if victoire == True:
        print("Match nul, la grille est pleine")
        remove("partie_en_cours.txt")
    taille_victoire = alignement_victoire(grille_info)
    print("La taille de l'alignement necessaire est de", taille_victoire, "pour cette partie")

    while victoire == False:
        for i in range(dernier_joueur, len(symboles_joueurs)):
            afficher_grille(grille_info)
            jouer_tour(grille_info, i, symboles_joueurs)
            afficher_grille(grille_info)
            liste_victoire = test_victoire(grille_info, taille_victoire, symboles_joueurs)
            if liste_victoire[0] == 0:
                victoire = False
            elif liste_victoire[0] == True:
                victoire = True
                print("Le joueur", liste_victoire[1], "a gagné")
                break
            elif liste_victoire[0] == -1:
                victoire = True
                print("Match nul, les joueurs", liste_victoire[1], "ont gagné et les autres ont perdu")
                break
            if victoire == True:
                try:
                    fichier = open("partie_en_cours.txt", "r")
                    fichier.close()
                    remove("partie_en_cours.txt")
                    break
                except FileNotFoundError:
                    pass
            if victoire == False:
                a = input("Appuyez sur entrée pour continuer ou entrez 'sauvegarde' pour sauvegarder la partie : ")
                if a == "sauvegarde":
                    sauvegarder_grille(grille_info, i + 1, nb_joueurs)
                    print("La partie a été sauvegardée")
                    victoire = True
                    break
        grille_pleine = test_grille_pleine(grille_info)
        if grille_pleine == True:
            victoire = True
            print("Match nul, la grille est pleine")
            break
        dernier_joueur = 0


jouer(symboles)