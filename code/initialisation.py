"""Ce fichier contient les fonctions qui permettent d'initialiser le jeu"""

from parametres import SYMBOLE_VIDE, SYMBOLE_JOUEUR_1, SYMBOLE_JOUEUR_2, SYMBOLE_JOUEUR_3, SYMBOLE_JOUEUR_4
from tests_alignements import alignement_horizontal, alignement_vertical, alignement_diagonal
from saisie import demander_nb_joueurs
from os import remove


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
            if taille_grille < 3: # Minimum 3x3 cases pour une petite grille
                entree_valide = False
                print("Veuillez saisir une taille superieure à 3 pour la petite grille")
            else: entree_valide = True # Si l'entree est valide, on sort de la boucle
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
            if taille_grille < 2: 
                entree_valide = False
                print("Veuillez saisir une taille superieure à 2 pour la grande grille")
            else: entree_valide = True
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


def transformation_dimension(grille_info): # Fonction qui permet de transformer la grille de 4 dimensions en 2 dimensions
    """
    Entree : la grille
    Sortie : True si il y a un alignement horizontal, False sinon
    """
    grille_copie = [] # On initialise la copie de la grille
    for Glig in range(grille_info[1]): # Pour chaque grande ligne de la grille
        for lig in range(grille_info[2]): # Pour chaque ligne de la petite grille
            grille_copie.append([]) # On ajoute la dimension des colonnes
            copie_lig = lig + Glig * grille_info[2] # On calcule la ligne de la copie de la grille
            for Gcol in range(grille_info[1]): # Pour chaque grande colonne de la grille
                for col in range(grille_info[2]): # Pour chaque colonne de la petite grille
                    grille_copie[copie_lig].append(grille_info[0][Glig][Gcol][lig][col]) # On ajoute l'element dans la copie de la grille
    return grille_copie # On retourne la copie de la grille


def test_victoire(grille_info, taille_victoire, symboles_joueurs):
    """
    Entree : Les informations de la grille, la taille de la victoire et les symboles des joueurs
    Sortie : True si il y a un gagnant, -1 si il y a plusieurs gagnants (match nul), False sinon
    [VIS A VIS DES CONDITIONS IMPOSEES PAR LE SUJET : NOUS AVONS CHANGE LEGEREMENT LE RETURN AFIN DE RETOURNER LA LISTE DES GAGNANTS ET NON PLUS LE NUMERO DU GAGNANT]
    """
    liste_gagnants = [] # On initialise la liste des gagnants
    resultat = 0 # On initialise le resultat
    grille_modifiee = transformation_dimension(grille_info) # On transforme la grille de 4 dimensions en 2 dimensions
    for i in range(0, len(symboles_joueurs)):
        if alignement_horizontal(grille_modifiee, taille_victoire, symboles_joueurs[i]) == True or alignement_vertical(grille_modifiee, taille_victoire, symboles_joueurs[i]) == True or alignement_diagonal(grille_modifiee, taille_victoire, symboles_joueurs[i]) == True: # On verifie les alignements 
            liste_gagnants.append(i) # On ajoute le joueur a la liste des gagnants s'il a gagne
            resultat = True # On change le resultat
    if len(liste_gagnants) > 1: # Si il y a plusieurs gagnants
        resultat = -1 # Le match est nul
    return (resultat, liste_gagnants)


def initialisation_joueurs(symboles_joueurs): # Fonction qui permet d'initialiser les symboles en fonction du nombre de joueurs
    """
    Fonction qui ne prend pas d'entree mais demande une intervention utilisateur dans demander_nb_joueurs()
    """
    nb_joueurs = demander_nb_joueurs() # On demande le nombre de joueurs
    while len(symboles_joueurs) > nb_joueurs: # Tant que le nombre de symboles est superieur au nombre de joueurs
        symboles_joueurs.pop() # On supprime le dernier symbole
    return nb_joueurs


def sauvegarder_grille(grille_info, dernier_joueur, nb_joueurs):
    """
    Entree : Les informations de la grille, le dernier joueur et le nombre de joueurs
    Sortie : On cree un fichier texte qui contient les informations de la grille afin de pouvoir les charger plus tard
    """
    try:
        fichier = open("partie_en_cours.txt", "x") # On cree le fichier en l'ouvrant
    except FileExistsError: # Si le fichier existe deja
        remove("partie_en_cours.txt") # On supprime le fichier
        fichier = open("partie_en_cours.txt", "x") # On ouvre a nouveau
    modification_symbole_sauvegarder(grille_info) # On transforme les symboles de la grille en integer
    fichier.write(str(grille_info[1]) + "\n") # On sauvegarde la taille de la grande grille
    fichier.write(str(grille_info[2]) + "\n") # On sauvegarde la taille de la petite grille
    fichier.write(str(dernier_joueur) + "\n") # On sauvegarde le numero du dernier joueur ayant joue
    fichier.write(str(nb_joueurs) + "\n") # On sauvegarde le nombre de joueurs dans la partie (de 2 a 4)
    grille_modifiee = transformation_dimension(grille_info) # On transforme la dimention de la grille afin de 
    variable = ""
    for i in range(0, len(grille_modifiee)):
        for j in range(0, len(grille_modifiee[0])):
            variable = variable + str(grille_modifiee[i][j]) # On met la grille dans la variable
    fichier.write(variable) # on met la variable dans le fichier texte
    fichier.close() # On ferme le fichier


