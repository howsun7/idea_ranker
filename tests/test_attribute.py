import unittest
from src.attribute import Attribute, ScaleAttributeType, BooleanAttributeType


class AttributeTests(unittest.TestCase):
    def test_createing_attribute(self):
        attr = Attribute('testattr', ScaleAttributeType())
        attr2 = Attribute('testattr2', BooleanAttributeType())
        self.assertEqual(attr.name, 'testattr')
        self.assertEqual(attr.weight, None)
        
        self.assertIsInstance(attr.attribute_type, ScaleAttributeType)
        self.assertIsInstance(attr2.attribute_type, BooleanAttributeType)