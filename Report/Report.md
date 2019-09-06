# Présentation
Le but du projet est de réaliser un jeu de labyrinthe. Le joueur part d’un point de départ et doit arriver à la sortie du labyrinthe en ayant collecté un certain nombre d’objets sur son chemin afin de neutraliser le gardien situé à la sortie !
Le jeu tourne autour de l’univers de MacGyver. Le joueur prend le contrôle du héros de la série.

## Ressources
Ce jeu utilise des ressources graphiques, fournies en amont du projet, telles que des images des personnages, des textures pour le labyrinthe ainsi que les d’objets à collecter. Toutes ces ressources sont stockées dans le répertoire « ressources/» à la racine du projet.

## Fonctionnalités
Les fonctionnalités de base demandées dans le jeu sont les suivantes:
- Le jeu comporte un seul niveau.
- Le niveau est écrit dans un fichier facilement modifiable.
- Le héros se déplace grâce aux flèches directionnelles du clavier.
- Le labyrinthe a un format de 15x15 sprites (cases).
- Les objets, que le héros collecte, sont placés de manière aléatoire dans le labyrinthe. Ainsi pour chaque partie les objets ne sont pas au même endroit.
- Le héros ramasse les objets dès qu’il se trouve sur la même case que ceux-ci.
- Si le héros se présente devant le gardien sans avoir collecté l’ensemble des objets, il perd la partie. Donc le héros gagne uniquement si il a tout les objets et qu’il trouve la sortie.
- Le programme doit pouvoir s’exécuter sur n’importe quel ordinateur.

## Technologies
Il est demandé de réaliser le programme en utilisant **Python 3**.
Le programme s'appuie aussi sur l’utilisation du module Pygame permettant la réalisation rapide de jeu avec le langage python (création de fenêtre graphique, gestion de la souris et du clavier, etc.).
Dans le présent programme les versions utilisées sont :
- Python 3.7.4 : https://www.python.org/
- Pygame 1.9.6 : https://www.pygame.org/

# Installation et utilisation

## Dépôt
L’ensemble du code source est hébergé sur la plateforme [GitHub](http://github.com). Le dépôt contenant ce code source est le suivant : https://github.com/GuillaumeOj/HelpMacGyver
Pour récupérer ce code source, vous avez deux possibilités:
1. En cliquant sur « Clone or download » vous pouvez télécharger l’ensemble du code source au format zip:
![Clone or Download source code](/img/CloneDownloadSourceCode.png)
2. En utilisant le logiciel [Git](https://git-scm.com/) (voir l'[Aide](https://git-scm.com/doc) du logiciel). Dans votre console favorite, dirigez vous vers le dossier de destination du code source puis tapez la commande suivante:
```
git clone git@github.com:GuillaumeOj/HelpMacGyver.git
or
git clone https://github.com/GuillaumeOj/HelpMacGyver.git
```

## Installation
Une fois le code source récupéré vous allez pouvoir passer à l'installation des éléments nécessaires au bon fonctionnement du programme.