def charger_grille():
    """
    Entree : Aucune
    Sortie : On charge les informations de la grille a partir du fichier texte et les informations de la partie necessaires pour la reprendre
    """
    grille_info = [0] # on initialise la grille
    fichier = open ("partie_en_cours.txt", "r")
    grille_info.append(int(fichier.readline().strip("\n"))) # On ajoute la taille de la grille
    grille_info.append(int(fichier.readline().strip("\n"))) # On ajoute la taille de la grille
    dernier_joueur = int(fichier.readline().strip("\n")) # On ajoute la taille de la petite grille
    nb_joueurs = int(fichier.readline().strip("\n")) # On ajoute le nombre de joueurs
    variable = fichier.readline() # On lit la variable
    grille_info[0] = [[[[int(variable[i * grille_info[2] ** 2 * grille_info[1] + j * grille_info[2] + k * grille_info[2] * grille_info[1] + l]) # On remet la grille dans la variable
                         for l in range(grille_info[2])]
                         for k in range(grille_info[2])]
                         for j in range(grille_info[1])]
                         for i in range(grille_info[1])]
    modification_symbole_charger(grille_info) # On remet les symboles de la grille en string (car on a transforme les symboles en integer pour pouvoir les sauvegarder)
    fichier.close() # On ferme le fichier
    return grille_info, dernier_joueur, nb_joueurs


def alignement_victoire(grille_info): # fonction qui calcule la taille de la victoire
    taille_victoire = round((76/100) * (grille_info[1] * grille_info[2])) # On fait 76% de la taille de la grille (logique: 76% est le pourcentage minimal pour conserver le 5 alignement sur une grille en 2x2x3)
    return taille_victoire


def modification_symbole_sauvegarder(grille_info, j1=SYMBOLE_JOUEUR_1, j2=SYMBOLE_JOUEUR_2, j3=SYMBOLE_JOUEUR_3, j4=SYMBOLE_JOUEUR_4, vide=SYMBOLE_VIDE):
    """
    Entree: Les informations de la grille, les symboles des joueurs et le symbole vide
    Sortie : Aucune mais on modifie les symboles de la grille en integer
    """
    for Glig in range(0, grille_info[1]): # On parcourt la grille
        for Gcol in range(0, grille_info[1]): # On parcourt la grille
            for lig in range(0, grille_info[2]): # On parcourt la grille
                for col in range(0, grille_info[2]): # On parcourt la grille
                    if grille_info[0][Glig][Gcol][lig][col] == j1: # Si le symbole est le symbole du joueur 1
                        grille_info[0][Glig][Gcol][lig][col] = 1 # On le remplace par 1
                    if grille_info[0][Glig][Gcol][lig][col] == j2: # Si le symbole est le symbole du joueur 2
                        grille_info[0][Glig][Gcol][lig][col] = 2 # On le remplace par 2
                    if grille_info[0][Glig][Gcol][lig][col] == j3: # Si le symbole est le symbole du joueur 3
                        grille_info[0][Glig][Gcol][lig][col] = 3 #  On le remplace par 3
                    if grille_info[0][Glig][Gcol][lig][col] == j4: # Si le symbole est le symbole du joueur 4
                        grille_info[0][Glig][Gcol][lig][col] = 4 # On le remplace par 4
                    if grille_info[0][Glig][Gcol][lig][col] == vide: # Si le symbole est le symbole vide
                        grille_info[0][Glig][Gcol][lig][col] = 0 # On le remplace par 0


def modification_symbole_charger(grille_info, j1=SYMBOLE_JOUEUR_1, j2=SYMBOLE_JOUEUR_2, j3=SYMBOLE_JOUEUR_3, j4=SYMBOLE_JOUEUR_4, vide=SYMBOLE_VIDE):
    """
    Entree: Les informations de la grille, les symboles des joueurs et le symbole vide
    Sortie : Aucune mais on modifie les symboles de la grille en integer
    """
    for Glig in range(0, grille_info[1]): # On parcourt la grille
        for Gcol in range(0, grille_info[1]): # On parcourt la grille
            for lig in range(0, grille_info[2]): # On parcourt la grille
                for col in range(0, grille_info[2]): # On parcourt la grille
                    if grille_info[0][Glig][Gcol][lig][col] == 1: # si la valeur est 1
                        grille_info[0][Glig][Gcol][lig][col] = j1 # On remplace par le symbole du joueur 1
                    if grille_info[0][Glig][Gcol][lig][col] == 2: # si la valeur est 2
                        grille_info[0][Glig][Gcol][lig][col] = j2 # On remplace par le symbole du joueur 2
                    if grille_info[0][Glig][Gcol][lig][col] == 3: # si la valeur est 3
                        grille_info[0][Glig][Gcol][lig][col] = j3 # On remplace par le symbole du joueur 3
                    if grille_info[0][Glig][Gcol][lig][col] == 4: # si la valeur est 4
                        grille_info[0][Glig][Gcol][lig][col] = j4 # On remplace par le symbole du joueur 4
                    if grille_info[0][Glig][Gcol][lig][col] == 0: # si la valeur est 0
                        grille_info[0][Glig][Gcol][lig][col] = vide # On remplace par le symbole vide
