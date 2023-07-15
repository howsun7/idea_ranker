import unittest
from src.attribute import Attribute, BooleanAttributeType, ScaleAttributeType
from src.idea_list import IdeaList


class IdeaListTests(unittest.TestCase):
    def setUp(self):
        self.idea_list = IdeaList()

    def test_adding_attributes(self):
        attr1 = Attribute("creativity", ScaleAttributeType())
        attr2 = Attribute("feasibility", BooleanAttributeType())
        self.idea_list.add_attribute(attr1)
        self.idea_list.add_attribute(attr2)
        
        self.assertEqual(self.idea_list.attributes, {"creativity": attr1, "feasibility": attr2})
