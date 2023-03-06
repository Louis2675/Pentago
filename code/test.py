from affichage import afficher_grille
from parametres import copie_profonde_liste, initialisation_grille

grille_info = initialisation_grille()

def rotation(grille_info, grille_tournee):
    grille = grille_tournee # A changer car l'algo prend en compte une seule petite grille et non la grande
    taille_petite_grille = grille_info[2]
    sauvegarde = copie_profonde_liste(grille_info[0]) # On cree une sauvegarde de la petite grille (a changer aussi)
    for colonne in range(0, taille_petite_grille): # pour avoir le nombre de la colonne
        ligne = taille_petite_grille - colonne - 1 # on regarde quelle ligne sera affecte dans la colonne apres la rotation
        for element in range(0, taille_petite_grille): # pour chaque element 
            grille[element][colonne] = sauvegarde[ligne][element] # on affecte apres la rotation vers la gauche


def rotation_grille(grille_info):
    grille = grille_info[0]
    taille_grande_grille = grille_info[1]
    entree_valide = False # var qui permet de verifier si l'entree est valide
    while not entree_valide == True: # on sort de la boucle quand l'entree est valide
        entree = input("Entrez les informations relatives a la rotation (direction ; nb_grille) ex. gauche ; 8 : ")
        entree = entree.replace(" ", "") # on enleve les espaces inutiles ecrits par l'utilisateur (permet d'eviter de redemander a cause d'espaces)
        liste_info = list(x for x in entree.split(";")) # on separe les elements
        print(liste_info)
        print(len(liste_info))
        if len(liste_info) == 2:
            print("len ok")
            if liste_info[0] == "gauche" or liste_info[0] == "droite": # on verifie l'entree des directions
                print("str ok")          
                try:
                    if liste_info[1] != "0":
                        liste_info = [liste_info[0], int(liste_info[1]) - 1]
                        entree_valide = True
                except IndexError: 
                    entree_valide = False
                    print("Entree invalide : veuillez entrer un nombre entier pour le numero de case")
            else: print("Entree invalide : veuillez bien entrer 'gauche' ou 'droite' suivi d'un nombre entier")
        else:
            print("Entree invalide : veuillez entrer deux elements")

    if liste_info[1] % taille_grande_grille == 0: # si la case est un multiple de la taille de la grille
        grande_ligne = liste_info[1] // taille_grande_grille - 1 # on recupere la ligne de la grande grille
        grande_colonne = liste_info[1] % taille_grande_grille - 1 # on recupere la colonne de la grande grille
    else: 
        grande_ligne = liste_info[1] // taille_grande_grille # on recupere la ligne de la grande grille
        grande_colonne = liste_info[1] % taille_grande_grille # on recupere la colonne de la grande grille


    grille_tournee = grille[grande_ligne][grande_colonne] # IMPORTANT : MAUVAISES VALEURS???
    if liste_info[0] == "gauche":
        print(grille_tournee)
    if liste_info[0] == "droite": # Une rotation vers la droite correspond a trois rotations vers la gauche...
        grille_tournee = rotation(grille_info, grille_tournee)
        grille_tournee = rotation(grille_info, grille_tournee)
        grille_tournee = rotation(grille_info, grille_tournee)

rotation_grille(grille_info)