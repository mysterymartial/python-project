from unittest import TestCase
from data_structure.array_list import ArrayList
class TestArrayList(TestCase):
    def setUp(self):
        self.list = ArrayList(3)
    def test_array_list_is_empty(self):
        self.assertTrue(self.list.is_empty())
    def test_get_size(self):
        self.assertEqual(self.list.get_size(),0)
    def test_add_item(self):
        self.list.add(3)
        self.list.add(4)
        self.list.add(5)
        self.assertEqual(self.list.get_size(),3)
    def test_remove_item(self):
        self.list.add(3)
        self.list.add(4)
        self.list.add(5)
        self.list.remove(4)
        self.assertEqual(self.list.get_size(),2)
    def test_remove_non_existing_element(self):
        with self.assertRaises(IndexError):
            self.list.remove(5)
    def test_insert_item_functionality(self):
        self.list.insert(0,4)
        self.assertEqual(self.list.get_size(),1)
    def test_insert_invalid_index_functionality(self):
        with self.assertRaises(IndexError):
            self.list.insert(-5,4)
    def test_dynamic_capacity(self):
        self.small_list = ArrayList(1)
        self.small_list.add(3)
        self.small_list.add(4)
        self.small_list.add(5)
        self.assertTrue(self.small_list.get_capacity() > 1)
        self.assertEqual(self.small_list.get_size(),3)
    def test_get_element_by_index(self):
        self.list.add(5)
        self.list.add(6)
        self.list.add(7)
        element = self.list.get(0)
        self.assertEqual(element,5)
    def test_to_clear_array_list(self):
        self.list.add(5)
        self.list.add(6)
        self.list.add(7)
        self.list.clear()
        self.assertEqual(self.list.get_size(),0)

