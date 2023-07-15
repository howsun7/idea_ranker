from typing import Callable


class AttributeType:
    def __init__(self, name: str, scoring_function: Callable = None):
        self.name = name
        if scoring_function is None:
            scoring_function = lambda x: x
        self.scoring_function = scoring_function

class ScaleAttributeType(AttributeType):
    def __init__(self, scoring_function: Callable = None):
        super().__init__('scaled', scoring_function)
                
class BooleanAttributeType(AttributeType):
    def __init__(self, scoring_function: Callable = None):
        self.name = 'boolean'
        if scoring_function is None:
            # True gets a score of 5 while False gets 1 
            scoring_function = lambda x: 5 if x else 1 
        self.scoring_function = scoring_function

class Attribute:
    def __init__(self, name, attribute_type: AttributeType, weight: float = None):
        self.name = name        
        self.attribute_type = attribute_type
        self.weight = weight

    def __str__(self):
        return self.name