from parametres import SYMBOLE_VIDE, SYMBOLE_JOUEUR_1, SYMBOLE_JOUEUR_2
from tests_alignements import alignement_horizontal, alignement_vertical, alignement_diagonal
from saisie import demander_nb_joueurs, demander_symbole


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


def initialisation_joueurs():
    nb_joueurs = demander_nb_joueurs()
    if nb_joueurs == 2:
        symboles_joueurs = [SYMBOLE_JOUEUR_1, SYMBOLE_JOUEUR_2]
    if nb_joueurs > 2: 
        symboles_joueurs = demander_symbole(nb_joueurs)
    return symboles_joueurs, nb_joueurs


def sauvegarder_grille(grille_info, dernier_joueur):
    fichier = open("partie_en_cours.txt", "x")
    fichier.write(str(grille_info[1]) + "\n")
    fichier.write(str(grille_info[2]) + "\n")
    fichier.write(str(dernier_joueur) + "\n")
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
    variable = fichier.readline()
    grille_info[0] = [[[[int(variable[i * grille_info[2] ** 2 * grille_info[1] + j * grille_info[2] + k * grille_info[2] * grille_info[1]]) for l in range(grille_info[2])] for k in range(grille_info[2])] for j in range(grille_info[1])] for i in range(grille_info[1])]
    fichier.close()
    return grille_info, dernier_joueur


def alignement_victoire(grille_info):
    taille_victoire = round((76/100) * (grille_info[1] * grille_info[2]))
    return taille_victoire


# def alignement_horizontal(grille_modifiee, taille_liste_gagnants, Symboles = [SYMBOLE_JOUEUR_1, SYMBOLE_JOUEUR_2]):
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
#             if compteur >= taille_liste_gagnants:
#                 return True
#     return False       
            

# def alignement_vertical(grille_modifiee, taille_liste_gagnants, Symboles = [SYMBOLE_JOUEUR_1, SYMBOLE_JOUEUR_2]):
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
#         if compteur >= taille_liste_gagnants:
#             return True
#     return False


# def alignement_diagonal(grille_modifiee, taille_liste_gagnants, Symboles = [SYMBOLE_JOUEUR_1, SYMBOLE_JOUEUR_2]):
#     compteur = 0
#     for i in range(1, len(grille_modifiee[0])):
#         if grille_modifiee[-i -1][i] == grille_modifiee[-i][i -1] == Symboles[1] or grille_modifiee[-i -1][i] == grille_modifiee[-i][i -1] == Symboles[0]:
#             if compteur == 0:
#                 compteur = compteur + 2
#             else:
#                 compteur = compteur + 1
#             if compteur == taille_liste_gagnants:
#                 return True
#     else: 
#         for i in range(1, len(grille_modifiee[0])):
#             if grille_modifiee[i][i] == grille_modifiee[i -1][i -1] == Symboles[1] or grille_modifiee[i][i] == grille_modifiee[i - 1][i -1] == Symboles[0]:
#                 if compteur == 0:
#                     compteur = compteur + 2
#                 else:
#                     compteur = compteur + 1
#                 if compteur == taille_liste_gagnants:
#                     return True