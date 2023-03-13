from initialisation import copie_profonde_liste
from parametres import SYMBOLE_VIDE
from affichage import afficher_grille

def jouer_case(grille_info, symbole):
    """
    Entrée : les informations de la grille de jeu et le symbole du joueur (1 ou 2)
    Intervention utilisateur : le joueur remplis un imput de la forme "colonne, ligne"
    Sortie : la grille du jeu avec la case remplie
    """
    grille = grille_info[0] # On affecte a la variable grille la premiere valeur du triplet grille_info
    taille_grille = grille_info[1] # On affecte a la variable taille_grille la deuxieme valeur du triplet grille_info
    taille_petite_grille = grille_info[2] # On affecte a la variable taille_petite_grille la troisieme valeur du triplet grille_info
    case_vide = False # On initialise la variable qui permet de verifier si la case est vide
    while not case_vide == True: # Tant que la case n'est pas vide
        entree_valide = False # On initialise la variable qui permet de verifier si l'entree est valide (saisie protegee)
        while not entree_valide == True: # Tant que l'entree n'est pas valide
            coordonnees = input("Choisissez une case sous le format colonne, ligne (ex. 1,4): ") # On demande a l'utilisateur de saisir les coordonnees de la case
            try: # On utilise un try/except pour verifier si l'entree est un nombre entier
                coordonnees = list(int(x) for x in coordonnees.split(","))
            except ValueError: # Si l'entree n'est pas valide, on affiche un message d'erreur et on recommence
                print("Veuillez entrer des nombres entier")  
                entree_valide = False
            if len(coordonnees) == 2: # On verifie que l'entree est bien un couple de nombre entier (colonne, ligne)
                mauvais_nombre_trouve = False # On initialise la variable qui permet de verifier si un mauvais nombre a ete trouve
                for i in range(len(coordonnees)): # Pour chaque element du couple
                    if coordonnees[i] == -1: # On empeche que la coordonnee entree soit a 0 (car sinon on retorouve - 1 dans la liste, i.e. la derniere case)
                            mauvais_nombre_trouve = True # Si un mauvais nombre est trouve, on redemandera a l'utilisateur de saisir une nouvelle entree
                    if not (0 <= coordonnees[i] <= taille_grille * taille_petite_grille): # On verifie que les coordonnees entrees sont bien dans la grille (on evite l'IndexError)
                        mauvais_nombre_trouve = True # Si un mauvais nombre est trouve, on redemandera a l'utilisateur de saisir une nouvelle entree
                if mauvais_nombre_trouve == False: # Si aucun mauvais nombre n'a ete trouve, on sort de la boucle
                    entree_valide = True

        ligne = coordonnees[1]
        colonne = coordonnees[0]

        if ligne % taille_petite_grille == 0:
            grande_ligne = (ligne - 1) // taille_petite_grille
        else:
            grande_ligne = ligne // taille_petite_grille
        
        if colonne % taille_petite_grille == 0:
            grande_colonne = (colonne - 1) // taille_petite_grille
        else:
            grande_colonne = colonne // taille_petite_grille

        if ligne % taille_petite_grille == 0: #Si la valeur de la ligne est plus grande que la taille de la sous grille,
            ligne = (ligne - 1) % taille_petite_grille #La ligne est egale au reste de la division euclidienne de la valeur de celle-ci par la taille de la sous grille
        else:
            ligne = (ligne % taille_petite_grille) - 1

        if colonne % taille_petite_grille == 0: #Si la valeur de la colonne est plus grande que la taille de la sous grille,
            colonne = (colonne - 1) % taille_petite_grille #La colonne est egale au reste de la division euclidienne de la valeur de celle-ci par la taille de la sous grille
        else:
            colonne = (colonne % taille_petite_grille) - 1

        if grille[grande_ligne][grande_colonne][ligne][colonne] == SYMBOLE_VIDE:
            grille[grande_ligne][grande_colonne][ligne][colonne] = symbole
            case_vide = True


