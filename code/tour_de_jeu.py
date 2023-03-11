from saisie import jouer_case, rotation_grille
from initialisation import test_victoire


def jouer_tour(grille_info, nb_joueur, symboles_joueurs, taille_victoire): # Fonction qui permet de jouer un tour
    """
    Entree : la grille, le nombre de joueurs, les symboles des joueurs
    Sortie : la grille modifiee apres les actions des joueurs
    """

    print("Joueur",  + 1, "à toi de jouer !")
    jouer_case(grille_info, symboles_joueurs[nb_joueur]) # On derande au joueur de jouer une case
    rotation_grille(grille_info) # On demande au joueur de tourner la grille