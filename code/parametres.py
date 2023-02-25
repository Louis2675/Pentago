"""Ce fichier contient les paramètres du jeu"""

from affichage import afficher_grille

SYMBOLE_JOUEUR_1 = "⦿"  # Initialise le symbole du joueur 1
SYMBOLE_JOUEUR_2 = "⦾"  # Initialise le symbole du joueur 2
SYMBOLE_VIDE = "."  # Initialise le symbole d'une case case_vide


def copie_profonde_liste(liste): # Fonction qui permet de copier une liste sur deux dimensions
    """
    Entrée : une variable de type liste
    Sortie : une variable de type liste dans laquelle on a copié la liste d'entrée de deux dimensions
    """
    copie_liste = [] # On initialise la copie de la liste
    for liste_a_trois_obj in liste: # Pour chaque liste de trois objets dans la longueur de la liste d'entree
        copy_of_liste_a_trois_obj = [] # On initialise une liste vide pour copier chaque element (la deuxieme dimension)
        for single_value in liste_a_trois_obj: # Pour chaque element de la liste de trois objets
            copy_of_liste_a_trois_obj.append(single_value) # On copie l'element dans la liste vide
        copie_liste.append(copy_of_liste_a_trois_obj) # On ajoute la liste de trois objets copie dans la liste vide
    return copie_liste # On retourne la liste copiee


def initialisation_petite_grille(): # Fonction qui permet d'initialiser la petite grille
    """
    Entrée : vide
    Intervention utilisateur : le joueur indique dans un input le nombre de case dans la petite grille
    Sortie : la petite grille et sa taille
    """
    entree_valide = False # On initialise la variable qui permet de verifier si l'entree est valide (saisie protegee)
    while not entree_valide == True: #Tant que l'entrée n'est pas valide
        try: # On utilise un try/except pour verifier si l'entree est un nombre entier
            taille_grille = int(input("Donnez un coté de la petite grille (ex. 3 pour une grille en 3x3): ")) # On demande a l'utilisateur de saisir un nombre entier
            entree_valide = True # Si l'entree est valide, on sort de la boucle
        except ValueError: # Si l'entree n'est pas valide, on affiche un message d'erreur et on recommence
            print("Veuillez entrer un nombre entier")  
            entree_valide = False 
    petite_grille = [] # On initialise la petite grille
    for i in range(taille_grille): # Pour chaque ligne de la petite grille
        petite_grille.append([]) # On ajoute la dimension des colonnes
        for j in range(taille_grille): # Pour chaque element de la ligne
            petite_grille[i].append(SYMBOLE_VIDE) # On ajoute le symbole d'une case vide
    return petite_grille, taille_grille # On retourne la petite grille et sa taille sous forme de couple


def initialisation_grille():
    """
    Entrée : vide
    Intervention utilisateur : le joueur indique dans un input le nombre de petites grilles dans la grille
    Sortie : la grille, sa taille et la taille de la petite grille
    """
    entree_valide = False # On initialise la variable qui permet de verifier si l'entree est valide (saisie protegee)
    condition_sortie = False # On initialise la variable qui permet de verifier si la condition de sortie est remplie
    while not entree_valide == True:
        try:
            taille_grille = int(input("Choisissez le nombre de petites grilles (ex. 4 pour 4x4 petite grilles): "))
            entree_valide = True
        except ValueError:
            print("Veuillez entrer un nombre entier")  
            entree_valide = False 
    grille = []
    while not condition_sortie == True: # Cette boucle permet de demander une seule fois la taille de la petite grille a l'utilisateur
        nb_petite_grille = initialisation_petite_grille() # On initialise la petite grille
        condition_sortie = True 
        for i in range(taille_grille): # Pour chaque ligne de la grille
            grille.append([]) # On ajoute la dimension des colonnes
            for j in range(taille_grille): # Pour chaque element de la ligne
                grille[i].append(copie_profonde_liste(nb_petite_grille[0])) # On ajoute la petite grille dans l'element de la ligne
    return grille, taille_grille, nb_petite_grille[1] # On retourne la grille, sa taille et la taille de la petite grille sous forme de triplet


