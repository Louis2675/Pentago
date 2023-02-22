from parametres import initialisation_grille

def afficher_grille(grille): # Procédure
    '''
    Sortie : - Super affichage de la grille
    '''
    print("     ", end="")
    for i in range(PPP):
        for j in range(NNN):
            print("  " + chr(i*NNN + j + 65), end=" ")
        print("  ", end = "")
    print()
    for m in range(PPP):
        print("     ", end="")
        print((style_haut_gauche[0] + style_haut_milieu[0]*(NNN-2) + style_haut_droit[0] + " ")*PPP)
        print(" "*(2 - (m*NNN + 1)//10), m*NNN + 1 , end=" ")
        for k in range(PPP):
            for i in range(NNN):
                print("│ " + style_pion[grille[m][k][0][i]] + " ", end="")
            print("│ ", end="")
        print()
        print("     ", end="")
        print((style_haut_gauche[1] + style_haut_milieu[1]*(NNN-2) + style_haut_droit[1] + " ")*PPP)
        for i in range(NNN-2):
            print(" "*(2 - (m*NNN + 2)//10), m*NNN + i + 2, end=" ")
            for k in range(PPP):
                for j in range(NNN):
                    print("│ " + style_pion[grille[m][k][i+1][j]] + " ", end="")
                print("│ ", end="")
            print()
            print("     ", end="")    
            print((style_milieu_gauche + style_milieu_milieu*(NNN-2) + style_milieu_droit + " ")*PPP)
        print(" "*(2 - (m*NNN + NNN)//10), m*NNN + NNN, end=" ")
        for k in range(PPP):
            for i in range(NNN):
                print("│ " + style_pion[grille[m][k][NNN-1][i]] + " ", end="")
            print("│ ", end="")
        print()
        print("     ", end="")
        print((style_bas_gauche + style_bas_milieu*(NNN-2) + style_bas_droit + " ")*PPP)


style_haut_gauche = ["┌───┬", "├───┼"]
style_milieu_gauche = "├───┼"
style_bas_gauche = "└───┴"
style_haut_milieu = ["───┬", "───┼"]
style_milieu_milieu = "───┼"
style_bas_milieu = "───┴"
style_haut_droit = ["───┐", "───┤"]
style_milieu_droit = "───┤"
style_bas_droit = "───┘"

style_pion = ["·", "\033[31m●\033[0m", "\033[34m●\033[0m"]

NNN = 0
PPP = 0
LLL = 0


grille = initialisation_grille()

print(afficher_grille(grille))