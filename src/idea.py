from typing import Dict, List, Union
from .errors import AttributeNotFoundError, IdeaListNotFoundError
from .idea_list import IdeaList


class Idea:
    """
    Class representing an idea.

    Attributes:
        name (str): The name of the idea.
        idea_list (IdeaList, optional): The IdeaList to which the idea belongs.
        attribute_values (dict): Dictionary mapping Attribute objects to their values.
                                Format: {attribute_name: value}
    """

    def __init__(self, name, idea_list: IdeaList = None):
        self.name = name
        self.idea_list = idea_list
        self.attribute_values = {}
    
    def add_attribute(self, name: str, value: Union[str, List, Dict]):
        # TODO: check if idea list has attribute by name
        self.attribute_values[name] = value
        
    def get_attribute_value(self, attribute_name):
        if attribute_name not in self.attribute_values:
            raise AttributeNotFoundError(attribute_name)
        return self.attribute_values[attribute_name]

    def get_attribute_score(self, attribute_name):
        value = self.get_attribute_value(attribute_name)

        if self.idea_list is None:
            raise IdeaListNotFoundError
        
        attribute = self.idea_list.attributes.get(attribute_name)

        if attribute is None:
            raise AttributeNotFoundError(attribute_name)

        score = attribute.attribute_type.scoring_function(value)

        return score
    
    def __str__(self):
        return self.name


