class Table:
    def __init__(self, customers_number):
        self.customers_number = customers_number
        self.bill = []

    def order(self, item, price, quantity=1):
        for dish in self.bill:
            if dish['item'] == item:
                dish['quantity'] += quantity
                return self.bill
        return self.bill.append({'item': item, 'price': price, 'quantity': quantity})

    def remove(self, item, price, quantity):
        for dish in self.bill:
            if dish['item'] == item:
                dish['quantity'] -= quantity
                if dish['quantity'] <= 0:
                    return self.bill.remove(dish)
                else:
                    return self.bill

    def get_subtotal(self):
        amount = 0
        for dish in self.bill:
            amount += dish['price'] * dish['quantity']
        return amount

    def get_total(self, tip=0.1):
        sub_total = self.get_subtotal()
        service_charge = sub_total * tip
        total = sub_total + service_charge
        checkout = {"Sub Total": "£%0.2f" % sub_total, "Service Charge": "£%0.2f" % service_charge,
                    "Total": "£%0.2f" % total}
        return checkout

    def split_bill(self):
        checkout = self.get_subtotal()
        return round(checkout / self.customers_number, 2)
