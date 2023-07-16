import unittest
from src.idea import Idea
from src.idea_list import IdeaList
from src.errors import AttributeNotFoundError


class IdeaTests(unittest.TestCase):
    def test_creating_idea(self):
        idea = Idea("a big idea")
        self.assertEqual(idea.name, "a big idea")
        self.assertEqual(idea.idea_list, None)
        self.assertEqual(idea.attribute_values, {})

        idea_list = IdeaList()
        idea2 = Idea("small idea", idea_list=idea_list)
        self.assertEqual(idea2.idea_list, idea_list)

    def test_adding_attribute_with_value(self):
        idea = Idea("startup idea 1")
        idea.add_attribute("potential", 3)
        self.assertEqual(idea.attribute_values, {"potential": 3})

    def test_adding_attribute_that_does_not_exist_in_idea_list(self):
        idea_list = IdeaList()
        idea = Idea("test idea", idea_list)
        self.assertEqual(idea_list.attributes, {})

        with self.assertRaises(AttributeNotFoundError):
            idea.add_attribute("potential", 3)

    def test_getting_attribute_by_name(self):
        idea = Idea("startup idea")
        idea.add_attribute("impact", 4)
        attr_value = idea.get_attribute_value("impact")
        self.assertEqual(attr_value, 4)

    def test_getting_nonexistent_attribute(self):
        idea = Idea("product 1")
        self.assertEqual(idea.attribute_values, {})
        with self.assertRaises(AttributeNotFoundError):
            idea.get_attribute_value("nonexistent_attribute")
