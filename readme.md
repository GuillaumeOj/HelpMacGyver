# Help McGyver what is it ?
The aim is to help McGyver to escape from a maze. The exit is kept by an evil bodyguard.
To neutralize the guard, the player must pick up some items in the maze.
If MacGyver meet the guardian without those items, he dies. Else, he completes the level.
For moving MacGyver in the maze, the player use the arrows on her/his keyboard.

This game is a project from OpenClassrooms: https://openclassrooms.com/fr/projects/156/assignment

# ToDo list
## Maze
- [x] Create a first level in a ".txt" file
- [x] Create a **Maze** class
- [x] Read a level file
- [x] Create four maze textures (wall, floor, start and end)
- [x] Generate the maze based on the level

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

### End window
- [ ] Create a **end_window** in **Panel**
- [ ] Show this "window" when the player win or loos (You Win ! / You Loose !)
- [ ] Generate two buttons (Continue / End)