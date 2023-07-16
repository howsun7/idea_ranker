import unittest
from src.attribute import Attribute, BooleanAttributeType, ScaleAttributeType
from src.idea_list import IdeaList
from src.idea import Idea


class IdeaListTests(unittest.TestCase):
    def setUp(self):
        self.idea_list = IdeaList()
        attr = Attribute("test attr", ScaleAttributeType())
        attr2 = Attribute("feasibility", BooleanAttributeType())
        self.idea_list.add_attribute(attr)
        self.idea_list.add_attribute(attr2)

    def test_adding_attributes(self):
        idea_list = IdeaList()
        attr1 = Attribute("creativity", ScaleAttributeType())
        attr2 = Attribute("feasibility", BooleanAttributeType())
        idea_list.add_attribute(attr1)
        idea_list.add_attribute(attr2)

        self.assertEqual(
            idea_list.attributes, {"creativity": attr1, "feasibility": attr2}
        )

    def test_adding_idea(self):
        self.assertEqual(len(self.idea_list.ideas), 0)
        self.assertEqual(self.idea_list.ideas, [])

        idea = Idea("test idea", self.idea_list)
        idea.add_attribute("test attr", 5)
        self.idea_list.add_idea(idea)

        self.assertEqual(len(self.idea_list.ideas), 1)
        self.assertEqual(self.idea_list.ideas, [idea])
