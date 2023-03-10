from parametres import initialisation_grille, SYMBOLE_JOUEUR_1, SYMBOLE_JOUEUR_2


grille_modifiee = [
    [SYMBOLE_JOUEUR_1,2,SYMBOLE_JOUEUR_1],
    [3,SYMBOLE_JOUEUR_1,5],
    [SYMBOLE_JOUEUR_1,6,SYMBOLE_JOUEUR_1]
    ]

print(alignement_diagonnal(grille_modifiee, 3))