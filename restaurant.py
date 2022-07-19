class Table:
    def __init__(self, diners):

        self.diners = diners
        self.bill = []

    def order(self, item, price, quantity=1):

        # Loop through existing list of items to check item is already there.
        for x in self.bill:
            if (x["item"]) == item:
                x["quantity"] += quantity
                return

        # Add if new item.
        menu_item = {"item": item, "price": price, "quantity": quantity}
        self.bill.append(menu_item)

    def remove(self, item, price, quantity=1):

        for x in self.bill:
            if x["item"] == item and x["price"] == price:
                if (x["quantity"] - quantity) == 0:
                    self.bill.remove(x)
                    return True
                elif (x["quantity"] - quantity) < 0:
                    return False
                else:
                    x["quantity"] -= quantity
                    return True

        return False

    def get_subtotal(self):

        subtotal = 0

        for x in self.bill:
            subtotal += (x["price"] * x["quantity"])

        return subtotal

    def get_total(self, service_charge = 0.10):

        subtotal = self.get_subtotal()
        sc_amount = subtotal * service_charge
        total = subtotal+sc_amount

        return {"Sub Total": '£{:,.2f}'.format(subtotal),
                     "Service Charge": '£{:,.2f}'.format(sc_amount),
                     "Total": '£{:,.2f}'.format(total)}

    def split_bill(self):
        return round((self.get_subtotal())/self.diners,2)
