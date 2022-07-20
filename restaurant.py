class Table:
    def __init__(self, num_of_people):
        self.num_of_people = num_of_people
        self.bill = []

    def order(self, item, price, quantity=1):
        # aggregating quantity.
        for i in self.bill:
            if i['item'] == item and i['price'] == price:
                i['quantity'] += quantity
                return
        # consolidating order
        bill_additions = {
            'item': item,
            'price': price,
            'quantity': quantity
        }
        return self.bill.append(bill_additions)


    def remove(self, item, price, quantity=1):
        for i in self.bill:
            # catching quantity error first
            if quantity > i['quantity']:
                return False
            # removing quantity
            elif i['item'] == item and i['price'] == price:
                i['quantity'] -= quantity
                # removing entry if quantity reaches 0
                if i['quantity'] <= 0:
                return self.bill.remove(i)
            elif i['item'] != item and i['price'] != price:
                return False
            else:
                return True


    def get_subtotal(self):
        subtotal_bill = 0
        for i in self.bill:
            subtotal_bill += (i['price'] * i['quantity'])
        return subtotal_bill


    def get_total(self, service_charge=0.1):
        subtotal = self.get_subtotal()
        service_charge_calc = subtotal * service_charge

        def_total = {
            'Sub Total': subtotal,
            'Service Charge': service_charge_calc,
            'Total': subtotal + service_charge_calc
        }
        return def_total


    def split_bill(self):
        total_bill = self.get_total()
        split = total_bill / self.num_of_people
        return split


