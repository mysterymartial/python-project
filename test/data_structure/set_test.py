from unittest import TestCase
from data_structure.set import Set
class SetTest(TestCase):
    def setUp(self):
        self.set = Set()
    def test_that_the_set_is_empty(self):
        self.assertTrue(self.set.is_empty())
        self.set.add("element1")
        self.assertFalse(self.set.is_empty())
        self.set.remove("element1")
        self.assertTrue(self.set.is_empty())
    def test_add_element_to_set(self):
        self.set.add("element1")
        self.assertTrue(self.set.contains("element1"))
    def test_remove_element_from_set(self):
        self.set.add("element1")
        self.set.add("element2")
        self.set.remove("element1")
        self.assertFalse(self.set.contains("element1"))
    def test_add_duplicate_raises(self):
        self.set.add("element1")
        with self.assertRaises(ValueError):
            self.set.add("element1")
    def test_remove_non_existing_element_raises(self):
        with self.assertRaises(ValueError):
            self.set.remove("element1")
    def test_clear_set(self):
        self.set.add("element1")
        self.set.add("element2")
        self.set.clear()
        self.assertTrue(self.set.is_empty())
    def test_size_of_set(self):
        self.set.add("element1")
        self.set.add("element2")
        self.set.add("element3")
        self.assertEqual(self.set.size(),3)


