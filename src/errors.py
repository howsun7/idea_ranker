class AttributeNotFoundError(Exception):
    def __init__(self, name):
        super().__init__(f'Attribute "{name}" not found')

class IdeaListNotFoundError(Exception):
    pass