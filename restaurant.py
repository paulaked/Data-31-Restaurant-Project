class Table:
    def __init__(self, diners):
        self.diners = diners
        self.bill = []

    def order(self, item: str, price: float, quantity: int = 1):
        """Add an order to the order list"""
        for i in self.bill:
            if i['item'] == item and i['price'] == price:  # check if price and name match
                i['quantity'] += quantity
                return self.bill
        return self.bill.append({'item': item, 'price': price, 'quantity': quantity})

    def remove(self, item: str, price: float, quantity: int):
        """Remove an order to the order list"""
        for j in self.bill:
            if j['item'] == item:  # and j['price'] == price: # check for match
                j['quantity'] -= quantity
                if j['quantity'] <= 0:
                    return self.bill.remove(j)
        return self.bill

    def get_subtotal(self):
        """Get sub-total for all current orders"""
        sub = 0
        for k in self.bill:
            sub += k['price'] * k['quantity']
        return sub

    def get_total(self, tip=0.1):
        """Get total for all current orders including tip"""
        sub_total = self.get_subtotal()
        service_charge = sub_total * tip  # add tip
        ttl = sub_total + service_charge
        total = {"Sub Total": "£%0.2f" % sub_total, "Service Charge": "£%0.2f" % service_charge,
                 "Total": "£%0.2f" % ttl}

        return total

    def split_bill(self):
        """Get split total for each diner on all current orders"""
        total = self.get_subtotal()
        return round(total / self.diners, 2)
