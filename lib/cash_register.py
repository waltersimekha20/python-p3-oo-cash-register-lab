# Save this code in a file named 'cash_register.py'

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item_price = 0 if len(self.items) == 1 else self.total - (self.total - last_item_price)
            last_item = self.items.pop()
            self.total -= last_item_price
            print(f"Voided last transaction: {last_item} - ${last_item_price:.2f}")
        else:
            print("No transactions to void.")
