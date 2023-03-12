from saisie import jouer_case, rotation_grille
from initialisation import copie_profonde_liste


def rotation_droite(grille_info, grille_tournee):
    grille = grille_tournee
    taille_petite_grille = grille_info[2]
    sauvegarde = copie_profonde_liste(grille) # On cree une sauvegarde de la petite grille (a changer aussi)
    for colonne in range(0, taille_petite_grille): # pour avoir le nombre de la colonne
        ligne = taille_petite_grille - colonne - 1 # on regarde quelle ligne sera affecte dans la colonne apres la rotation
        for element in range(0, taille_petite_grille): # pour chaque element 
            grille[element][colonne] = sauvegarde[ligne][element] # on affecte apres la rotation vers la gauche


def rotation_gauche(grille_info, grille_tournee): # Une rotation vers la droite correspond a trois rotations vers la gauche...
    rotation = rotation_droite(grille_info, grille_tournee) # on fait une rotation vers la gauche
    rotation = rotation_droite(grille_info, rotation) # on fait une rotation vers la gauche
    rotation = rotation_droite(grille_info, rotation) # on fait une rotation vers la gauche


def jouer_tour(grille_info, nb_joueur, symboles_joueurs): # Fonction qui permet de jouer un tour
    """
    Entree : la grille, le nombre de joueurs, les symboles des joueurs
    Sortie : la grille modifiee apres les actions des joueurs
    """
    print("Joueur",  nb_joueur, "à toi de jouer !")
    jouer_case(grille_info, symboles_joueurs[nb_joueur]) # On derande au joueur de jouer une case
    rotation_grille(grille_info) # On demande au joueur de tourner la grille
