class Table:
    def __init__(self, diners):

        self.diners = diners
        self.bill = []

    def order(self, item, price, quantity = 1):

        # Loop through existing list of items to check item is already there.
        for order in self.bill:
            if (order["item"]) == item:
                order["quantity"] += quantity
                return

        # Add if new item.
        menu_item = {"item": item, "price": price, "quantity": quantity}
        self.bill.append(menu_item)

    def remove(self, item, price, quantity=1):

        for order in self.bill:

            if order["item"] == item and order["price"] == price:
                # Remove item if none left.
                if (order["quantity"] - quantity) == 0:
                    self.bill.remove(order)
                    return True
                # Invalid if quantity is rendered negative.
                elif (order["quantity"] - quantity) < 0:
                    return False
                # Otherwise, remove specified number of items.
                else:
                    order["quantity"] -= quantity
                    return True

        return False

    def get_subtotal(self):

        subtotal = 0

        for order in self.bill:
            subtotal += (order["price"] * order["quantity"])

        return subtotal

    def get_total(self, service_charge = 0.10):

        # Get values for each.
        subtotal = self.get_subtotal()
        sc_amount = subtotal * service_charge
        total = subtotal+sc_amount

        # Format and return.
        return {"Sub Total": '£{:,.2f}'.format(subtotal),
                     "Service Charge": '£{:,.2f}'.format(sc_amount),
                     "Total": '£{:,.2f}'.format(total)}

    def split_bill(self):

        # Divide bill by number of diners and round to nearest penny.
        return round((self.get_subtotal())/self.diners,2)
