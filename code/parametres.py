"""Ce fichier contient les paramètres du jeu"""

SYMBOLE_JOUEUR_1 = "⦿"  # Initialise le suymbole du joueur 1
SYMBOLE_JOUEUR_2 = "⦾"  # Initialise le suymbole du joueur 2
SYMBOLE_VIDE = "."  # Initialise le suymbole d'une case vide

grille = [
    [
        [[], [] ,[]], [[], [], []], [[], [], []]
    ],
    [
        [[], [] ,[]], [[], [], []], [[], [], []]
    ],
    [
        [[], [] ,[]], [[], [], []], [[], [], []]
    ],
    [
        [[], [] ,[]], [[], [], []], [[], [], []]
    ]
]

for i in range(len(grille)):
    for j in range(len(grille[i])):
        for k in range(len(grille[i][j])):
            grille[i][j][k] = SYMBOLE_VIDE


def choisir_case(grille, symbole):
    """Permet de choisir une case pour y placer un symbole"""
    cpt = 0
    while cpt == 0:
        case = int(input("Sélectionnez votre case : ")) -1
        lig = int(input("Sélectionnez votre ligne : ")) -1
        col = int(input("Sélectionnez votre colonne : ")) -1
        if grille[case][lig][col] == SYMBOLE_VIDE:
            print(symbole)
            grille[case][lig][col] = symbole
            cpt = 1
        else: print(False)
    return grille
