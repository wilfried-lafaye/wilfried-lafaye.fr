"""
The actions module contains the functions that are called when a command is executed in the game.

Each function in the Actions class takes 3 parameters:
- game: the game object
- list_of_words: the list of words in the command
- number_of_parameters: the number of parameters expected by the command

The functions return True if the command was executed successfully, False otherwise.
The functions print an error message if the number of parameters is incorrect.
"""
import random
#Error messages
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions():
    """
    A class containing all the action methods that can be executed in the game.

    Each method corresponds to a specific command in the game and handles the logic
    for that command.

    Attributes:
        None

    Methods:
        go(game, list_of_words, number_of_parameters)
        quit(game, list_of_words, number_of_parameters)
        help(game, list_of_words, number_of_parameters)
        history(game, list_of_words, number_of_parameters)
        back(game, list_of_words, number_of_parameters)
        check(game, list_of_words, number_of_parameters)
        look(game, list_of_words, number_of_parameters)
        take(game, list_of_words, number_of_parameters)
        drop(game, list_of_words, number_of_parameters)
        talk(game, list_of_words, number_of_parameters)
    """
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        # Get the direction from the list of words.
        direction = list_of_words[1]
        # Move the player in the direction specified by the parameter.
        player.move(direction)
        if player.current_room.name == "Exit" and "number" not in player.inventory:
            print("Micheal didn't let you escape !!!")
            game.finished = True
            return True
        if player.current_room.name == "Exit" and "number" in player.inventory:
            print("You have escape the laboratory ! Congratulations !")
            print("Thanks for playing !")
            game.finished = True
            return True

        for character in (c for c in game.characters if c.name not in ('Daisy', 'Micheal')):
            rooms_possible = [
                room for room in character.current_room.exits.values()
                if room is not None and (character.name != "Scientist" or room.name != "local")
            ]
            if rooms_possible and random.choice([True, False]):
                next_room = random.choice(rooms_possible)
                if player.current_room in (next_room, character.current_room) and character.name == "Scientist":
                    if not any(item.name == 'coat' for item in player.inventory.values()):
                        print("You have been trapped by the scientist!")
                        game.finished = True
                        return True
                del character.current_room.characters[character.name.lower()]
                character.move(next_room)
                next_room.characters[character.name.lower()] = character
                print(f"{character.name} moved to {next_room.name}.")
        return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nThank you {player.name} for playing 'Silent Steps'. Goodbye.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        # Print the list of available commands.
        print("\nThese are the available commands :")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    def history(game, list_of_words, number_of_parameters):
        """
        Display the player's movement history.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        player = game.player
        player.get_history()
        return True
    def back(game, list_of_words, number_of_parameters):
        """
        Move the player back to the previous room.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        player = game.player
        if not player.history :
            print("\nYou can't go back anymore.\n")
            return False
        player.history.pop()
        if not player.history :
            print("\nYou can't go back anymore.\n")
            return False
        print(player.history[-1].get_long_description())
        print(player.get_history())
        player.current_room = player.history[-1]
        return True
    def check(game, list_of_words, number_of_parameters):
        """
        Check the player's inventory.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        if not game.player.inventory: 
            print("There is nothing in your inventory.") 
            return False 
        player = game.player
        #print(player.get_inventory())
        return player.get_inventory()
    def look(game, list_of_words, number_of_parameters):
        """
        Look at the elements in the current room.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        player = game.player
        if not player.current_room.get_elements_in_room() :
            print("\nThere is nothing in this room.\n")
            return False
        for elements in player.current_room.get_elements_in_room():
            print(elements)
            return True
    def take(game, list_of_words, number_of_parameters):
        """
        Take an item from the current room and add it to the player's inventory.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        player = game.player
        list_items_current_room =  player.current_room.inventory.copy()
        item = list_of_words[1]
        inventory_weight = 0
        for items in player.inventory.values():
            inventory_weight+= items.weight
        for items in list_items_current_room:
            if item == items.name:
                if inventory_weight >= player.max_weight:
                    print("This item is too heavy. Your inventory is full")
                    return False

                player.current_room.inventory.discard(items)
                player.inventory[item] = items
                print(f"{item} had been add to your inventory.")
                return True
        return "This item doesn't exist."
    def drop(game, list_of_words, number_of_parameters):
        """
        Drop an item from the player's inventory into the current room.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        player = game.player
        item = list_of_words[1]
        list_items_player =  player.inventory.copy()

        for items in list_items_player:
            if item == items:
                del player.inventory[items]
                player.current_room.inventory.add(list_items_player[items])
                print(f"{item} had been droped")
                return False
        print("You don't have this item in your inventory.")
        return False
    def talk(game, list_of_words, number_of_parameters):
        """
        Talk to a character in the current room.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        if list_of_words[1].lower() in game.player.current_room.characters:
            print(game.player.current_room.characters[list_of_words[1].lower()].get_msg())
            return True
        print(f"{list_of_words[1]} is not present in this room")
        return False
