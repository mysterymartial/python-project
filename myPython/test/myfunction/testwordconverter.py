from unittest import TestCase
from myfunction.wordconverter import word_converter,word_convert

class TestWordConverter(TestCase):
    def test_word_converter(self):
        self.assertEqual({"a":1,"w":1,"e":1},word_converter("awe"))
    def test_for_capital_letters_edge_case(self):
        self.assertEqual({"a":1,"w":1,"e":1},word_converter("AWE"))
    def test_word_convert(self):
        self.assertEqual({"h":2,"a":2, "n":2},word_convert("hannah"))
        self.assertEqual({"h":2,"a":2, "n":2},word_convert("HANNAh"))