from parametres import initialisation_grille
grille_info = initialisation_grille()

def transformation_dimension(grille_info, longueur_alignement): # Fonction qui permet de transformer la grille de 4 dimensions en 2 dimensions
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
    print(grille_copie)
