# Define the Player class.
"""
This module contains the Player class, which represents a player in a game.
"""
class Player():
    """
    This class represents a player. A player is composed of a name and a current room.

    Attributes:
        name (str): The name of the player.
        current_room (str): The room where the player is.

    Methods:
        __init__(self, name) : The constructor.
        move(self, direction) : This function changes the current room of the player
    """
    # Define the constructor.
    def __init__(self, name):
        """
        Initialize a new Player instance.

        Args:
            name (str): The name of the player.
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {}
        self.max_weight = 4
        """
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {}
        self.max_weight = 4
    # Define the move method.
    def move(self, direction):
        """
        Change the current room of the player based on the given direction.

        Args:
            direction (str): The direction to move 
            (n, north, s, south, e, east, w, west, u, up, d, down).

        Returns:
            bool: True if the move was successful, False otherwise.
            """
        # Get the next room from the exits dictionary of the current room.
        if direction.lower() in {"n", "north", "s", "south", "e", "east","w" , "west", "u", "up", "d", "down"} :
            if self.current_room.exits[direction[0].upper()] is not None :
                if self.current_room.exits[direction[0].upper()].name == "ElevatorDOWN" and "card" not in self.inventory :
                    print("You can't use the elevator without the card !!!")
                    return True
                next_room = self.current_room.exits[direction[0].upper()]
                self.history.append(self.current_room)
                self.current_room = next_room
                print(self.current_room.get_long_description())
                print(self.get_history())
                return True
        print("You can't go in that direction.")
        return False
        # Set the current room to the next room and save this room on the history.
        print("This direction doesn't exist.") 
        return False

    def get_history(self):
        """
        Get a string representation of the rooms the player has visited.

        Returns:
            str: A string listing the descriptions of visited rooms.
        """
        print("You've already been in these rooms :\n")
        for room in self.history:
            print(f"- {room.description}")
        return ""

    def get_inventory(self):
        """
        Get a string representation of the player's inventory.

        Returns:
            str: A string listing the items in the player's inventory or a message if it's empty.
        """
        if not self.inventory : 
            return "\nYou're inventory is empty.\n"
        print("These are your items :")
        for items in self.inventory.values() :
            print(f"- {items}")

    