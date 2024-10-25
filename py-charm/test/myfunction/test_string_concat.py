from unittest import TestCase

from myfunction.string_concat import string_concat,string_addition,string_manipulation,character_count,character_clean




class TestStringConcat(TestCase):
    def test_concat(self):
        self.assertEqual("xycabz",string_concat("abc","xyz"))


    def test_string_addition(self):
        self.assertEqual("joyce",string_addition("joy","ce"))
    def test_string_addition2(self):
        self.assertEqual("helceloo",string_addition("helloo","ce"))
    def test_string_manipulation(self):
        self.assertEqual("Oby",string_manipulation("bOy"))
        self.assertEqual("MKDil",string_manipulation("MiKDl"))
    def test_string_character_count(self):
        self.assertEqual(("o",2),character_count("semicolon","o"))
        self.assertEqual(("e",1),character_count("semicolon","e"))
    def test_string_charater_clean(self):
        self.assertEqual("hello",character_clean("he,ll.o"))
        self.assertEqual("make",character_clean("ma,,,,k...e"))