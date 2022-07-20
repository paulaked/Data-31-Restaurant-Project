class Table:

    def __init__(self, num_of_customers):
        self.bill = []
        self.num_of_customers = num_of_customers


    def order(self, item, price, quantity = 1):
        if item not in self.bill:
            ordered = {"item": item, "price": price, "quantity": quantity}
            self.bill.append(ordered)
        else:
            for i in self.bill:
                if i.items() == item:
                    i.keys(quantity) + 1
        return self.bill

    def remove(self, item, price, quantity = "1"):
        for key in self.bill:
            if key["item"]  == item and key["price"] == price and quantity < key["quantity"]:
                key["quantity"] -= quantity
            elif key["item"]  == item and key["price"] == price and quantity >= key["quantity"]:
                key["quantity"] -= quantity
                key["quantity"] *= -1
            else:
                return False

    def get_subtotal(self):
     

    def get_total(self, SCharge = 0.1):

    def split_bill(self):




