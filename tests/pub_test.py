import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):

    def setUp(self):
        self.instance_of_Pub = Pub("The Drinking Scot", 500.00)

    def test_pub_has_name(self):
        self.assertEqual("The Drinking Scot", self.instance_of_Pub.name)

    def test_pub_has_till(self):
        self.assertEqual(500.00, self.instance_of_Pub.till)

    