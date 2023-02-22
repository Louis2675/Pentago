from parametres import initialisation_grille

grille_info = [
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]], [[[19, 20, 21], [22, 23, 24], [25, 26, 27]], [[28, 29, 30], [31, 32, 33], [34, 35, 36]]]]
sous_grille = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def afficher_ligne (sous_grille, ligne):
    print("|", end="") # Met un element au debut de chaque ligne
    for i in range(0, 3):
        print(" {} ".format(sous_grille[ligne][i]), end="|")

def afficher_grille(grille_info):
    grille = grille_info[0]
    taille_grille = grille_info[1]
    taille_sous_grille = grille_info[2]
    for k in range(0, taille_grille):
        for i in range(0, taille_sous_grille):
            for j in range(0, taille_grille):
                afficher_ligne(grille[k][j], i)
            print()

afficher_grille(grille_info)
