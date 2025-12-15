# Silent Steps

**Silent Steps** is a Python text-based adventure game where you navigate through different rooms of a hospital to complete stealth missions and attempt to escape. You’ll interact with characters, collect items, and avoid a threatening scientist.

## Description

In this game, you play as a character who must progress through multiple rooms, talk to NPCs **Michael** and **Daisy**, collect key items, and avoid being detected by a scientist.  
The entire game is played in the command line using simple text commands.

## Main Features

- Exploration of multiple rooms  
- Interaction with non-player characters (NPCs)  
- Inventory management (pick up and use items)  
- Dialogue and trading system with NPCs  
- Win and loss conditions based on player actions  
- Modular architecture with classes for characters, items, commands, rooms, etc.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/wilfried-lafaye/silent-steps.git
   cd silent-steps
2. Install dependencies (if required by the project):

3. pip install -r requirements.txt

Usage
Run the game by executing the main script:

python game.py

Use the following text commands in the game:
- `go <direction>`: move to an adjacent room (e.g., `go north`)
- `take <item>`: pick up an item in the room
- `talk <character>`: talk to a character
- `inventory`: display the items you are carrying
- `help`: display the list of available commands

## Project Structure

- `game.py`: main script that launches and controls the game
- `player.py`: manages the player and their state
- `character.py`: classes for characters and NPCs
- `room.py`: definition of rooms and management of connections
- `item.py`: management of items in rooms and inventory
- `command.py`: parsing and execution of user commands
- `actions.py`: available actions in the game

## Contributions

Contributions are welcome! Feel free to open an issue or a pull request to propose improvements, fixes, or new features.

## License

This project is licensed under the MIT license. See the `LICENSE` file for more details.