grille_info = initialisation_grille()

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
                coordonnees = tuple(int(x) -1 for x in coordonnees.split(",")) # On convertit la chaine de caractere en tuple de nombre entier
            except ValueError: # Si l'entree n'est pas valide, on affiche un message d'erreur et on recommence
                print("Veuillez entrer des nombres entier")  
                entree_valide = False
            print("conversion ok")
            if len(coordonnees) == 2: # On verifie que l'entree est bien un couple de nombre entier (colonne, ligne)
                print("longeur ok")
                mauvais_nombre_trouve = False # On initialise la variable qui permet de verifier si un mauvais nombre a ete trouve
                for i in range(len(coordonnees)): # Pour chaque element du couple
                    if coordonnees[i] == -1: # On empeche que la coordonnee entree soit a 0 (car sinon on retorouve - 1 dans la liste, i.e. la derniere case)
                            mauvais_nombre_trouve = True # Si un mauvais nombre est trouve, on redemandera a l'utilisateur de saisir une nouvelle entree
                            print("mauvais nombre trouve : valeur nulle, c'est", coordonnees[i])
                    if not (0 <= coordonnees[i] <= taille_grille * taille_petite_grille -1): # On verifie que les coordonnees entrees sont bien dans la grille (on evite l'IndexError)
                        mauvais_nombre_trouve = True # Si un mauvais nombre est trouve, on redemandera a l'utilisateur de saisir une nouvelle entree
                        print("mauvais nombre trouve, c'est", coordonnees[i])
                if mauvais_nombre_trouve == False: # Si aucun mauvais nombre n'a ete trouve, on sort de la boucle
                    print("boucle terminee, pas de mauvais nombre")
                    entree_valide = True

        ligne = coordonnees[1]
        colonne = coordonnees[0]
        cpt_ligne = 0
        cpt_colonne = 0

        if ligne % taille_petite_grille == 0:
            cpt_ligne = ((ligne + 1) // taille_petite_grille) + 1
        else:
            cpt_ligne = (ligne // taille_petite_grille) + 1
        if colonne % taille_petite_grille == 0:
            cpt_colonne = ((colonne + 1) // taille_petite_grille) + 1
        else:
            cpt_colonne = (colonne // taille_petite_grille) + 1
        nb_petite_grille = ((taille_grille * cpt_ligne) - (taille_grille - cpt_colonne)) - 1

        
        if ligne > taille_petite_grille: #Si la valeur de la ligne est plus grande que la taille de la sous grille,
            while ligne > taille_petite_grille: #Tant qu'elle n'est pas inferieure,
                ligne = ligne % taille_petite_grille #La ligne est egale au reste de la division euclidienne de la valeur de celle-ci par la taille de la sous grille

        if colonne > taille_petite_grille: #Si la valeur de la colonne est plus grande que la taille de la sous grille,
            while colonne > taille_petite_grille: #Tant qu'elle n'est pas inferieure,
                colonne = colonne % taille_petite_grille #La colonne est egale au reste de la division euclidienne de la valeur de celle-ci par la taille de la sous grille
        
            

        print("pour la case, le calcul: {} + 1 // {} =".format(coordonnees[1], taille_petite_grille), nb_petite_grille)
        print("pour la ligne, le calcul: {} + 1 // {} =".format(coordonnees[1], taille_grille), ligne)
        print("pour la colonne,  le calcul: {} + 1 // {} =".format(coordonnees[0], taille_grille), colonne)
        
        grille[0][nb_petite_grille][ligne][colonne] = "#"
        afficher_grille(grille_info)
        grille[0][nb_petite_grille][ligne][colonne] = SYMBOLE_VIDE
        
    
        if grille[0][nb_petite_grille][ligne][colonne] == SYMBOLE_VIDE:
            grille[0][nb_petite_grille][ligne][colonne] = symbole
            print("case vide")
            case_vide = True
            


def rotation_grille(grille_info):
    """
    Entree : la grille et le sens de la rotation
    Sortie : la grille tournee
    """
    grille = grille_info[0] # On affecte a la variable grille la premiere valeur du triplet grille_info
    taille_grille = grille_info[1] # On affecte a la variable taille_grille la deuxieme valeur du triplet grille_info
    taille_petite_grille = grille_info[2] # On affecte a la variable taille_petite_grille la troisieme valeur du triplet grille_info
    entree_valide = False # Variable qui permet de verifier si l'entree est valide (gauche ou droite)

    while not entree_valide == True: # Boucle qui verifie si l'entree est valide
        sens = input("Entrez le sens de rotation (gauche/droite) : ").lower()
        if sens == "gauche" or sens == "droite": # si l'entree est valide
            entree_valide = True