
from unittest import TestCase
from bike.bike import Bike

class TestBike(TestCase):
    def setUp(self):
        self.bike = Bike()

    def test_bike_is_turned_on(self):
        self.bike.turned_on()
        self.assertTrue(self.bike.bike_state())

    def test_bike_is_turned_off(self):
        self.bike.turned_off()
        self.assertFalse(self.bike.bike_state())

    def test_accelerate_at_first_gear(self):
        self.bike.turned_on()
        for _ in range(20):
            self.bike.accelerate()
        self.assertEqual(20, self.bike.get_speed())
        self.assertEqual(1, self.bike.update_gear())

    def test_accelerate_to_second_gear(self):
        self.bike.turned_on()
        for _ in range(21):
            self.bike.accelerate()
        self.assertEqual(21, self.bike.get_speed())
        self.assertEqual(2, self.bike.update_gear())

    def test_accelerate_to_third_gear(self):
        self.bike.turned_on()
        for _ in range(31):
            self.bike.accelerate()
        self.assertEqual(31, self.bike.get_speed())
        self.assertEqual(3, self.bike.update_gear())

    #def test_accelerate_at_gear_3(self):
        #self.bike.turned_on()
        #for _ in range(35):
            #self.bike.accelerate()
        #self.assertEqual(35, self.bike.get_speed())
        #self.assertEqual(3, self.bike.update_gear())

    def test_accelerate_to_fourth_gear(self):
        self.bike.turned_on()
        for _ in range(45):
            self.bike.accelerate()
        self.assertEqual(41, self.bike.get_speed())
        self.assertEqual(4, self.bike.update_gear())

    def test_decelerate(self):
        self.bike.turned_on()
        for _ in range(20):
            self.bike.accelerate()
        self.bike.decelerate()
        self.assertEqual(19, self.bike.get_speed())
        self.assertEqual(1, self.bike.update_gear())

    def test_accelerate_when_the_bike_is_off(self):
        with self.assertRaises(ValueError):
            self.bike.accelerate()

    def test_decelerate_when_the_bike_is_off(self):
        with self.assertRaises(ValueError):
            self.bike.decelerate()
