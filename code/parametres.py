SYMBOLE_JOUEUR_1 = "⦿" # Initialise le suymbole du joueur 1
SYMBOLE_JOUEUR_2 = "⦾" # Initialise le suymbole du joueur 2
SYMBOLE_VIDE = "." # Initialise le suymbole d'une case vide

grille = [[], [], [], []]  # Initialise la grille
sous_grille = [[[],[],[]],[[],[],[]],[[],[],[]]] # Grille d'un seul morpion

def copie_liste(liste):
    """Copie une liste"""
    copie = []
    for element in liste:
        copie.append(element)
    return copie

# Mettre sous grille dans chaque case de grille

for i in enumerate(grille): # Pour chaque case de grille
    grille[i[0]] = copie_liste(sous_grille) # Copie la sous grille dans chaque case de grille

print(grille)
