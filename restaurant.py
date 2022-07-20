class Table:
    def __init__(self,number_of_people):
        self.number_of_people = number_of_people
        self.bill = []

    def order(self, item, price, quantity=1):
        for i in self.bill: # i = item they are adding/ordering
            if i['item'] == item:
                i['quantity'] += quantity
                return self.bill
        return self.bill.append({'item': item, 'price': price, 'quantity': quantity})

    def remove(self, item, price, quantity):
        for k in self.bill: # k = item they are removing
            if k['item'] == item:
                k['quantity'] -= quantity
                if k['quantity'] <= 0:
                    return self.bill.remove(k)
                else:
                    return self.bill

    def get_subtotal(self):
        subtotal = 0
        for i in self.bill:
            subtotal += i['price'] * i['quantity']
        return subtotal

    def get_total(self, service_charge=0.1):
        subtotal = self.get_subtotal()
        sc = subtotal * (service_charge)
        total = subtotal + sc
        receipt = {'Sub Total': '£{:.2f}'.format(subtotal), 'Service Charge': '£{:.2f}'.format(sc),
                   'Total': '£{:.2f}'.format(total)}
        return receipt


    def split_bill(self):
        cost = self.get_subtotal()
        sb = (cost / self.number_of_people)
        return round(sb,2)


table = Table(6)
table.order('Food', 23.0, 3)
table.order('Food2', 8.0, 1)
table.order('Food3', 3.20, 5)

print(table.get_total())