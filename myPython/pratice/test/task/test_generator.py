from unittest import TestCase
from task.generator import Generator
class TestGenerator(TestCase):
    def test_generator(self):
       self.assertEqual(Generator.gen("34,67,55,33,12,98"),"['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')")
