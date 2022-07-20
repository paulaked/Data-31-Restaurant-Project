class Table:
    def __init__(self, tablenumber):
        self.tablenumber = tablenumber
        self.bill = []

    def order(self, item: str, price, quantity=1):

        if item not in self.bill:  # checking if the item is already on the bill
            cheque = {"item": item, "price": price, "quantity": quantity}
            self.bill.append(cheque)
        else:  # if it is, then adding the quantity
            for food in self.bill:
                if food.items() == item:
                    food.keys(quantity) + 1
        return self.bill

    def remove(self, item, price, quantity):
        for key in self.bill: # Checking if the quantity is less than that on the bill
            if key["item"] == item and key["price"] == price and quantity < key["quantity"]:
                key["quantity"] -= quantity
            elif key["item"] == item and key["price"] == price and quantity >= key["quantity"]:
                self.bill.remove(key)
            else:
                return False

    def get_subtotal(self):
        price = self.bill["price"]
        quantity = self.bill["quantity"]
        cost_of_meal = price * quantity
        return cost_of_meal

    def get_total(self):
        pass

    def split_bill(self):
        pass
