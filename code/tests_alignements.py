"""Ce fichier contient les fonctions de test d'alignements du jeu"""

def alignement_horizontal(grille_modifiee, taille_victoire, symbole): # Fonction qui permet de verifier si il y a un alignement horizontal
    """
    Entree : La grille, la taille de victoire, le symbole
    Sortie : Retourne True si il y a un alignement horizontal, False sinon
    """
    for ligne in range(0, len(grille_modifiee)): # Pour chaque ligne de la grille
        compteur = 0 # Initialise le compteur a 0
        for colonne in range(1, len(grille_modifiee)): # Pour chaque colonne de la grille
            if grille_modifiee[ligne][colonne] == grille_modifiee[ligne][colonne - 1] == symbole: # Si les deux valeures sont egales au symbole
                if compteur == 0: # Si le compteur est a 0
                    compteur = compteur + 2 # On ajoute 2 au compteur
                else:
                    compteur = compteur + 1 # Sinon on ajoute 1 au compteur
            if compteur >= taille_victoire: # Si le compteur est superieur ou egal a la taille de victoire
                return True # On retourne True
    return False


def alignement_vertical(grille_modifiee, taille_victoire, symbole): # Fonction qui permet de verifier si il y a un alignement vertical
    """
    Entree : La grille, la taille de victoire, le symbole
    Sortie : Retourne True si il y a un alignement horizontal, False sinon
    """
    for colonne in range(0, len(grille_modifiee)): # Pour chaque colonne de la grille
        compteur = 0 # Initialise le compteur a 0
        for ligne in range(1, len(grille_modifiee)): # Pour chaque ligne de la grille
            if grille_modifiee[ligne][colonne] == grille_modifiee[ligne - 1][colonne] == symbole: # si les deux valeures sont egales au symbole
                if compteur == 0: # Si le compteur est a 0
                    compteur = compteur + 2 # On ajoute 2 au compteur
                else:  
                    compteur = compteur + 1 # Sinon on ajoute 1 au compteur
            else:
                compteur = 0 # Sinon on remet le compteur a 0
            if compteur >= taille_victoire: # Si le compteur est superieur ou egal a la taille de victoire
                return True # On retourne True
    return False


def alignement_diagonal(grille_modifiee, taille_victoire, symbole): # Fonction qui permet de verifier si il y a un alignement diagonal
    """
    Entree : La grille, la taille de victoire, le symbole
    Sortie : Retourne True si il y a un alignement horizontal, False sinon
    """
    compteur = 0 # Initialise le compteur a 0
    for ligne in range(0, len(grille_modifiee)): # Pour chaque ligne de la grille
        for colonne in range(0, len(grille_modifiee)): # Pour chaque colonne de la grille
            for element in range(1, len(grille_modifiee)): # Pour chaque element de la grille
                if grille_modifiee[ligne][colonne] == grille_modifiee[ligne - element][colonne - element] == symbole: # Si les deux valeures sont egales au symbole
                    if compteur == 0: # Si le compteur est a 0
                        compteur = compteur + 2 # On ajoute 2 au compteur
                    else:
                        compteur = compteur + 1 # Sinon on ajoute 1 au compteur
                elif grille_modifiee[ligne][colonne - element] == grille_modifiee[ligne - element][colonne - element] == symbole: # Si les deux valeures sont egales au symbole
                    if compteur == 0: # Si le compteur est a 0
                        compteur = compteur + 2 # On ajoute 2 au compteur
                    else:
                        compteur = compteur + 1 # Sinon on ajoute 1 au compteur
                else:
                    compteur = 0 # Sinon on remet le compteur a 0
            if compteur >= taille_victoire: # Si le compteur est superieur ou egal a la taille de victoire
                return True
    return False    


def test_grille_pleine(grille_info, valeures): # Fonction qui permet de verifier si la grille est pleine
    for Glig in range(0, grille_info[1]): # Pour chaque ligne de la grille
        for Gcol in range(0, grille_info[1]): # Pour chaque colonne de la grille
            for lig in range(0, grille_info[2]): # Pour chaque ligne de la grille
                for col in range(0, grille_info[2]): # Pour chaque colonne de la grille
                    if grille_info[0][Glig][Gcol][lig][col] == valeures[-1]: # Si la case est vide
                        return False
    return True