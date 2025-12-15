"""
This module contains the Game class which represents the main game logic and structure.

The game is a text-based adventure where players navigate through rooms, interact with characters,
and manage inventory items.

Example:
    To start the game:
    
    >>> game = Game()
    >>> game.play()
"""
#Import Modules
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
class Game:
    """
    Represents the main game structure and logic.

    This class manages the game state, including rooms, commands, player, and characters.

    Attributes:
        finished (bool): Indicates if the game has ended.
        rooms (list): List of Room objects in the game.
        commands (dict): Dictionary of available commands.
        player (Player): The player object.
        characters (list): List of Character objects in the game.

    Example:
        >>> game = Game()
        >>> game.setup()
        >>> game.play()
    """
    def __init__(self):
        """
        Initializes a new Game instance.

        Sets up initial game state with empty lists and dictionaries.

        Example:
            >>> game = Game()
            >>> print(game.finished)
            False
        """
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.characters =[]
    def setup(self):
        """
        Sets up the game environment.

        Initializes commands, rooms, player, items, and characters.

        Example:
            >>> game = Game()
            >>> game.setup()
            >>> print(len(game.rooms))
            10
        """
        # Setup commands
        help = Command("help", " : show this help.", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : exit the game.", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : move in a cardinal direction (N, E, S, W)."
                     , Actions.go, 1)
        self.commands["go"] = go
        history = Command("history", " : shows visited rooms.", Actions.history, 0)
        self.commands["history"] = history
        back = Command("back", " : go back in the last room.", Actions.back, 0)
        self.commands["back"] = back
        check = Command("check", " : show the items in your inventory.", Actions.check, 0)
        self.commands["check"] = check
        look = Command("look", " : show the items in the room.", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " : take the chosen item.", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " : drop the chosen item from your inventory.", Actions.drop, 1)
        self.commands["drop"] = drop
        talk = Command("talk", " : talk to a PNJ in the current room.", Actions.talk,1)
        self.commands["talk"] = talk
        # Setup rooms
        bedroom = Room("Bedroom", "your bedroom.")
        self.rooms.append(bedroom)
        local = Room("local", "the local.")
        self.rooms.append(local)
        patient_room = Room("PatientRoom", "another patient room")
        self.rooms.append(patient_room)
        office = Room("office", "scientist's office")
        self.rooms.append(office)
        hall = Room("Hall", "the upstairs hallway.")
        self.rooms.append(hall)
        elevator_up = Room("ElevatorUP", "the elevator on the first floor.")
        self.rooms.append(elevator_up)
        elevator_down = Room("ElevatorDOWN", "the elevator on the ground floor.")
        self.rooms.append(elevator_down)
        hall2 = Room("Hall2", "the groundfloor hallway.")
        self.rooms.append(hall2)
        closet = Room("Closet", "a closet.")
        self.rooms.append(closet)
        exitt = Room("Exit", "the exit.")
        self.rooms.append(exitt)
        # Create exits for rooms
        bedroom.exits = {"N" : local, "E" : hall, "S" : None,
                          "W" : None, "U" : None, "D" : None}
        local.exits = {"N" : None, "E" : patient_room, "S" : bedroom,
                        "W" : None, "U" : None, "D" : None}
        patient_room.exits = {"N" : None, "E" : office, "S" : None,
                               "W" : local, "U" : None, "D" : None}
        office.exits = {"N" : None, "E" : None, "S" : None,
                         "W" : patient_room, "U" : None, "D" : None}
        hall.exits = {"N" : None, "E" : elevator_up, "S" : None,
                       "W" : bedroom, "U" : None, "D" : None}
        elevator_up.exits = {"N" : None, "E" : None, "S" : None,
                              "W" : hall, "U" : None, "D" : elevator_down}
        elevator_down.exits = {"N" : None, "E" : None, "S" : None,
                                "W" : hall2, "U" : elevator_up, "D" : None}
        hall2.exits = {"N" : None, "E" : elevator_down, "S" : closet,
                        "W" : exitt, "U" : None, "D" : None}
        closet.exits = {"N" : hall2, "E" : None, "S" : None,
                         "W" : None, "U" : None, "D" : None}
        exitt.exits = {"N" : None, "E" : None, "S" : None,
                        "W" : None, "U" : None, "D" : None}
        # Setup player and starting room and it
        self.player = Player("Bob")
        self.player.current_room = bedroom
        # Setup items
        local.inventory.add(Item("coat","a coat that allow you to hide from the scientist",2))
        office.inventory.add(Item("card","this card allows you to use the elevator",1))
        office.inventory.add(Item("number", "Daisy's phone number",1))
        patient_room.inventory.add(Item("key", "a mysterious key",2))
        # Setup PNJs
        michael = Character("Micheal",
                            "a cleaning agent, you can corrupt him by giving him Daisy's number."
                            ,hall2, ["let me do my work","oh wait I know you",
                                     "I will let you escape if you give me Daisy's number"] )
        hall2.characters.update({"micheal" : michael})
        self.characters.append(michael)
        scientist = Character("Scientist",
                               "an old man with white hair and an arched back ", office, ["I've never seen you before","You must be new here"])
        office.characters.update({"scientist" : scientist})
        self.characters.append(scientist)
        daisy = Character("Daisy","a 35-year-old laboratory nurse, is a methodical and passionate woman.", bedroom, ["You want to escape from here ?","go to the office to take elevator card and my number"])
        bedroom.characters.update({"daisy" : daisy})
        self.characters.append(daisy)
    # Play the game
    def play(self):
        """
        Starts and runs the main game loop.

        Continues to process player commands until the game is finished.
        """
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            self.process_command(input("> "))

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        """
        Processes a command entered by the player.

        Args:
            command_string (str): The command entered by the player.

        Returns:
            bool: True if the command was recognized and executed, False otherwise.
        """
        # Split the command string into a list of words
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]
        if command_word in "          ":
            return False

        # If the command is not recognized, print an error message
        if command_word.lower() not in self.commands:
            print(f"\nCommand '{command_word}'does not exits. Write 'help' to see all the commands\n")
            return False
        # If the command is recognized, execute it
        command = self.commands[command_word.lower()]
        command.action(self, list_of_words, command.number_of_parameters)
        return True
    # Print the welcome message
    def print_welcome(self):
        """
        Prints the welcome message and initial room description.
        """
        print("The sterile white walls close around you.\n")
        print("You've studied every inch of this facility, mapped every surveillance point.\n")
        print("They think you're just another subject, another experiment.\n")
        print("But today, everything changes.\n")
        print("You will break out. No matter the cost.\n")
        print(self.player.current_room.get_long_description())
def main():
    """
    Main function to start the game.

    Creates a Game instance and starts the game.
    """
    # Create a game object and play the game
    Game().play()
if __name__ == "__main__":
    main()
