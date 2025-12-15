"""
This module contains the Command class, 
which represents a command in a text-based game or application.

The Command class encapsulates the properties and behavior of a command, including its name,
help text, associated action, and the number of parameters it expects.
"""
class Command():
    """
    This class represents a command. 
    A command is composed of a command word, a help string, 
    an action and a number of parameters.

    Attributes:
        command_word (str): The command word.
        help_string (str): The help string.
        action (function): The action to execute when the command is called.
        number_of_parameters (int): The number of parameters expected by the command.

    Methods:
        __init__(self, command_word, help_string, action, number_of_parameters) : The constructor.
        __str__(self) : The string representation of the command.
    """

    # The constructor.
    def __init__(self, command_word, help_string, action, number_of_parameters):
        """
        Initialize a new Command instance.

        Args:
            command_word (str): The word that triggers this command.
            help_string (str): A brief description of what the command does.
            action (function): The function to be called when this command is executed.
            number_of_parameters (int): The number of parameters this command expects.
        """
        self.command_word = command_word
        self.help_string = help_string
        self.action = action
        self.number_of_parameters = number_of_parameters
    # The string representation of the command.
    def __str__(self):
        """
        Return a string representation of the Command.

        Returns:
            str: A string containing the command word and help string.
        """
        return  self.command_word \
                + self.help_string
