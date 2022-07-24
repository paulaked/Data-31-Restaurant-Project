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
            if i['item'] == item and i['price'] == price:
                # remove from bill if reaches zero
                if i['quantity'] <= 0:
                    self.bill.remove(i)
                    return True
                # catching wrong input
                elif quantity > i['quantity']:
                    return False
                # altering bill quantity
                else:
                    i['quantity'] -= quantity
                    return True


    def get_subtotal(self):
        subtotal_bill = 0
        # calculating subtotal
        for i in self.bill:
            subtotal_bill += (i['price'] * i['quantity'])
        return subtotal_bill


    def get_total(self, service_charge=0.10):
        # calculating service charge and adding to total bill
        subtotal = self.get_subtotal()
        service_charge_calc = (subtotal * service_charge)
        the_total = (subtotal + service_charge_calc)

        # presenting a dictionary of values in gbp
        return {
            'Sub Total': '£%0.2f' % subtotal,
            'Service Charge': '£%0.2f' % service_charge_calc,
            'Total': '£%0.2f' % the_total}


    def split_bill(self):
        # splitting bill between people at table, rounded to the penny
        return round((self.get_subtotal()) / self.num_of_people, 2)