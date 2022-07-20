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
        subtotal = 0
        for key in self.bill:
            subtotal1 = key ["price"] * key ["quantity"]
            subtotal += subtotal1
        return subtotal

    def get_total(self, service_c=0.10):
        subtotal = self.get_subtotal()
        service_c = service_c * subtotal
        total1 = subtotal + service_c
        subtotal = "£{0:,.2f}".format(subtotal)
        service_c = "£{0:,.2f}".format(service_c)
        total1 = "£{0:,.2f}".format(total1)
        dict = {"Sub Total" : subtotal,"Service Charge" : service_c, "Total": total1}

        return dict



    def split_bill(self):
        total2 =0
        total2 += self.get_subtotal()
        total2 = total2/self.number_of_people
      
        return total2
