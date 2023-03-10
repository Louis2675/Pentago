from parametres import initialisation_grille, SYMBOLE_JOUEUR_1, SYMBOLE_JOUEUR_2


grille_info = initialisation_grille()


def transformation_dimension(grille_info): # Fonction qui permet de transformer la grille de 4 dimensions en 2 dimensions
    """
    Entree : la grille
    Sortie : True si il y a un alignement horizontal, False sinon
    """
    grille_copie = []
    for Glig in range(grille_info[1]):
        for lig in range(grille_info[2]):
            grille_copie.append([])
            copie_lig = lig + Glig * grille_info[2]
            for Gcol in range(grille_info[1]):
                for col in range(grille_info[2]):
                    grille_copie[copie_lig].append(grille_info[0][Glig][Gcol][lig][col])

transformation_dimension(grille_info)


def alignement_horizontal(grille_modifiee, taille_victoire, Symboles = [SYMBOLE_JOUEUR_1, SYMBOLE_JOUEUR_2]):
    compteur = 0
    for ligne in range(0, len(grille_modifiee)):
        for colonne in range(1, len(grille_modifiee[ligne])):
            if grille_modifiee[0][ligne] == grille_modifiee[ligne][colonne - 1] == Symboles[1] or grille_modifiee[ligne][colonne] == grille_modifiee[ligne][colonne - 1] == Symboles[0]:
                if compteur == 0:
                    compteur = compteur + 2
                else:
                    compteur = compteur + 1
            else:
                compteur = 0
            if compteur >= taille_victoire:
                return True
    return False       
            




def alignement_vertical(grille_modifiee, taille_victoire, Symboles = [SYMBOLE_JOUEUR_1, SYMBOLE_JOUEUR_2]):
    compteur = 0
    for ligne in range(1, len(grille_modifiee)):
        for colonne in range(0, len(grille_modifiee[ligne])):
            print(colonne, ",", end=" ")
            if grille_modifiee[ligne][colonne] == grille_modifiee[ligne -1][colonne] == Symboles[1] or grille_modifiee[ligne][colonne] == grille_modifiee[ligne -1][colonne] == Symboles[0]:
                print("condition verifiee", end=" ")
                if compteur == 0:
                    compteur = compteur + 2
                    print("compteur + 2")
                else:
                    compteur = compteur + 1
                    print("compteur + 1")
            else:
                compteur = 0
                print("compteur = 0")
    if compteur >= taille_victoire:
        return True
    print("iteration suivante")
    return False


def alignement_diagonnal(grille_modifiee, taille_victoire, Symboles = [SYMBOLE_JOUEUR_1, SYMBOLE_JOUEUR_2]):
    compteur = 0
    for i in range(1, len(grille_modifiee[0])):
        if grille_modifiee[-i -1][i] == grille_modifiee[-i][i -1] == Symboles[1] or grille_modifiee[-i -1][i] == grille_modifiee[-i][i -1] == Symboles[0]:
            if compteur == 0:
                compteur = compteur + 2
            else:
                compteur = compteur + 1
            if compteur == taille_victoire:
                return True
    else: 
        for i in range(1, len(grille_modifiee[0])):
            if grille_modifiee[i][i] == grille_modifiee[i -1][i -1] == Symboles[1] or grille_modifiee[i][i] == grille_modifiee[i - 1][i -1] == Symboles[0]:
                if compteur == 0:
                    compteur = compteur + 2
                else:
                    compteur = compteur + 1
                if compteur == taille_victoire:
                    return True

grille_modifiee = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [1, 2, 3, 4, 5, SYMBOLE_JOUEUR_1, 7, 8, 9, 10],
        [1, 2, 3, 4, 5, SYMBOLE_JOUEUR_1, 7, 8, 9, 10],
        [1, 2, 3, 4, 5, SYMBOLE_JOUEUR_1, 7, 8, 9, 10],
        [1, 2, 3, 4, 5, SYMBOLE_JOUEUR_1, 7, 8, 9, 10]
                   ]
print(alignement_vertical(grille_modifiee, 4))
