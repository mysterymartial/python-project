from unittest import TestCase

from data_structure.queue import Queue
class TestQueue(TestCase):
    def setUp(self):
        self.queue = Queue()
    def test_queue_is_empty(self):
        self.assertTrue(self.queue.is_empty())
    def test_queue_size(self):
        self.assertEqual(self.queue.get_size(), 0)
    def test_enqueue_functionality(self):
        intial_size = self.queue.get_size()
        self.queue.enequeue(5)
        self.assertEqual(self.queue.get_size(), intial_size + 1)
    def test_dequeue_functionality(self):
        self.queue.enequeue(5)
        self.queue.enequeue(4)
        dequeued = self.queue.dequeue()
        self.assertEqual(dequeued, 5)
        self.assertEqual(self.queue.get_size(), 1)
    def test_enqueue_from_empty_queue(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()
    def test_peek_functionality(self):
        self.queue.enequeue(5)
        self.queue.enequeue(4)
        self.assertEqual(self.queue.peek(), 5)

    def test_increase_capacity_functionality(self):
        self.small_queue = Queue(1)
        self.small_queue.enequeue(5)
        self.small_queue.enequeue(4)
        self.assertEqual(self.small_queue.get_size(), 2)
        self.assertEqual(self.small_queue.peek(), 5)
        self.assertTrue(self.small_queue.get_capacity() >1)
