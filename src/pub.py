class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks_list = []

    def drinks_list_length(self):
        return len(self.drinks_list)

    def add_to_drinks_list(self, drink_to_add):
        self.drinks_list.append(drink_to_add)

    def sell_to_customer(self, amount):
        self.till += amount

    def pub_checks_age(self, customer):
            if customer.age >= 18:
                return True
            else:
                return False
            
        

