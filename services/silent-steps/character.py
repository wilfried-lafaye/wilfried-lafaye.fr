"""
This module defines the Character class for a text-based adventure game.

The Character class represents a character in the game, 
with attributes such as name, description, current room, and messages.
"""
class Character():
    """
    A class representing a character in a text-based adventure game.

    Attributes:
        name (str): The name of the character.
        description (str): A brief description of the character.
        current_room (str): The name of the room the character is currently in.
        msgs (list): A list of messages the character can say.
    """
    # Constructor
    def __init__(self, name, description, current_room, msgs):
        """
        Initialize a new Character instance.

        Args:
            name (str): The name of the character.
            description (str): A brief description of the character.
            current_room (str): The name of the room the character starts in.
            msgs (list): A list of messages the character can say.
        """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs

    def __str__(self):
        """
        Return a string representation of the Character.

        Returns:
            str: A string containing the character's name and description.
        """
        return  f"{self.name} : {self.description}"

    def move(self, next_room):
        """
        Move the character to a new room.

        Args:
            next_room (str): The name of the room to move to.

        Returns:
            bool: Always returns False (this could be used for game logic).
        """
        self.current_room = next_room
        return False

    def get_msg(self):
        """
        Get the next message from the character's message list.

        This method removes the first message from the list and appends it to the end,
        creating a circular list of messages.

        Returns:
            str: The next message in the character's message list.
        """
        msg = self.msgs.pop(0)
        self.msgs.append(msg)
        return msg
