class AttributeNotFoundError(Exception):
    def __init__(self, name=None):
        msg = f'Attribute "{name}" not found' if name else "Attribute not found."
        super().__init__(msg)


class IdeaListNotFoundError(Exception):
    pass
