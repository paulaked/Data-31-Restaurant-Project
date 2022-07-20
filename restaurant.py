class Table:
    def __init__(self, number_of_people):
        self.bill = []
        self.number_of_people = number_of_people

    def order(self, item, price, quantity=1):
        if item not in self.bill:
            ordered_items = {"item": item, "price": price, "quantity": quantity}
            self.bill.append(ordered_items)
        else:
            for i in self.bill:
                if i.items() == item:
                    i.keys(quantity) + 1
        return self.bill

    def remove(self, item, price, quantity):
        for key in self.bill:
            if key ["item"] == item and key ["price"] == price and quantity <key ["quantity"]:
                key ["quantity"] -= quantity
            elif key["item"] == item and key["price"] == price and quantity >= key ["quantity"]:
                self.bill.remove(key)
            else:
                return False


    def get_subtotal(self):
        pass

    def get_total(self):
        pass

    def split_bill(self):
        pass
