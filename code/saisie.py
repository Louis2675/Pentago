"""Ce fichier contient les fonctions d'affichage du jeu"""


from random import shuffle


def demander_nb_joueurs(): # Demande le nombre de joueurs
    """
    Entree : par l'utilisateur du nombre de joueurs avec une input
    Sortie : le nombre de joueurs
    """
    entree_valide = False 
    while not entree_valide == True: # Si entree non valide
        try:
            nb_joueurs = int(input("Combien de joueurs vont jouer ? (min. 2;  max. 4) : ")) # On demande le nombre de joueurs
            if nb_joueurs >= 2 and nb_joueurs <= 4: # on verifie que le nombre de joueurs est entre 2 et 4
                entree_valide = True 
            else: print("Veuillez entrer un nombre entier entre 2 et 4 : ")
        except ValueError: # on verifie si l'entree est un nombre entier
            print("Veuillez entrer un nombre entier : ")
    return nb_joueurs # on retourne le nombre de joueurs 


def ordre_joueurs(nb_joueurs): # Demande les noms des joueurs et les mets dans une liste
    """
    Entree : Le nombre de joueurs + par l'utilisateur des noms de joueurs
    Sortie : Rien, procedure. Affiche les noms des joueurs dans l'ordre de jeu
    """
    entree_valide = False # On initialise la variable entree_valide a False
    while entree_valide == False: # Tant que l'entree n'est pas valide
        joueurs = input("Veuillez entrer les noms des {} joueurs séparés par une virgule (ex. Maxime, Louis): ".format(str(nb_joueurs))) # On demande les noms
        joueurs = joueurs.replace(" ", "") # On enleve les espaces inutiles
        joueurs = joueurs.split(",") # On met les noms dans une liste

        if len(joueurs) == nb_joueurs: # On verifie que le nombre de noms est le bon
            shuffle(joueurs) # On melange la liste des noms
            for i in range(0, len(joueurs)): # On affiche les noms dans l'ordre de jeu
                print("Le joueur", str(i + 1), "est", joueurs[i]) # On affiche le nom du joueur
                entree_valide = True # On met entree_valide a True
        else:
            print("Erreur: Vous n'avez pas entré le bon nombre de joueurs") # On affiche un message d'erreur
        for i in range(0, len(joueurs)):
            if joueurs[i] == "":
                print("Erreur: Vous avez entré un nom vide") # On affiche un message d'erreur