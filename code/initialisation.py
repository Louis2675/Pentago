from parametres import SYMBOLE_VIDE
from tests_alignements import alignement_horizontal, alignement_vertical, alignement_diagonnal


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


def test_victoire():
    return None

# def alignement_horizontal(grille_modifiee, taille_victoire, Symboles = [SYMBOLE_JOUEUR_1, SYMBOLE_JOUEUR_2]):
#     for ligne in range(0, len(grille_modifiee)):
#         compteur = 0
#         for colonne in range(1, len(grille_modifiee[ligne])):
#             if grille_modifiee[0][ligne] == grille_modifiee[ligne][colonne - 1] == Symboles[1] or grille_modifiee[ligne][colonne] == grille_modifiee[ligne][colonne - 1] == Symboles[0]:
#                 if compteur == 0:
#                     compteur = compteur + 2
#                 else:
#                     compteur = compteur + 1
#             else:
#                 compteur = 0
#             if compteur >= taille_victoire:
#                 return True
#     return False       
            

# def alignement_vertical(grille_modifiee, taille_victoire, Symboles = [SYMBOLE_JOUEUR_1, SYMBOLE_JOUEUR_2]):
#     for colonne in range(0, len(grille_modifiee)):
#         compteur = 0
#         for ligne in range(1, len(grille_modifiee)): #Ne va pas jusqu'au bout, peut etre à cause de la grille temporaire, à tester sur la vraie grille
#             if grille_modifiee[ligne][colonne] == grille_modifiee[ligne -1][colonne] == Symboles[1] or grille_modifiee[ligne][colonne] == grille_modifiee[ligne -1][colonne] == Symboles[0]:
#                 if compteur == 0:
#                     compteur = compteur + 2
#                 else:
#                     compteur = compteur + 1
#             else:
#                 compteur = 0
#         if compteur >= taille_victoire:
#             return True
#     return False


# def alignement_diagonnal(grille_modifiee, taille_victoire, Symboles = [SYMBOLE_JOUEUR_1, SYMBOLE_JOUEUR_2]):
#     compteur = 0
#     for i in range(1, len(grille_modifiee[0])):
#         if grille_modifiee[-i -1][i] == grille_modifiee[-i][i -1] == Symboles[1] or grille_modifiee[-i -1][i] == grille_modifiee[-i][i -1] == Symboles[0]:
#             if compteur == 0:
#                 compteur = compteur + 2
#             else:
#                 compteur = compteur + 1
#             if compteur == taille_victoire:
#                 return True
#     else: 
#         for i in range(1, len(grille_modifiee[0])):
#             if grille_modifiee[i][i] == grille_modifiee[i -1][i -1] == Symboles[1] or grille_modifiee[i][i] == grille_modifiee[i - 1][i -1] == Symboles[0]:
#                 if compteur == 0:
#                     compteur = compteur + 2
#                 else:
#                     compteur = compteur + 1
#                 if compteur == taille_victoire:
#                     return True