import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.instance_of_Drink = Drink("Whiskey", 5.00)

    def test_drink_has_name(self):
        self.assertEqual("Whiskey", self.instance_of_Drink.name)

    def test_drink_has_price(self):
        self.assertEqual(5.00, self.instance_of_Drink.price)