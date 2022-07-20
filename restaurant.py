class Table:
    def __init__(self, tablenumber):
        self.tablenumber = tablenumber
        self.bill = []

    def order(self, item:str, price, quantity=1):

        if item not in self.bill:
            cheque = {"item": item, "price": price, "quantity": quantity}
            self.bill.append(cheque)
        else:
            for food in self.bill:
                if food.items() == item:
                    food.keys(quantity) + 1
        return self.bill

    def remove(self, item, price, quantity):
        quantity = quantity - self.bill[quantity]

        if quantity == 0:
            return False
        if quantity >= 1:
            return True

    def get_subtotal(self):
        cost_of_meal = self.orderprice * self.orderquantity
        return cost_of_meal

    def get_total(self):
        pass

    def split_bill(self):
        pass
