class Table:
    def __init__(self, tablenumber):
        self.tablenumber = tablenumber
        self.bill = []

    def order(self, item, price, quantity=1):
        item = item
        price = price
        quantity = quantity

        return self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price, quantity):
        price = price
        quantity = quantity - self.order(quantity)

        if quantity == 0:
            return False
        if quantity >= 1:
            return True

    def get_subtotal(self,):
        pass

    def get_total(self):
        pass

    def split_bill(self):
        pass
