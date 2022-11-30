import unittest
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):

    def setUp(self):
        self.instance_of_Pub = Pub("The Drinking Scot", 500.00)
        self.instance_of_Drink = Drink("Whiskey", 5.00)

    def test_pub_has_name(self):
        self.assertEqual("The Drinking Scot", self.instance_of_Pub.name)

    def test_pub_has_till(self):
        self.assertEqual(500.00, self.instance_of_Pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual(0, self.instance_of_Pub.drinks_list_length())

    def test_can_add_drink_to_drinks_list(self):
        self.instance_of_Pub.add_to_drinks_list(self.instance_of_Drink)
        self.assertEqual(1, self.instance_of_Pub.drinks_list_length())
