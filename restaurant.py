class Table:

    def __init__(self, num_of_people):
        self.bill = []
        self.num_of_people = num_of_people


    def order(self, item = "food", price = "10.00", quantity = "1"):
        if item not in self.list:
            ordered = {"item": item, "price": price, "quantity": quantity}
            self.bill.append(ordered)
        else:
            for i in self.bill:
                if i.items() == item:
                    i.keys(quantity) + 1
        return self.bill

    def remove(self):
        pass

    def get_subtotal(self):
        pass

    def get_total(self):
        pass

    def split_bill(self):
        pass




