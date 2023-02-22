"""Ce fichier contient les affichages du jeu"""

def afficher_ligne (sous_grille, taille_sous_grille, ligne):
    print("|", end="") # Met un element au debut de chaque ligne
    for i in range(0, taille_sous_grille):
        print(" {} ".format(sous_grille[ligne][i]), end="|")

def afficher_grille(grille_info):
    grille = grille_info[0]
    taille_grille = grille_info[1]
    taille_sous_grille = grille_info[2]
    for k in range(0, taille_grille):
        """C'est ici que l'on devra print les entre deux grandes-lignes"""
        for i in range(0, taille_sous_grille):
            for j in range(0, taille_grille):
                afficher_ligne(grille[k][j], taille_sous_grille, i)
            print()