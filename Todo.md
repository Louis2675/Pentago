# Pentago
 
 - Faire un random pour choisir quel joueur commence
 - Finir `jouer_tour()`
 - Verifier si le remplacement des `tuple()` et des `list()` marche dans la version finale
 - Si il y a une erreur venant de `rotation_gauche()` et/ou `rotation_droite()` ça vient peut-être des return qu'on a enlevé pour les transformer en procédures
  - Tester à fond pour voir si l'alignement marche
 - Enlever les "." en tant que `symbole_vide`
 - ARRETER LE JEU QUAND AUCUNE CASE EST RESTANTE
 - Pour les sauvegardes un fix leit etre de le faire que pour une grille en 2x3 a 2 joueurs (car on peut avoir des problemes pour encoder tous les symboles en multi...
  - Demander si `jouer_case()` et `rotation_grille` doivent être dans saisie.py ou tour_de_jeu.py