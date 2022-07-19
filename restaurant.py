class Table:

    def __init__(self, dinners):
        self.dinners = dinners

        self.bill = []




    def order(self, item, price, quantity=1): # **kwargs keyword passes arguments to a function that are assigned to a particular keyword.

        #list = {"item": [], "price": [], "quantity": []};

        #if {"item": item, "price": price, "quantity":quantity} in bill.values():
        #    quantity = quantity + 1

        for num in self.bill:
            if(num["item"]) == item:
                pass

        list = {"item": item, "price": price, "quantity":quantity}
        self.bill.append(list)
        self.bill["item"].append(item)
        self.bill["price"].append(price)
        self.bill["quantity"].append(quantity)


    def remove(self, item, price, quantity=1):
        for food_item in self.bill:
            if food_item["item"] == item and food_item["price"] == price:
                if (food_item["quantity"] - quantity) == 0:
                    self.bill.remove(food_item)
                    return True
                #elif


    def get_subtotal(self):
        pass


    def get_total(self):
        pass

    def split_bill(self):
        pass
