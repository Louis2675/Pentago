
"""Ce fichier contient les paramètres du jeu"""

SYMBOLE_JOUEUR_1 = "⦿"  # Initialise le symbole du joueur 1
SYMBOLE_JOUEUR_2 = "⦾"  # Initialise le symbole du joueur 2
SYMBOLE_VIDE = "."  # Initialise le symbole d'une case case_vide

petite_grille = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Initialise une grille de 3x3
grille = [[],[],[],[]] # Initialise la grille du jeu


def copie_profonde_liste(liste): # Fonction qui permet de copier une liste
    """
    Entrée : une variable de type liste
    Sortie : une variable de type liste dans laquelle on a copié la liste d'entrée de deux dimensions
    """
    nv_liste = []
    for three_item_list in liste:
        copy_of_three_item_list = []
        for single_value in three_item_list:
            copy_of_three_item_list.append(single_value)
        nv_liste.append(copy_of_three_item_list)
    return nv_liste

for i in range(0, 4): # On demande 4 car il y a 4 petites grilles dans le jeu
    grille[i] = copie_profonde_liste(petite_grille) # On ajoute une copie de la grille de 3x3 à la grille du jeu


for i in range(len(grille)):
    for j in range(len(grille[i])):
        for k in range(len(grille[i][j])):
                grille[i][j][k] = SYMBOLE_VIDE


def choisir_case(grille, symbole): # Permet de remplir une case de la grille en fonction du symbole du joueur (1 ou 2)
    """
    Entrée : la grille du jeu et le symbole du joueur (1 ou 2)
    Intervention utilisateur : le joueur remplis un imput de la forme "case, ligne, colonne"
    Sortie : la grille du jeu avec la case remplie
    """
    case_vide = False
    while case_vide == False:
        input_valid = False
        while not input_valid == True:
            choix = input("Choisissez une case (case, ligne, colonne): ")
            liste_of_choix = choix.split(",")
            if len(liste_of_choix) == 3:
                found_a_bad_number = False
                for i in range(0, len(liste_of_choix)):
                    liste_of_choix[i] = liste_of_choix[i].replace(" ", "")
                    try:
                        if i == 0:
                            if not (1 <= int(liste_of_choix[i]) <= 4) and found_a_bad_number == False:
                                found_a_bad_number = True
                        elif not (1 <= int(liste_of_choix[i]) <= 3) and found_a_bad_number == False:
                                found_a_bad_number = True
                    except ValueError:
                        found_a_bad_number = True
                if found_a_bad_number == False:
                    input_valid = True
                    
        if input_valid == True:
            choix = (int(liste_of_choix[0]) - 1, int(liste_of_choix[1]) - 1, int(liste_of_choix[2]) - 1)         
        if grille[choix[0]][choix[1]][choix[2]] == SYMBOLE_VIDE:
            grille[choix[0]][choix[1]][choix[2]] = symbole
            
            case_vide = True

choisir_case(grille, SYMBOLE_JOUEUR_1)
print(grille)

