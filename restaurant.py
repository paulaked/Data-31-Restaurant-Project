class Table:
    def __init__(self,number_of_people):
        self.number_of_people = number_of_people
        self.bill = []

    def order(self, item, price, quantity=1):
        for i in self.bill:
            if i['item'] == item:
                i['quantity'] += quantity
                return self.bill
        return self.bill.append({'item': item, 'price': price, 'quantity': quantity})

def remove(self, item, price, quantity):
    for k in self.bill:
        if k['item'] == item:
            k['quantity'] -= quantity
            return self.bill




    def get_subtotal(self, total_cost):
        self.total_cost = total_cost

    def get_total(self,total_cost, service_charge):
        self.total_cost = total_cost
        self.service_charge = service_charge

    def split_bill(self):
        pass
