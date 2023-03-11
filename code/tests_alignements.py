from parametres import SYMBOLE_JOUEUR_1, SYMBOLE_JOUEUR_2


def alignement_horizontal(grille_modifiee, taille_victoire, Symboles = [SYMBOLE_JOUEUR_1, SYMBOLE_JOUEUR_2]):
    for ligne in range(0, len(grille_modifiee)):
        compteur = 0
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
    for colonne in range(0, len(grille_modifiee)):
        compteur = 0
        for ligne in range(1, len(grille_modifiee)): #Ne va pas jusqu'au bout, peut etre à cause de la grille temporaire, à tester sur la vraie grille
            if grille_modifiee[ligne][colonne] == grille_modifiee[ligne -1][colonne] == Symboles[1] or grille_modifiee[ligne][colonne] == grille_modifiee[ligne -1][colonne] == Symboles[0]:
                if compteur == 0:
                    compteur = compteur + 2
                else:
                    compteur = compteur + 1
            else:
                compteur = 0
        if compteur >= taille_victoire:
            return True
    return False


def alignement_diagonnal(grille_modifiee, taille_victoire, Symboles = [SYMBOLE_JOUEUR_1, SYMBOLE_JOUEUR_2]):
    compteur = 0
    for j in range(1, len(grille_modifiee)):
        for i in range(1, len(grille_modifiee[0])):
            if grille_modifiee[-i -j][i] == grille_modifiee[-i-(j-1)][i -1] == Symboles[1] or grille_modifiee[-i -j][i] == grille_modifiee[-i-(j-1)][i -1] == Symboles[0]:
                if compteur == 0:
                    compteur = compteur + 2
                else:
                    compteur = compteur + 1
                if compteur == taille_victoire:
                    return True
    else: 
        compteur = 0
        for j in range(1, len(grille_modifiee)):
            for i in range(1, len(grille_modifiee[0])):
                if grille_modifiee[-i -(j-1)][i] == grille_modifiee[-i -j][i -1] == Symboles[1] or grille_modifiee[i -(j-1)][i] == grille_modifiee[-i -j][i -1] == Symboles[0]:
                    if compteur == 0:
                        compteur = compteur + 2
                    else:
                        compteur = compteur + 1
                    if compteur == taille_victoire:
                        return True
                

grille_modifiee = [
    [1, "a", SYMBOLE_JOUEUR_1, 8],
    [1, "a", SYMBOLE_JOUEUR_1, 8],
    [1, "a", SYMBOLE_JOUEUR_1, 8],
    [1, "a", SYMBOLE_JOUEUR_1, 8],
]

#     if grille_modifiee[-i -j][i] == grille_modifiee[-i-(j-1)][i -1] == Symboles[1] or grille_modifiee[-i -j][i] == grille_modifiee[-i-(j-1)][i -1] == Symboles[0]:
#        ~~~~~~~~~~~~~~~^^^^^^^
# IndexError: list index out of range

alignement_diagonnal(grille_modifiee, 3)