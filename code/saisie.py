
def demander_nb_joueurs():
    entree_valide = False
    while not entree_valide == True:
        try:
            nb_joueurs = int(input("Combien de joueurs vont jouer ? (min. 2;  max. 4) : "))
            if nb_joueurs >= 2 and nb_joueurs <= 4:
                entree_valide = True
            else: print("Veuillez entrer un nombre entier entre 2 et 4 : ")
        except ValueError:
            print("Veuillez entrer un nombre entier : ")
    return nb_joueurs