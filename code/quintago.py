from saisie import demander_nb_joueurs, demander_symbole
from parametres import SYMBOLE_JOUEUR_1, SYMBOLE_JOUEUR_2


def nb_joueurs():
    nb_joueurs = demander_nb_joueurs()
    if nb_joueurs == 2:
        symboles_joueurs = [SYMBOLE_JOUEUR_1, SYMBOLE_JOUEUR_2]
    if nb_joueurs > 2: 
        symboles_joueurs = demander_symbole(nb_joueurs)
    return symboles_joueurs
