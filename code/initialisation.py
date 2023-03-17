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
    grille_copie = []
    for Glig in range(grille_info[1]):
        for lig in range(grille_info[2]):
            grille_copie.append([])
            copie_lig = lig + Glig * grille_info[2]
            for Gcol in range(grille_info[1]):
                for col in range(grille_info[2]):
                    grille_copie[copie_lig].append(grille_info[0][Glig][Gcol][lig][col])
    return grille_copie


def test_victoire(grille_info, taille_victoire, symboles_joueurs):
    liste_gagnants = []
    resultat = 0
    grille_modifiee = transformation_dimension(grille_info)
    for i in range(0, len(symboles_joueurs)):
        if alignement_horizontal(grille_modifiee, taille_victoire, symboles_joueurs[i]) == True or alignement_vertical(grille_modifiee, taille_victoire, symboles_joueurs[i]) == True or alignement_diagonal(grille_modifiee, taille_victoire, symboles_joueurs[i]) == True:
            liste_gagnants.append(i)
            resultat = True
    if len(liste_gagnants) > 1:
        resultat = -1
    return (resultat, liste_gagnants)


def initialisation_joueurs(symboles_joueurs):
    nb_joueurs = demander_nb_joueurs()
    while len(symboles_joueurs) > nb_joueurs:
        symboles_joueurs.pop()
    return nb_joueurs


def sauvegarder_grille(grille_info, dernier_joueur, nb_joueurs):
    try:
        fichier = open("partie_en_cours.txt", "x")
    except FileExistsError:
        remove("partie_en_cours.txt")
        fichier = open("partie_en_cours.txt", "x")
    modification_symbole_sauvegarder(grille_info)
    fichier.write(str(grille_info[1]) + "\n")
    fichier.write(str(grille_info[2]) + "\n")
    fichier.write(str(dernier_joueur) + "\n")
    fichier.write(str(nb_joueurs) + "\n")
    grille_modifiee = transformation_dimension(grille_info)
    variable = ""
    for i in range(0, len(grille_modifiee)):
        for j in range(0, len(grille_modifiee[0])):
            variable = variable + str(grille_modifiee[i][j])
    fichier.write(variable)
    fichier.close()


def charger_grille():
    grille_info = [0]
    fichier = open ("partie_en_cours.txt", "r")
    grille_info.append(int(fichier.readline().strip("\n"))) # On ajoute la taille de la grille
    grille_info.append(int(fichier.readline().strip("\n"))) # On ajoute la taille de la grille
    dernier_joueur = int(fichier.readline().strip("\n")) # On ajoute la taille de la petite grille
    nb_joueurs = int(fichier.readline().strip("\n")) # On ajoute le nombre de joueurs
    variable = fichier.readline()
    grille_info[0] = [[[[int(variable[i * grille_info[2] ** 2 * grille_info[1] + j * grille_info[2] + k * grille_info[2] * grille_info[1] + l])
                         for l in range(grille_info[2])]
                         for k in range(grille_info[2])]
                         for j in range(grille_info[1])]
                         for i in range(grille_info[1])]
    modification_symbole_charger(grille_info)
    fichier.close()
    return grille_info, dernier_joueur, nb_joueurs



def alignement_victoire(grille_info):
    taille_victoire = round((76/100) * (grille_info[1] * grille_info[2]))
    return taille_victoire


def modification_symbole_sauvegarder(grille_info, j1=SYMBOLE_JOUEUR_1, j2=SYMBOLE_JOUEUR_2, j3=SYMBOLE_JOUEUR_3, j4=SYMBOLE_JOUEUR_4, vide=SYMBOLE_VIDE):
    for Glig in range(0, grille_info[1]):
        for Gcol in range(0, grille_info[1]):
            for lig in range(0, grille_info[2]):
                for col in range(0, grille_info[2]):
                    if grille_info[0][Glig][Gcol][lig][col] == j1:
                        grille_info[0][Glig][Gcol][lig][col] = 1
                    if grille_info[0][Glig][Gcol][lig][col] == j2:
                        grille_info[0][Glig][Gcol][lig][col] = 2
                    if grille_info[0][Glig][Gcol][lig][col] == j3:
                        grille_info[0][Glig][Gcol][lig][col] = 3
                    if grille_info[0][Glig][Gcol][lig][col] == j4:
                        grille_info[0][Glig][Gcol][lig][col] = 4
                    if grille_info[0][Glig][Gcol][lig][col] == vide:
                        grille_info[0][Glig][Gcol][lig][col] = 0


def modification_symbole_charger(grille_info, j1=SYMBOLE_JOUEUR_1, j2=SYMBOLE_JOUEUR_2, j3=SYMBOLE_JOUEUR_3, j4=SYMBOLE_JOUEUR_4, vide=SYMBOLE_VIDE):
    for Glig in range(0, grille_info[1]):
        for Gcol in range(0, grille_info[1]):
            for lig in range(0, grille_info[2]):
                for col in range(0, grille_info[2]):
                    if grille_info[0][Glig][Gcol][lig][col] == 1:
                        grille_info[0][Glig][Gcol][lig][col] = j1
                    if grille_info[0][Glig][Gcol][lig][col] == 2:
                        grille_info[0][Glig][Gcol][lig][col] = j2
                    if grille_info[0][Glig][Gcol][lig][col] == 3:
                        grille_info[0][Glig][Gcol][lig][col] = j3
                    if grille_info[0][Glig][Gcol][lig][col] == 4:
                        grille_info[0][Glig][Gcol][lig][col] = j4
                    if grille_info[0][Glig][Gcol][lig][col] == 0:
                        grille_info[0][Glig][Gcol][lig][col] = vide