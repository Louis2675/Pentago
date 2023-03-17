
def alignement_horizontal(grille_modifiee, taille_victoire, symbole):
    for ligne in range(0, len(grille_modifiee)):
        compteur = 0
        for colonne in range(1, len(grille_modifiee)):
            if grille_modifiee[ligne][colonne] == grille_modifiee[ligne][colonne - 1] == symbole:
                if compteur == 0:
                    compteur = compteur + 2
                else:
                    compteur = compteur + 1
            if compteur >= taille_victoire:
                return True
    return False

def alignement_vertical(grille_modifiee, taille_victoire, symbole):
    for colonne in range(0, len(grille_modifiee)):
        compteur = 0
        for ligne in range(1, len(grille_modifiee)):
            if grille_modifiee[ligne][colonne] == grille_modifiee[ligne - 1][colonne] == symbole:
                if compteur == 0:
                    compteur = compteur + 2
                else:
                    compteur = compteur + 1
            else:
                compteur = 0
            if compteur >= taille_victoire:
                return True
    return False


def alignement_diagonal(grille_modifiee, taille_victoire, symbole):
    compteur = 0
    for ligne in range(0, len(grille_modifiee)):
        for colonne in range(0, len(grille_modifiee)):
            for element in range(1, len(grille_modifiee)):
                if grille_modifiee[ligne][colonne] == grille_modifiee[ligne - element][colonne - element] == symbole:
                    if compteur == 0:
                        compteur = compteur + 2
                    else:
                        compteur = compteur + 1
                elif grille_modifiee[ligne][colonne - element] == grille_modifiee[ligne - element][colonne - element] == symbole:
                    if compteur == 0:
                        compteur = compteur + 2
                    else:
                        compteur = compteur + 1
                else:
                    compteur = 0
            if compteur >= taille_victoire:
                return True
    return False    


def test_grille_pleine(grille_info):
    for Glig in range(0, grille_info[1]):
        for Gcol in range(0, grille_info[1]):
            for lig in range(0, grille_info[2]):
                for col in range(0, grille_info[2]):
                    if grille_info[0][Glig][Gcol][lig][col] == " ":
                        return False
    return True