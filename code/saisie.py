
def demander_nb_joueurs():
    entree_valide = False
    while not entree_valide == True:
        try:
            nb_joueurs = int(input("Combien de joueurs vont jouer ? (min. 2) : "))
            if nb_joueurs >= 2:
                entree_valide = True
            else: print("Veuillez entrer un nombre entier supérieur ou égal à 2 : ")
        except ValueError:
            print("Veuillez entrer un nombre entier : ")
    return nb_joueurs


def demander_symbole(nb_joueurs):
    symboles_joueurs = []
    while len(symboles_joueurs) < nb_joueurs:
        symbole = input("Entrez le symbole du joueur " + str(len(symboles_joueurs) + 1) + " : ")
        if len(symbole) == 1:
            symboles_joueurs.append(symbole)
        else: print("Veuillez entrer un symbole d'un seul caractere : ")
        for i in range (0, len(symboles_joueurs) -1):
            if str(symbole) == symboles_joueurs[i]:
                symboles_joueurs.pop()
    return symboles_joueurs
