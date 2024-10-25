from unittest import TestCase
from tv import Tv



class Test(TestCase):

    def test_television_is_on(self):
        tv = Tv()
        self.assertFalse(tv.turn_on())
    def test_television_is_off(self):
        tv = Tv()
        self.assertTrue(tv.turn_off)
    def test_get_channel(self):
        tv = Tv()
        tv.turn_on()
        self.assertEqual(tv.get_channel(),1)
    def test_get_channel_after_setting_channel(self):
        tv = Tv()
        tv.turn_on()
        tv.set_channel(3)
        self.assertEqual(tv.get_channel(),3)
    def test_set_channel_after_setting_to_the_limit_of_channel(self):
        tv = Tv()
        tv.turn_on()
        self.assertRaises(ValueError, tv.set_channel, 200)
    def test_channel_limit(self):
        tv = Tv()
        tv.turn_on()
        self.assertRaises(ValueError,tv.set_channel,0)
    def test_get_volume(self):
        tv = Tv()
        tv.turn_on()
        self.assertEqual(tv.get_volume(),0)
    def test_set_volume(self):
        tv = Tv()
        tv.turn_on()
        tv.set_volume(2)
        self.assertEqual(tv.get_volume(),2)
    def test_volume_limit_negative_value(self):
        tv = Tv()
        tv.turn_on()
        self.assertRaises(ValueError, tv.set_volume,-1)
    def test_volume_limit_positive(self):
        tv = Tv()
        tv.turn_on()
        self.assertRaises(ValueError, tv.set_volume,12)
    def test_channel_is_up(self):
        tv = Tv()
        tv.turn_on()
        tv.channel_up()
        self.assertEqual(tv.get_channel(),2)
    def test_channel_is_down(self):
        tv = Tv()
        tv.turn_on()
        tv.set_channel(3)
        tv.channel_down()
        self.assertEqual(tv.get_channel(),2)

    def test_volume_up(self):
        tv = Tv()
        tv.turn_on()
        tv.volume_up()
        self.assertEqual(tv.get_volume(),1)

    def test_volume_down(self):
        tv = Tv()
        tv.turn_on()
        tv.set_volume(3)
        tv.volume_down()
        self.assertEqual(tv.get_volume(),2)

    def test_mute_function(self):
        tv = Tv()
        tv.turn_on()
        tv.set_volume(7)
        self.assertEqual(tv.get_volume(),7)
        tv.mute()
        self.assertEqual(tv.get_volume(),0)
        tv.un_mute()
        self.assertEqual(tv.get_volume(),7)


