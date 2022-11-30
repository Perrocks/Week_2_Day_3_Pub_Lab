class Customer:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet

    def add_to_drinks_to_customer(self, drink_to_add):
        self.drink_in_hand.append(drink_to_add)

    def remove_from_wallet(self, amount):
        self.wallet -= amount