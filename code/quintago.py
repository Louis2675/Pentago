"""Ce fichier contient le code principal du jeu Quintago, il permet de lancer une partie et de jouer une partie"""

from tests_alignements import test_grille_pleine
from tour_de_jeu import jouer_tour
from initialisation import initialisation_grille, initialisation_joueurs, test_victoire, alignement_victoire, charger_grille, sauvegarder_grille
from affichage import afficher_grille, bienvenue
from os import remove
from parametres import symboles
from saisie import ordre_joueurs


def jouer(symboles): # Fonction qui permet de jouer une partie 
    """
    Entree : La liste des symboles
    Sortie: Aucune permet juste de lancer une partie
    """
    bienvenue()
    a = input("Appuyez sur entrée pour commencer la partie ou entrez 'charger' pour charger une sauvegarde (ne fonctionne que si un fichier sauvegarde existe) : ")
    print()
    if a == "charger": # Si l'utilisateur veut charger une partie
        try:
            fichier = open("partie_en_cours.txt", "r") # On ouvre le fichier
            fichier.close() # On ferme le fichier
            print("Une sauvegarde a été trouvée") # On affiche un message qui dit que la sauvegarde a été trouvée
            grille_info, dernier_joueur, nb_joueurs = charger_grille() # On charge la grille
            symboles_joueurs = symboles[:-1] # On initialise la liste des symboles des joueurs
            while len(symboles_joueurs) > nb_joueurs: # Tant que la liste des symboles est plus grande que le nombre de joueurs
                symboles_joueurs.pop() # On enleve le dernier element de la liste
        except FileNotFoundError: # Si le fichier n'existe pas
            a = None # On met la valeur de a en None

    if a != "charger": # Si l'utilisateur ne veut pas charger une partie
        symboles_joueurs = symboles[:-1] # On initialise la liste des symboles des joueurs
        grille_info = initialisation_grille() # On initialise la grille
        print()
        info_joueurs = initialisation_joueurs(symboles_joueurs) # On initialise les joueurs
        print()
        ordre_joueurs(info_joueurs) # On met un ordre des joueurs aleatoire
        print()
        dernier_joueur = 0 # On initialise le dernier joueur
        nb_joueurs = info_joueurs # On initialise le nombre de joueurs dans la variable nb_joueurs

    victoire = test_grille_pleine(grille_info, symboles) # On teste si la grille est pleine (car en cas de sauvegarde c'est pontiellement le cas)
    if victoire == True: # Si la grille est pleine
        print("Match nul, la grille est pleine") # On affiche un message qui dit que la grille est pleine
        remove("partie_en_cours.txt") # On supprime le fichier de sauvegarde

    taille_victoire = alignement_victoire(grille_info) # On initialise la taille de l'alignement necessaire pour gagner
    print("La taille de l'alignement necessaire est de", taille_victoire, "pour cette partie") # On informe le joueur de l'alignement necessaire pour gagner

    while victoire == False : # Tant que personne n'a gagne ou que la grille n'est pas pleine
        sortie = False # On initialise la variable sortie
        while dernier_joueur < len(symboles_joueurs) and sortie == False: # Tant que le dernier joueur est inferieur au nombre de joueurs et que la variable sortie est egale a False
            entree_pleine = True # On initialise la variable entree_pleine
            print()
            afficher_grille(grille_info) # afficher la grille
            print()
            jouer_tour(grille_info, dernier_joueur, symboles_joueurs) # On fait jouer le joueur
            print()
            afficher_grille(grille_info) # On affiche la grille
            print()
            liste_victoire = test_victoire(grille_info, taille_victoire, symboles_joueurs) # On teste si un joueur a gagne
            if liste_victoire[0] == 0: # Si personne n'a gagne
                victoire = False
            elif liste_victoire[0] == True: # Si un joueur a gagne
                victoire = True
                print("Le joueur", liste_victoire[1 + 1], "a gagné")
                sortie = True
            elif liste_victoire[0] == -1: # Si il y a match nul
                victoire = True
                print("Match nul, les joueurs", liste_victoire[1], "ont gagné et les autres ont perdu")
                sortie = True
            if victoire == True: # Si un joueur a gagne
                try: # On supprime le fichier de sauvegarde
                    fichier = open("partie_en_cours.txt", "r") # On ouvre et ferme le fichier pour verifier s'il existe
                    fichier.close()
                    remove("partie_en_cours.txt")
                    sortie = True
                except FileNotFoundError: # Si le fichier n'existe pas
                    pass # On ne fait rien
            if victoire == False: # Si personne n'a gagne
                a = input("Appuyez sur entrée pour continuer ou entrez 'sauvegarde' pour sauvegarder la partie : ") # On demande a l'utilisateur s'il veut sauvegarder la partie
                if a == "sauvegarde": # Si l'utilisateur veut sauvegarder la partie
                    sauvegarder_grille(grille_info, dernier_joueur + 1, nb_joueurs) # On sauvegarde la partie
                    print("La partie a été sauvegardée")
                    victoire = True # On met la variable victoire a True pour sortir de la boucle
                    sortie = True # On met la variable sortie a True pour sortir de la boucle
                    entree_pleine = False # On met la variable entree_pleine a False pour ne pas tester si la grille est pleine
                grille_pleine = test_grille_pleine(grille_info, symboles) # On teste si la grille est pleine
                if grille_pleine == True and entree_pleine == True: # Si la grille est pleine et que la variable entree_pleine est egale a True
                    victoire = True # On met la variable victoire a True pour sortir de la boucle
                    print("Match nul, la grille est pleine") # On affiche un message qui dit que la grille est pleine et donc match match nul
                    sortie = True # On met la variable sortie a True pour sortir de la boucle
            dernier_joueur = dernier_joueur + 1 # On incremente le dernier joueur
        dernier_joueur = 0 # On remet le dernier joueur a 0


jouer(symboles)