def rotation_grille(grille_info):
    grille = grille_info[0]  # on recupere la grille
    taille_grande_grille = grille_info[1] # on recupere la taille de la grille
    entree_valide = False # var qui permet de verifier si l'entree est valide
    while not entree_valide == True: # on sort de la boucle quand l'entree est valide
        entree = input("Entrez les informations relatives a la rotation (direction ; nb_grille) ex. gauche ; 8 : ")
        while entree == "":
            entree = input("Entrez les informations relatives a la rotation (direction ; nb_grille) ex. gauche ; 8 : ")
        entree = entree.replace(" ", "") # on enleve les espaces inutiles ecrits par l'utilisateur (permet d'eviter de redemander a cause d'espaces)
        liste_info = list(x for x in entree.split(";"))
        if len(liste_info) == 2: # Si il n'y a que deux elements 
            if liste_info[0] == "gauche" or liste_info[0] == "droite": # on verifie l'entree des directions
                try:
                    if liste_info[1] != "0":
                        liste_info = [liste_info[0], int(liste_info[1])]
                        entree_valide = True
                except IndexError:
                    entree_valide = False
                    print("Entree invalide : veuillez entrer un nombre entier pour le numero de case")
            else: print("Entree invalide : veuillez bien entrer 'gauche' ou 'droite' suivi d'un nombre entier")
        else:
            print("Entree invalide : veuillez entrer deux elements")

        if liste_info[1] % taille_grande_grille == 0: # si la case est un multiple de la taille de la grille
            grande_ligne = liste_info[1] // taille_grande_grille - 1 # on recupere la ligne de la grande grille
            grande_colonne = taille_grande_grille -1
        else: 
            grande_ligne = liste_info[1] // taille_grande_grille # on recupere la ligne de la grande grille
            grande_colonne = liste_info[1] % taille_grande_grille - 1 # on recupere la colonne de la grande grille

    grille_tournee = grille[grande_ligne][grande_colonne] # On affecte la grille a tourner a une variable
    if liste_info[0] == "gauche": # si on tourne vers la gauche
        rotation_gauche(grille_info, grille_tournee)
    if liste_info[0] == "droite": # si on tourne vers la droite
        rotation_droite(grille_info, grille_tournee)
    grille_info[0][grande_ligne][grande_colonne] = grille_tournee


def rotation_droite(grille_info, grille_tournee):
    grille = grille_tournee
    taille_petite_grille = grille_info[2]
    sauvegarde = copie_profonde_liste(grille) # On cree une sauvegarde de la petite grille (a changer aussi)
    for colonne in range(0, taille_petite_grille): # pour avoir le nombre de la colonne
        ligne = taille_petite_grille - colonne - 1 # on regarde quelle ligne sera affecte dans la colonne apres la rotation
        for element in range(0, taille_petite_grille): # pour chaque element 
            grille[element][colonne] = sauvegarde[ligne][element] # on affecte apres la rotation vers la gauche


def rotation_gauche(grille_info, grille_tournee): # Une rotation vers la droite correspond a trois rotations vers la gauche...
    grille = grille_tournee
    taille_petite_grille = grille_info[2]
    sauvegarde = copie_profonde_liste(grille) # On cree une sauvegarde de la petite grille (a changer aussi)
    for colonne in range(0, taille_petite_grille): # pour avoir le nombre de la colonne
        ligne = taille_petite_grille - colonne - 1 # on regarde quelle ligne sera affecte dans la colonne apres la rotation
        for element in range(0, taille_petite_grille): # pour chaque element 
            grille[element][colonne] = sauvegarde[ligne][element] # on affecte apres la rotation vers la gauche
    sauvegarde = copie_profonde_liste(grille) # On cree une sauvegarde de la petite grille (a changer aussi)
    for colonne in range(0, taille_petite_grille): # pour avoir le nombre de la colonne
        ligne = taille_petite_grille - colonne - 1 # on regarde quelle ligne sera affecte dans la colonne apres la rotation
        for element in range(0, taille_petite_grille): # pour chaque element 
            grille[element][colonne] = sauvegarde[ligne][element] # on affecte apres la rotation vers la gauche
    sauvegarde = copie_profonde_liste(grille) # On cree une sauvegarde de la petite grille (a changer aussi)
    for colonne in range(0, taille_petite_grille): # pour avoir le nombre de la colonne
        ligne = taille_petite_grille - colonne - 1 # on regarde quelle ligne sera affecte dans la colonne apres la rotation
        for element in range(0, taille_petite_grille): # pour chaque element 
            grille[element][colonne] = sauvegarde[ligne][element] # on affecte apres la rotation vers la gauche


def jouer_tour(grille_info, nb_joueur, symboles_joueurs): # Fonction qui permet de jouer un tour
    """
    Entree : la grille, le nombre de joueurs, les symboles des joueurs
    Sortie : la grille modifiee apres les actions des joueurs
    """
    print("Joueur",  nb_joueur + 1, "à toi de jouer !")
    jouer_case(grille_info, symboles_joueurs[nb_joueur]) # On derande au joueur de jouer une case
    afficher_grille(grille_info) # On affiche la grille
    rotation_grille(grille_info) # On demande au joueur de tourner la grille