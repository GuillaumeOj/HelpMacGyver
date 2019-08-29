# Help McGyver what is it ?
The aim is to help McGyver to escape from a maze. The exit is kept by an evil bodyguard.
To neutralize the guard, the player must pick up some items in the maze.
If MacGyver meet the guardian without those items, he dies. Else, he completes the level.
For moving MacGyver in the maze, the player use the arrows on her/his keyboard.

This game is a project from OpenClassrooms: https://openclassrooms.com/fr/projects/156/assignment

# ToDo list
## Maze
- [x] Create a first level in a ".txt" file
- [] Create a **Maze** class
- [] Read a level file
- [] Create three maze textures (wall, floor and start/end)
- [] Generate the maze based on the level

## Characters
- [] Create a **Character** class (usable for McGyver or the guardian)
- [] Create the guardian
- [] Place the guardian at the maze's exit
- [] Create McGyver
- [] Place McGyver at the maze's sart
- [] Move McGyver with the keyboard's arrows
- [] Collide McGyver with the maze's walls
- [] McGyver win if he found the exit
- [] McGyver pick up the items (see "Items" below)
- [] McGyver wins only if he goes to the exit with all items, else he dies.

## Items
- [] Create an **Item** class
- [] Generate three items (needle, plastic tube and ether)
- [] Place randomly the items in the maze
- [] Erase an item when McGyver pick it up
- [] List all items picked up by McGyver on the window's right side