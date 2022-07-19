class Table:
    bill = []

    def __init__(self, customers_number):
        self.customers_number = customers_number

    def order(self, item, price, quantity=1):
        for dish in self.bill:
            if dish['item'] == item:
                dish['quantity'] += quantity
                return self.bill
        return self.bill.append({'item': item, 'price': price, 'quantity': quantity})

    def remove(self):
        pass

    def get_subtotal(self):
        pass

    def get_total(self):
        pass

    def split_bill(self):
        pass
