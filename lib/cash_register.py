#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        self._discount = discount
        self.items = []
        self.total = 0
        self._void_last_transaction = False
    
    def add_item(self, item, price, quantity=1):
        self.total += price*quantity
        self.last_item_price = price * quantity
        for i in range(quantity):
            self.items.append(item)
    
    @property
    def discount(self):
        return self._discount
    
    @discount.setter
    def discount(self, discount):
        if (discount != 0):
            self._discount = discount

    def apply_discount(self):
        if self.discount != 0:
            new_total = self.total - self.total * self._discount/100
            self.total = int(new_total)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        self.items.pop()
        if (len(self.items) == 0):
            self.total = 0.0
        else:
            self.total -= self.last_item_price