"""
This module contains the Room class, 
which represents a room in a text-based adventure game.

The Room class provides functionality for managing room properties,
exits, inventory, and characters.

Example:
    >>> from room import Room
    >>> forest = Room("Forest", "You are in an enchanted forest. 
    You hear a gentle breeze through the treetops.")
    >>> print(forest.name)
    Forest
    >>> print(forest.get_long_description())
    You're in You are in an enchanted forest. You hear a gentle breeze through the treetops.

    Exits:
    """
class Room:
    """
    This class represents a room. A room is composed of a name, 
    a description, and a dictionary which represents all of the connected rooms.

    Attributes:
        name (str): The name of the room.
        description (str): The description of the room.
        exits (dict): All the connected rooms.
        inventory (set): Items present in the room.
        characters (dict): Characters present in the room.

    Methods:
        __init__(self, name, description): The constructor.
        get_exit(self, direction): Get the room in a specific direction.
        get_exit_string(self): Get a string describing the room's exits.
        get_long_description(self): Get a long description of the room.
        get_elements_in_room(self): Get all elements (items and characters) in the room.
    """
    def __init__(self, name, description):
        """
        Initialize a new Room instance.

        Args:
            name (str): The name of the room.
            description (str): The description of the room.
        """
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = set()
        self.characters = {}
    # Define the get_exit method.
    def get_exit(self, direction):
        """
        Get the room in the given direction if it exists.

        Args:
            direction (str): The direction to check for an exit.

        Returns:
            Room or None: The room in the given direction, or None if no exit exists.
        """
        # Return the room in the given direction if it exists.
        if direction in self.exits:
            return self.exits[direction]
        return None
    def get_exit_string(self):
        """
        Return a string describing the room's exits.

        Returns:
            str: A string listing all available exits.
        """
        exit_string = "Exits: "
        for exits in self.exits:
            if self.exits.get(exits) is not None:
                exit_string += exits + ", "
        exit_string = exit_string.strip(", ")
        return exit_string
    # Return a long description of this room including exits.
    def get_long_description(self):
        """
        Return a long description of this room including exits.

        Returns:
            str: A detailed description of the room and its exits.
        """
        return f"\nYou're in {self.description}\n\n{self.get_exit_string()}\n"
    def get_elements_in_room(self):
        """
        Return all elements (items and characters) present in the room.

        Returns:
            set: A set containing all items and characters in the room.
        """
        elements = self.inventory.copy()
        for character in self.characters.values():
            elements.add(character)
        return elements
