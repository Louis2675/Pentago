fichier = open("partie_en_cours.txt", "r")
print(fichier.readline())  
SYMBOLE_VIDE = "."

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

def rotation_droite(grille_info, grille_tournee):
    grille = grille_tournee
    taille_petite_grille = grille_info[2]
    sauvegarde = copie_profonde_liste(grille) # On cree une sauvegarde de la petite grille (a changer aussi)
    for colonne in range(0, taille_petite_grille): # pour avoir le nombre de la colonne
        ligne = taille_petite_grille - colonne - 1 # on regarde quelle ligne sera affecte dans la colonne apres la rotation
        for element in range(0, taille_petite_grille): # pour chaque element 
            grille[element][colonne] = sauvegarde[ligne][element] # on affecte apres la rotation vers la gauche





def rotation_grille(grille_info):
    grille = grille_info[0]  # on recupere la grille
    taille_grande_grille = grille_info[1] # on recupere la taille de la grille
    entree_valide = False # var qui permet de verifier si l'entree est valide
    while not entree_valide == True: # on sort de la boucle quand l'entree est valide
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
        grille_tournee = rotation_gauche(grille_info, grille_tournee)
    if liste_info[0] == "droite": # si on tourne vers la droite
        grille_tournee = rotation_droite(grille_info, grille_tournee)
    grille_info[0][grande_ligne][grande_colonne] = grille_tournee

grille_info = initialisation_grille()
rotation_grille(grille_info)