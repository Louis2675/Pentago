
def coordonees(liste_info, taille_grande_grille): # fonction qui permet de recuperer les coordonnees de la case

    if liste_info % taille_grande_grille == 0: # si la case est un multiple de la taille de la grille
        grande_ligne = liste_info // taille_grande_grille - 1 # on recupere la ligne de la grande grille
        grande_colonne = taille_grande_grille -1 
        
    else: 
        grande_ligne = liste_info // taille_grande_grille # on recupere la ligne de la grande grille
        grande_colonne = liste_info % taille_grande_grille - 1 # on recupere la colonne de la grande grille
    return grande_ligne, grande_colonne

print(coordonees(1, 3))

# [][][] [][][] [][][]
# [][][] [][][] [][][] 
# [][][] [][][] [][][]  

# [][][] [][][] [][][]
# [][][] [][][] [][][] 
# [][][] [][][] [][][]  

# [][][] [][][] [][][]
# [][][] [][][] [][][] 
# [][][] [][][] [][][]  