"""
This module defines the Item class to represent objects with a name, description, and weight.
"""
class Item():
    """
    Represents an object with a name, description, and weight.

    Attributes:
        name (str): The name of the item.
        description (str): A brief description of the item.
        weight (float): The weight of the item in kilograms.
    """
    def __init__(self, name, description, weight):
        """
        Initializes a new Item object.

        Args:
            name (str): The name of the item.
            description (str): A brief description of the item.
            weight (float): The weight of the item in kilograms.
        """
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        """
        Returns a string representation of the item.

        Returns:
            str: A string representing the item with its name, description, and weight.
        """
        return  f"{self.name} : {self.description} ({self.weight}kg)"
