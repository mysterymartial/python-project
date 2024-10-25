from unittest import TestCase
from data_structure.stack import Stack
class TestStack(TestCase):
    def setUp(self):
        self.stack = Stack(3)

    def test_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_stack_initial_size(self):
        self.assertEqual(self.stack.get_size(), 0)
    def test_push_functionality(self):
        self.assertEqual(self.stack.get_size(), 0)
        self.stack.push(1)
        self.assertEqual(self.stack.get_size(), 1)
    def test_pop_functionality(self):
        self.assertEqual(self.stack.get_size(), 0)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 4)
        self.assertEqual(self.stack.get_size(), 2)
    def test_pop_element_that_is_not_in_existence(self):
        with self.assertRaises(IndexError):
            self.stack.pop()
    def test_peek_return_the_top_element_of_the_stack(self):
        self.stack.push(4)
        self.stack.push(5)
        self.stack.push(6)
        self.assertEqual(self.stack.peek(),6)
        self.assertEqual(self.stack.get_size(), 3)
    def test_increase_capacity_when_full(self):
        small_stack = Stack(2)
        small_stack.push(1)
        small_stack.push(2)
        small_stack.push(3)
        self.assertEqual(small_stack.get_size(), 3)
        self.assertEqual(small_stack.peek(), 3)
        self.assertTrue(small_stack.get_capacity() >2)

