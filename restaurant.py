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
                if dish['quantity'] == 0:
                    return self.bill.remove(dish)
                else:
                    return self.bill


    def get_subtotal(self):
        amount = 0
        for dish in self.bill:
            amount += dish['price'] * dish['quantity']
        return amount

    def get_total(self):
        pass

    def split_bill(self):
        pass
