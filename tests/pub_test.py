import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.instance_of_Pub = Pub("The Drinking Scot", 500.00)
        self.instance_of_Drink = Drink("Whiskey", 5.00)
        # self.instance_of_Customer = Customer("Billy", 21, 20.00)

    def test_pub_has_name(self):
        self.assertEqual("The Drinking Scot", self.instance_of_Pub.name)

    def test_pub_has_till(self):
        self.assertEqual(500.00, self.instance_of_Pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual(0, self.instance_of_Pub.drinks_list_length())

    def test_can_add_drink_to_drinks_list(self):
        self.instance_of_Pub.add_to_drinks_list(self.instance_of_Drink)
        self.assertEqual(1, self.instance_of_Pub.drinks_list_length())

    def test_pub_sells_item_to_customer(self):
        self.instance_of_Pub.sell_to_customer(self.instance_of_Drink.price)
        self.assertEqual(505.00, self.instance_of_Pub.till)
    
    def test_pub_checks_customer_age(self):
        self.instance_of_Customer = Customer("Billy", 21, 20.00)
        
        is_of_age = self.instance_of_Pub.pub_checks_age(self.instance_of_Customer)
        self.assertEqual(True, is_of_age)

