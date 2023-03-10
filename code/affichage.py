"""Ce fichier contient les affichages du jeu"""


def afficher_ligne (sous_grille, taille_sous_grille, ligne): # Fonction qui permet d'afficher une ligne de la petite grille
    print("|", end="") # Met un element au debut de chaque ligne
    for colonne in range(0, taille_sous_grille): # Pour chaque element de la ligne
        print(" {} ".format(sous_grille[ligne][colonne]), end="|") # On affiche l'element


def afficher_grille(grille_info): # Fonction qui permet d'afficher la grille
    grille = grille_info[0] # On recupere la grille
    taille_grille = grille_info[1] # On recupere la taille de la grille
    taille_sous_grille = grille_info[2] # On recupere la taille des sous-grilles
    for k in range(0, taille_grille): # Pour le nombre de grandes-lignes
        """C'est ici que l'on devra print les entre deux grandes-lignes"""
        print()
        for i in range(0, taille_sous_grille): # Pour le nombre de lignes dans une sous-grille
            for j in range(0, taille_grille): # Pour le nombre de sous-grilles dans une grande-ligne
                afficher_ligne(grille[k][j], taille_sous_grille, i)
            print()
