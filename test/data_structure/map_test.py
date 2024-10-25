from unittest import TestCase
from data_structure.map import Map

class TestMap(TestCase):
    def setUp(self):
        self.map = Map()
    def test_empty_map(self):
        self.assertTrue(self.map.is_empty())
        self.map.put("key1",1)
        self.assertFalse(self.map.is_empty())
        self.map.remove("key1")
        self.assertTrue(self.map.is_empty())
    def test_put_key_and_add_value(self):
        self.map.put('key1', 1)
        self.map.put('key2', 2)
        self.assertEqual(self.map.get('key1'), 1)
        self.assertEqual(self.map.get('key2'), 2)

    def test_update(self):
        self.map.put('key1', 1)
        self.map.put('key2', 2)
        self.map.update('key2', 3)
        self.assertEqual(self.map.get('key2'), 3)

    def test_remove(self):
        self.map.put('key1', 1)
        self.map.remove('key1')
        self.assertIsNone(self.map.get('key1'))
    def test_(self):
        self.map.put('key1', 1)
        self.map.put('key2', 2)
        self.map.clear()
        self.assertEqual(self.map.size(),0)

    def test_size(self):
        self.map.put('key1', 1)
        self.map.put('key2', 2)
        self.assertEqual(self.map.size(), 2)

    def test_putting_existing_key(self):
        self.map.put('key1', 1)
        with self.assertRaises(KeyError):
            self.map.put('key1', 2)

    def test_putting_non_existing_key(self):
        with self.assertRaises(KeyError):
            self.map.update('key1', 3)

    def test_removing_nonexisting_key(self):
        with self.assertRaises(KeyError):
            self.map.remove('key1')

