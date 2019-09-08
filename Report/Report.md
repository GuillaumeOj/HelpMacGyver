# Présentation
Le but du projet est de réaliser un jeu de labyrinthe. La ou le joueu·r·se part d’un point de départ et doit arriver à la sortie du labyrinthe en ayant collecté un certain nombre d’objets sur son chemin afin de neutraliser le gardien situé à la sortie !
Le jeu tourne autour de l’univers de MacGyver. La ou le joueu·r·se prend le contrôle du héros de la série.

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
Pour récupérer ce code source, il y a deux possibilités :
1. En cliquant sur « Clone or download » on télécharge l’ensemble du code source au format zip que l'on décompresse dans un dossier de notre choix :

![Clone or Download source code](img/CloneDownloadSourceCode.png)

2. Ou en utilisant le logiciel [Git](https://git-scm.com/) (voir l'[Aide](https://git-scm.com/doc) du logiciel). Dans une console, on se dirige sur le dossier de destination du code source puis on tape la commande suivante:
```
git clone git@github.com:GuillaumeOj/HelpMacGyver.git
ou
git clone https://github.com/GuillaumeOj/HelpMacGyver.git
```

## Installation
Une fois le code source récupéré il reste l'installation du module `pygame`.
Pour une bonne utilisation, il est conseillé d'utiliser un environnement virtuel tel que [Virtualenv](https://github.com/pypa/virtualenv) (voir la [documentation](https://virtualenv.pypa.io/en/latest/#)).
Une fois que Vitualenv est installé, on se positionne sur le répertoire contenant le projet et on lance la commande suivante dans une console :
```
virtualenv -p python3 env
```
ou sur PowerShell:
```powershell
virtualenv -p $env:python3 env
```
Ensuite pour activer l'environnement virtuel on tape la commande suivante :
```
source env/bin/activate
```
ou sur PowerShell:
```powershell
.env/scripts/activate.ps1
```
Enfin, grâce au module `pip` on installe les modules nécessaires au fonctionnement du programme (*pygame*) :
```
pip install -r requirements.txt
```

## Exécution
Pour exécuter le programme on lance la commande suivante dans une console :
```
python main.py
```
Toute les instructions d'installation sont récapitulées dans le fichier [readme.md](../readme.md) présent à la racine du code source.

# Découpage du programme
Le programme est constitué d'un script principal, `main.py`, qui fait appel à un package `src`.
Ce package contient plusieurs modules contenant chacun une classe utile pour le jeu. Les classes utilisées sont les suivantes:
- `maze` permettant la création et la gestion du labyrinthe dans une fenêtre.
- `character` utilisée pour la création de personnages (le gardien et MacGyver). Elle permet aussi de gérer le déplacement de celui-ci ainsi que le ramassage des objets.
- `item` servant à la génération d'objets. Une méthode de la classe permet de placer aléatoirement les objets dans le labyrinthe.
- `panel` qui est une classe "annexe" permettant l'affichage et la gestion du panneau situé à droite de la fenêtre de jeu (objets ramassés, message de victoire / défaite et menu de fin)

Ces classes sont accompagnées d'un module de configuration du labyrinthe, `maze_config`. Ce module met à disposition des constantes (dimensions des cellules du labyrinthe, dimensions du labyrinte, vitesse de déplacement, etc.)

Le fichier permettant de créer la structure du labyrinthe est stocké dans un répertoire `maps/` à la racine du projet. Ce fichier est nommé `level_1-1.txt`.

Pour finir, les images utilisées au cours du jeu (textures du labyrinthe, personnages, objets) sont elles stockées dans le répertoire `ressources/`.

Au final, l'arborescence du jeu ressemble à ceci:
- main.py
- maps/
    - level_1-1.txt
- ressources/
    - ...
- src/
    - maze_config.py
    - maze.py
    - item.py
    - character.py
    - panel.py

# Déroulement du programme
## Phase d'initialisation
Suite à l'exécution de `main.py`, les actions suivantes vont se dérouler :

1. Initialisation de la bibliothèque `pygame` essentielle à la création de l'affichage du jeu et la gestion des événements utilisateurs.
2. Génération et affichage du labyrinthe en se basant sur le fichier **.txt** préalablement écrit.
3. Affichage du panneau d'affichage sur la droite du labyrinthe
4. Création et placement des personnages à leurs places respectives (le gardien à la sortie et MacGyver au départ).
5. Ensuite des objets sont générés et placés dans le labyrinthe. Le placement se fait aléatoirement grâce à l'utilisation du module `random` fourni avec Python.


## Phase de mouvement
Une fois ces premières étapes effectuées, le programme va surveiller et "capturer" les événements créés par la ou le joueu·r·se.
- Lorsqu'elle ou il appuie sur `ESC` ou la croix de fermeture de la fenêtre, le jeu se ferme.
- Lorsqu'elle ou il utilise les flêches directionnelles de son clavier, la mise en mouvement de MacGyver s'enclenchera.

Les phases de mouvement enclenchent un certain nombre d'instructions :
1. On efface MacGyver de son ancienne position
2. On calcul la nouvelle position du héros dans le labyrinthe et on s'assure qu'il est autorisé à se déplacer dans cette direction (que ce ne soit pas un mur par exemple).
3. Sur la nouvelle position du personnage, on vérifie si un objet se trouve dans la cellule. Si il y en a un, on l'ajoute dans la besace du héros.
4. On affiche MacGyver à sa nouvelle position
