# Help McGyver what is it ?
The aim is to help McGyver to escape from a maze. The exit is kept by an evil bodyguard.
To neutralize the guard, the player must pick up some items in the maze.
If MacGyver meet the guardian without those items, he dies. Else, he completes the level.
For moving MacGyver in the maze, the player use the arrows on her/his keyboard.

This game is a project from OpenClassrooms: https://openclassrooms.com/fr/projects/156/assignment

# How it works ?
It's the simple game you can play.
You run **main.py** and use your arrows key to move Macgyver.
You have to pick all items before reaching the maze's exit, otherwise you will die.

# How to insall it ?
1. Clone this repository on your computer. Run :
```
git clone git@github.com:GuillaumeOj/HelpMacGyver.git
or
git clone https://github.com/GuillaumeOj/HelpMacGyver.git
```
2. Create a virtual environement in your directory:
```
virtualenv -p python3 env
```
or for PowerShell:
```powershell
virtualenv -p $env:python3 env
```
3. Activate your virtual environement:
```
source env/bin/activate
```
or for PowerShell:
```powershell
.env/scripts/activate.ps1
```
4. Install `requirements.txt`:
```
pip install -r requirements.txt
```
5. Run `main.py`:
```
python main.py
```
6. Enjoy the game !

# ToDo list
## Maze
- [x] Create a first level in a ".txt" file
- [x] Create a **Maze** class
- [x] Read a level file
- [x] Create four maze textures (wall, floor, start and end)
- [x] Generate the maze based on the level
- [x] Add 'erase' method when Macgyver move or when an item is picked up

## Characters
- [x] Create a **Character** class (usable for McGyver or the guardian)
- [x] Create the guardian
- [x] Place the guardian at the maze's end
- [x] Create McGyver
- [x] Place McGyver at the maze's start
- [x] Move McGyver with the keyboard's arrows
- [x] Collide McGyver with the maze's walls
- [x] McGyver win if he found the end
- [x] McGyver picks up the items (see "Items" below)
- [x] McGyver wins only if he goes to the exit with all items, else he dies.

## Items
- [x] Create an **Item** class
- [x] Generate three items (needle, plastic tube and ether)
- [x] Place randomly the items in the maze
- [x] List all items picked up by McGyver on the window's right side

## Panel
- [x] Create a **Panel** class
- [x] Generate a background for the panel
- [x] Create area for the items picked up by Mc Gyver

### End menu
- [x] Create a **end_menu** in **Panel**
- [x] Show this "menu" when the player win or lose and stop the game
- [x] Generate two buttons (Yes / No)
- [x] Stop the game if the player choose 'End'
- [x] Restart the game if the player choose 'Continue'
