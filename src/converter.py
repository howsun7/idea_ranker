class IdeaListConverter:
    def __init__(self, idea_list):
        self.idea_list = idea_list

    def convert_ideas_to_data(self):
        data = []
        for idea in self.idea_list.get_ideas():
            data.append(self.convert_idea_to_data(idea))
        return data

    def convert_idea_to_data(self, idea):
        return {"name": idea.name, "attribute_values": idea.attribute_values}
