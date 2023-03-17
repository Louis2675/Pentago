"""Ce fichier contient les fonctions d'affichage du jeu"""

def bienvenue(): # Fonction qui affiche le message de bienvenue dans le jeu
    print('''
  ___ _                                                      _     _                 
 | _ |_)___ _ ___ _____ _ _ _  _ ___   __ _ _  _   __ _ _  _(_)_ _| |_ __ _ __ _ ___ 
 | _ \ / -_) ' \ V / -_) ' \ || / -_) / _` | || | / _` | || | | ' \  _/ _` / _` / _ \\
 |___/_\___|_||_\_/\___|_||_\_,_\___| \__,_|\_,_| \__, |\_,_|_|_||_\__\__,_\__, \___/
                                                     |_|                   |___/     
    ''')


def afficher_ligne (sous_grille, taille_sous_grille, ligne): # Fonction qui permet d'afficher une ligne de la petite grille
    """
    Entree : La sous-grille, la taille de la sous-grille, la ligne a afficher
    Sortie : Affiche la ligne de la sous-grille
    """
    print("|", end = "") # Met un element au debut de chaque ligne
    for colonne in range(0, taille_sous_grille): # Pour chaque element de la ligne
        print(" {} ".format(sous_grille[ligne][colonne]), end = "|") # On affiche l'element


def afficher_grille(grille_info): # Fonction qui permet d'afficher la grille
    """
    Entree : Les informations de la grille
    Sortie : Affiche la grille
    """
    grille = grille_info[0] # On recupere la grille
    taille_grille = grille_info[1] # On recupere la taille de la grille
    taille_sous_grille = grille_info[2] # On recupere la taille des sous-grilles
    for k in range(0, taille_grille): # Pour le nombre de grandes-lignes
        print(taille_grille * taille_sous_grille * 4 * "=" + taille_grille * "=")
        for i in range(0, taille_sous_grille): # Pour le nombre de lignes dans une sous-grille
            for j in range(0, taille_grille): # Pour le nombre de sous-grilles dans une grande-ligne
                afficher_ligne(grille[k][j], taille_sous_grille, i)
            print()
    print(taille_grille * taille_sous_grille * 4 * "=" + taille_grille * "=")