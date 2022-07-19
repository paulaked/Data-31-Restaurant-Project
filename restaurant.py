class Table:

    def __init__(self, num_of_people):
        self.bill = []
        self.num_of_people = num_of_people

    def order(self, item, price, quantity = 1):
        if item not in self.bill:
            ordered = {'item': item, 'price': price, 'quantity': quantity}
            self.bill.append(ordered)
        else:
            for i in self.bill:
                if i.items() == item:
                    i.keys(quantity) + 1
        return self.bill

    def remove(self, item, price, quantity):
        for key in self.bill:
            if key["item"] == item and key["price"] == price and quantity < key["quantity"]:
                key["quantity"] -= quantity
            elif key["item"] == item and key["price"] == price and quantity >= key["quantity"]:
                self.bill.remove(key)
            else:
                return False


    def get_subtotal(self):
        subtotal = 0
        for key in self.bill:
            temp = key['price'] * key['quantity']
            subtotal += temp

        return subtotal

    def get_total(self, sc):
        subtotal = self.get_subtotal()
        service_charge = subtotal * sc
        total = subtotal + service_charge
        subtotal = "£{:,.2f}".format(subtotal)
        service_charge = "£{:,.2f}".format(service_charge)
        total = "£{:,.2f}".format(total)
        dict = {'Sub Total': subtotal, 'Service Charge': service_charge, 'Total': total}

        return dict

    def split_bill(self):
        total = 0
        total += self.get_subtotal()
        total = total / self.num_of_people
        return total




new = Table(2)
new.order("food", 10.00, 2)
new.remove("food", 10.00, 3)
print(new.bill)