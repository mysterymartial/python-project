from unittest import TestCase
from data_structure.linked_list import Linked_List
from data_structure.node import Node
class TestLinkedList(TestCase):
    def setUp(self):
        self.linked_list = Linked_List()

    def test_insert_at_the_end(self):
        self.linked_list.insert_at_end(5)
        self.linked_list.insert_at_end(6)
        self.linked_list.insert_at_end(7)
        self.assertEqual(self.linked_list.head.data, 5)
        self.assertEqual(self.linked_list.head.next.data, 6)
        self.assertEqual(self.linked_list.head.next.next.data, 7)

    def test_insert_at_the_beginning(self):
        self.linked_list.insert_at_start(20)
        self.linked_list.insert_at_start(30)
        self.assertEqual(self.linked_list.head.data, 30)
        self.assertEqual(self.linked_list.head.next.data, 20)


    def test_is_empty(self):
        self.assertTrue(self.linked_list.is_empty())
        self.linked_list.insert_at_end(5)
        self.assertFalse(self.linked_list.is_empty())

    def test_length(self):
        self.assertEqual(self.linked_list.length(), 0)
        self.linked_list.insert_at_end(5)
        self.assertEqual(self.linked_list.length(),1)
        self.linked_list.insert_at_end(6)
        self.assertEqual(self.linked_list.length(),2)
    def test_display_linked_list(self):
        self.linked_list.insert_at_end(5)
        self.linked_list.insert_at_end(6)
        self.linked_list.insert_at_end(7)
        self.assertEqual(self.linked_list.display(),"5 -> 6 -> 7 -> None")
    def test_delete_contains(self):
        self.linked_list.insert_at_end(5)
        self.linked_list.insert_at_end(6)
        self.assertTrue(self.linked_list.contains(5))
        self.assertFalse(self.linked_list.contains(7))
    def test_search(self):
        self.linked_list.insert_at_end(5)
        self.linked_list.insert_at_end(6)
        self.linked_list.insert_at_end(7)
        found_node = self.linked_list.search(6)
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.data, 6)
        found_node = self.linked_list.search(40)
        self.assertIsNone(found_node)

    def test_reverse(self):
        self.linked_list.insert_at_end(5)
        self.linked_list.insert_at_end(6)
        self.linked_list.insert_at_end(7)
        self.linked_list.reverse()
        self.assertEqual(self.linked_list.head.data, 7)
        self.assertEqual(self.linked_list.head.next.data, 6)
        self.assertEqual(self.linked_list.head.next.next.data, 5)

    def test_clear(self):
        self.linked_list.insert_at_end(5)
        self.linked_list.insert_at_end(6)
        self.linked_list.insert_at_end(7)
        self.assertIsNotNone(self.linked_list.head)
        self.assertEqual(self.linked_list.head.data, 5)
        self.assertEqual(self.linked_list.head.next.data, 6)
        self.assertEqual(self.linked_list.head.next.next.data, 7)

        self.linked_list.clear()
        self.assertIsNone(self.linked_list.head)
        self.assertEqual(self.linked_list.length(),0)

    def test_delete(self):
        self.linked_list.insert_at_end(5)
        self.linked_list.insert_at_end(6)
        self.linked_list.insert_at_end(7)
        self.linked_list.delete(6)
        self.assertEqual(self.linked_list.head.data, 5)
        self.assertEqual(self.linked_list.head.next.data, 7)
        self.assertEqual(self.linked_list.length(), 2)

    def test_insert_at(self):
        self.linked_list.insert_at_index(0, 5)
        self.assertEqual(self.linked_list.head.data, 5)

        self.linked_list.insert_at_index(1, 6)
        self.assertEqual(self.linked_list.head.next.data, 6)

        self.linked_list.insert_at_index(1, 7)
        self.assertEqual(self.linked_list.head.next.data, 7)
        self.assertEqual(self.linked_list.head.next.next.data, 6)


        self.assertEqual(self.linked_list.length(), 3)

        with self.assertRaises(IndexError):
            self.linked_list.insert_at_index(-1, 5)

        with self.assertRaises(IndexError):
            self.linked_list.insert_at_index(5, 30)

    def test_delete_at_index(self):
        self.linked_list.insert_at_end(5)
        self.linked_list.insert_at_end(6)
        self.linked_list.insert_at_end(7)

        self.linked_list.delete_at_index(1)
        self.assertEqual(self.linked_list.head.data, 5)
        self.assertEqual(self.linked_list.head.next.data, 7)

        with self.assertRaises(IndexError):
            self.linked_list.delete_at_index(-1)
        with self.assertRaises(IndexError):
            self.linked_list.delete_at_index(5)

