from saisie import demander_taille_victoire
from tour_de_jeu import jouer_tour, jouer_case, rotation_grille
from initialisation import initialisation_grille, initialisation_joueurs, test_victoire, copie_profonde_liste
from affichage import afficher_grille


def jouer():
    victoire = False
    grille_info = initialisation_grille()
    taille_victoire = demander_taille_victoire()
    infos_joueurs = initialisation_joueurs()
    symboles_joueurs = infos_joueurs[0]
    nb_joueurs = infos_joueurs[1]
    while victoire == False:
        for i in range(0, len(symboles_joueurs)):
            afficher_grille(grille_info)
            jouer_tour(grille_info, i, symboles_joueurs)
            liste_victoire = test_victoire(grille_info, taille_victoire, symboles_joueurs)
            if liste_victoire[0] == 0:
                victoire = False
            elif liste_victoire[0] == True:
                victoire = True
                print("Le joueur", liste_victoire[1], "a gagné")
            elif liste_victoire[0] == -1:
                victoire = True
                print("Match nul, les joueurs", liste_victoire[1], "ont gagné et les autres ont perdu")

jouer()