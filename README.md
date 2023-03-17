# Le jeu du Quintago

<img alt="GitHub Pipenv locked Python version" src="https://img.shields.io/github/pipenv/locked/python-version/Louis2675/Pentago?label=Python"> <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/y/Louis2675/Pentago?color=brightgreen"> <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/Louis2675/Pentago?color=blueviolet"> <img alt="GitHub release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/Louis2675/Pentago?color=yellow&include_prereleases&label=version">

Trouvez les règles du jeu <a href="https://fr.wikipedia.org/wiki/Pentago">ici.</a>
___

## Setup 

<p>Clonez <a href="https://github.com/Louis2675/Pentago">cette repo GitHub</a> sur votre ordinateur (ou téléchargez les fichiers directement) puis lancez le fichier <code>quintago.py</code> pour jouer au jeu.</p>

### Alternatives en cas de problème avec le lancement du jeu

Lancer le fichier via **Powershell** : 

1. Localiser le directoire dans lequel vous avez téléchargé le dossier 
```powershell
cd <votre directoire>
```
2. Une fois que votre terminal est pointé vers le bon dossier utilisez la commande suivante
```powershell
 python -u "<votre directoire>/quintago.py"
```

## Informations relatives au projet

### Arborescence du projet
Voici l'arborescence des fichiers du projet et leur fonction
<a href='https://www.linkpicture.com/view.php?img=LPic640c98b59034f1961891353'><img src='https://www.linkpicture.com/q/Screenshot-2023-03-11-160405.png' type='image'></a>

### Paramètres et librairies utilisés

- `SYMBOLE_JOUEUR_1` : Ce symbole sert à remplir la grille quand le joueur 1 a rempli une case (● - rouge)
- `SYMBOLE_JOUEUR_2` : Ce symbole sert à remplir la grille quand le joueur 1 a rempli une case (● - bleu)
- `SYMBOLE_JOUEUR_3` : Ce symbole sert à remplir la grille quand le joueur 1 a rempli une case (● - jaune)
- `SYMBOLE_JOUEUR_4` : Ce symbole sert à remplir la grille quand le joueur 1 a rempli une case (● - violet)
- `SYMBOLE_VIDE` : Ce symbole sert à remplir la grille quand une case est vide (.)
- `symboles` : liste contenant les symboles des joueurs

- `os (.remove)` : Cette librairie nous permet de supprimer un fichier

## Remerciements

<p> Merci à <a href="shields.io">shields.io</a> et <a href="xmind.app">xmind.app</a> pour les badges de statistiques et l'arborescence sur le fichier <code>README.md</code></p>
<details>
 <Summary>Auteurs du projet...</summary>
	<br>
 <ul>
    <li> <a href="https://github.com/Louis2675">Louis Declerck</a>
    <li> <a href="https://github.com/sp3ymaXx">Maxime Becquaert</a>
 </ul>
</details>
