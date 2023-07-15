from .errors import AttributeNotFoundError


class IdeaList:
    """
    Class representing a list of ideas.

    Attributes:
        ideas (list): List of Idea objects.
        attributes (dict): Dictionary mapping attribute names to Attribute objects.
                           Format: {attribute_name: attribute_object}
    """

    def __init__(self):
        self.ideas = []
        self.attributes = {}
    
    def add_attribute(self, attribute):
        self.attributes[attribute.name] = attribute
    
    def add_idea(self, idea):
        self.ideas.append(idea)
    
    def get_ideas(self):
        return self.ideas
    
    def get_attribute_value(self, idea, attribute):
        if attribute.name not in idea.attribute_values:
            raise AttributeNotFoundError
        
        return idea.attribute_values[attribute.name]
        
    def rank_ideas(self):
        ranked_ideas = sorted(self.ideas, key=lambda idea: self.calculate_idea_score(idea), reverse=True)
        return ranked_ideas
    
    def calculate_idea_score(self, idea):        
        # if any attribute weight is None, it takes precedence and equal weight is applied.
        equal_weight = any(attribute.weight is None for attribute in self.attributes.values())
        score = 0

        for attribute_name, attribute in self.attributes.items():                 
            attribute_score = idea.get_attribute_score(attribute_name)

            if equal_weight:
                score += attribute_score * len(self.attributes)
            else:
                score += attribute_score * attribute.weight
            
        return score
    
    def display_ideas(self):
        import pandas as pd 
        data = []
        attribute_names = list(self.attributes.values())

        for idea in self.ideas:
            attribute_values = [idea.name]
            for attribute_name in attribute_names:
                attribute_value = self.get_attribute_value(idea, attribute_name)
                attribute_values.append(attribute_value)
            data.append(attribute_values)

        df = pd.DataFrame(data, columns=['Idea'] + attribute_names)
        print(df)
    

