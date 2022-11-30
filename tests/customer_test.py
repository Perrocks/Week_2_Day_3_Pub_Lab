import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.instance_of_Customer = Customer("Billy", 21, 20.00)
        self.instance_of_Drink = Drink("Whiskey", 5.00)

    def test_customer_has_name(self):
        self.assertEqual("Billy", self.instance_of_Customer.name)

    def test_customer_has_age(self):
        self.assertEqual(21, self.instance_of_Customer.age)

    def test_customer_has_wallet(self):
        self.assertEqual(20.00, self.instance_of_Customer.wallet)

    def test_customer_buys_item(self):
        self.instance_of_Customer.remove_from_wallet(self.instance_of_Drink.price)
        self.assertEqual(15.00, self.instance_of_Customer.wallet)
