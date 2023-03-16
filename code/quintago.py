from tour_de_jeu import jouer_tour
from initialisation import initialisation_grille, initialisation_joueurs, test_victoire, alignement_victoire, charger_grille, sauvegarder_grille
from affichage import afficher_grille
from os import remove


def jouer():
    victoire = False
    grille_info = initialisation_grille()
    taille_victoire = alignement_victoire(grille_info)
    print("La taille de l'alignement necessaire est de", taille_victoire, "pour cette partie")
    infos_joueurs = initialisation_joueurs()
    symboles_joueurs = infos_joueurs[0]
    nb_joueurs = infos_joueurs[1]
    a = input("Appuyez sur entrée pour commencer la partie ou entrez 'charger' pour charger une sauvegarde (ne fonctionne que si un fichier sauvegarde existe) : ")
    if a == "charger":
        try:
            fichier = open("partie_en_cours.txt", "r")
            fichier.close()
            print("Une sauvegarde a été trouvée")
            grille_info, dernier_joueur = charger_grille()
        except FileNotFoundError:
            print("Aucune sauvegarde n'a été trouvée")
    dernier_joueur = 0
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
            elif liste_victoire[0] == -1:
                victoire = True
                print("Match nul, les joueurs", liste_victoire[1], "ont gagné et les autres ont perdu")
            if victoire == True:
                try:
                    fichier = open("partie_en_cours.txt", "r")
                    fichier.close()
                    remove("partie_en_cours.txt")
                except FileNotFoundError:
                    pass
            if victoire == False:
                a = input("Appuyez sur entrée pour continuer ou entrez 'sauvegarde' pour sauvegarder la partie : ")
                if a == "sauvegarde":
                    sauvegarder_grille(grille_info, i)
                    print("La partie a été sauvegardée")
                    victoire = True


jouer()