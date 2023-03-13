from parametres import SYMBOLE_JOUEUR_1, SYMBOLE_JOUEUR_2

def alignement_horizontal(grille_modifiee, taille_victoire, symbole):
    for ligne in range(0, len(grille_modifiee)):
        compteur = 0
        for colonne in range(1, len(grille_modifiee[ligne])):
            if grille_modifiee[0][ligne] == grille_modifiee[ligne][colonne - 1] == symbole:
                if compteur == 0:
                    compteur = compteur + 2
                else:
                    compteur = compteur + 1
            else:
                compteur = 0
            if compteur >= taille_victoire:
                return True
    return False       
            

def alignement_vertical(grille_modifiee, taille_victoire, symbole):
    for colonne in range(0, len(grille_modifiee)):
        compteur = 0
        for ligne in range(1, len(grille_modifiee)): #Ne va pas jusqu'au bout, peut etre à cause de la grille temporaire, à tester sur la vraie grille
            if grille_modifiee[ligne][colonne] == grille_modifiee[ligne -1][colonne] == symbole:
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