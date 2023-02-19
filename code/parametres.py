"""Ce fichier contient les paramètres du jeu"""

SYMBOLE_JOUEUR_1 = "⦿"  # Initialise le symbole du joueur 1
SYMBOLE_JOUEUR_2 = "⦾"  # Initialise le symbole du joueur 2
SYMBOLE_VIDE = "."  # Initialise le symbole d'une case case_vide


def initialisation_petite_grille(): #
    """
    Entrée : vide
    Intervention utilisateur : le joueur indique dans un input le nombre de case dans la petite grille
    Sortie : la petite grille et sa taille
    """
    entree_valide = False
    while not entree_valide == True: #Tant que l'entrée n'est pas valide
        try:
            taille_grille = int(input("Donnez un coté de la petite grille (ex. 3 pour une grille en 3x3): "))
            entree_valide = True
        except ValueError:
            print("Veuillez entrer un nombre entier")  
            entree_valide = False 
    petite_grille = []
    for i in range(taille_grille):
        petite_grille.append([])
        for j in range(taille_grille):
            petite_grille[i].append(SYMBOLE_VIDE)
    return petite_grille, taille_grille


def initialisation_grille():
    """
    Entrée : vide
    Intervention utilisateur : le joueur indique dans un input le nombre de petites grilles dans la grille
    Sortie : la grille, sa taille et la taille de la petite grille
    """
    entree_valide = False
    condition_sortie = False
    while not entree_valide == True:
        try:
            taille_grille = int(input("Choisissez le nombre de petites grilles (ex. 4 pour 4x4 petite grilles): "))
            entree_valide = True
        except ValueError:
            print("Veuillez entrer un nombre entier")  
            entree_valide = False 
    grille = []
    while not condition_sortie == True:
        nb_petite_grille = initialisation_petite_grille()
        condition_sortie = True
    for i in range(taille_grille):
        grille.append([])
        for j in range(taille_grille):
            grille[i].append(nb_petite_grille[0])
    return grille, taille_grille, nb_petite_grille[1]

grille_info = initialisation_grille()

def jouer_case(grille_info, symbole):
    """
    Entrée : les informations de la grille de jeu et le symbole du joueur (1 ou 2)
    Intervention utilisateur : le joueur remplis un imput de la forme "colonne, ligne"
    Sortie : la grille du jeu avec la case remplie
    """
    grille = grille_info[0]
    taille_grille = grille_info[1]
    taille_petite_grille = grille_info[2]
    case_vide = False
    while not case_vide == True:
        entree_valide = False
        while not entree_valide == True:
            coordonnees = input("Choisissez une case sous le format colonne, ligne (ex. 1,4): ")
            try:
                coordonnees = tuple(int(x) -1 for x in coordonnees.split(","))
            except ValueError:
                print("Veuillez entrer des nombres entier")  
                entree_valide = False
            print("conversion ok")
            if len(coordonnees) == 2:
                print("longeur ok")
                mauvais_nombre_trouve = False
                for i in range(len(coordonnees)):
                    if coordonnees[i] == -1:
                            mauvais_nombre_trouve = True
                            print("mauvais nombre trouve : valeur nulle, c'est", coordonnees[i])
                    if not (0 <= coordonnees[i] <= taille_grille * taille_petite_grille -1):
                        mauvais_nombre_trouve = True
                        print("mauvais nombre trouve, c'est", coordonnees[i])
                if mauvais_nombre_trouve == False:
                    print("boucle terminee, pas de mauvais nombre")
                    entree_valide = True


        nb_petite_grille = coordonnees[1] // taille_petite_grille + 1
        ligne = coordonnees[1] // taille_grille + 1
        colonne = coordonnees[0] // taille_grille + 1
        print(nb_petite_grille, ligne, colonne)
        
        if grille[nb_petite_grille][ligne][colonne] == SYMBOLE_VIDE:
            grille[nb_petite_grille][ligne][colonne] = symbole
            print("case vide")
            case_vide = True
        print("fin func ou retour boucle")

jouer_case(grille_info, SYMBOLE_JOUEUR_1)
print(grille_info[0])
