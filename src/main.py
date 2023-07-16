from .attribute import Attribute, BooleanAttributeType, ScaleAttributeType
from .idea import Idea
from .idea_list import IdeaList

if __name__ == "__main__":
    idea_list = IdeaList()
    idea_list.add_attribute(Attribute("creativity", ScaleAttributeType()))
    idea_list.add_attribute(Attribute("feasibility", ScaleAttributeType()))
    idea_list.add_attribute(Attribute("innovative", BooleanAttributeType()))

    idea1 = Idea("Idea 1", idea_list)
    idea1.add_attribute("creativity", 5)
    idea1.add_attribute("feasibility", 4)
    idea1.add_attribute("innovative", True)

    idea2 = Idea("Idea 2", idea_list)
    idea2.add_attribute("creativity", 5)
    idea2.add_attribute("feasibility", 2)
    idea2.add_attribute("innovative", False)

    idea_list.add_idea(idea1)
    idea_list.add_idea(idea2)
