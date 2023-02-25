from affichage import afficher_grille
from parametres import copie_profonde_liste, initialisation_grille

grille_info = initialisation_grille()

def rotation(grille_info):
    grille = grille_info[0]
    taille_petite_grille = grille_info[2]
    sauvegarde = copie_profonde_liste(grille_info)
    for colonne in range(0, taille_petite_grille):
        ligne = taille_petite_grille - colonne - 1
        for element in range(0, taille_petite_grille):
            grille[element][colonne] = sauvegarde[ligne][element]
            
print(rotation())
