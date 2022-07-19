
class Table:
    def __init__(self, number_of_diners: int):
        self.bill = []
        self.number_of_diners = number_of_diners

    def order(self, item, price, quantity=1):
        self.bill.append({"item": item, "price": price, "quantity": quantity})
        return self.bill

    def remove(self, item, price, quantity):
        for order in self.bill:
            if order["item"] == item and order["price"] == price:
                if (order["quantity"] - quantity) >= 1:
                    order["quantity"] -= quantity
                else:
                    self.bill.remove(order)
                return True
        return False

    def get_subtotal(self):
        total_price = 0
        for order in self.bill:
            total_price += order["price"] * order["quantity"]
        return float("{:.2f}".format(total_price))

    def get_total(self, service_charge=0.1):
        sub_total = self.get_subtotal()
        total_price = sub_total * (1 + service_charge)
        return {'Sub Total': f"£{'{:.2f}'.format(sub_total)}", 
                'Service Charge': f"£{'{:.2f}'.format(sub_total * service_charge)}",
                'Total': f"£{'{:.2f}'.format(total_price)}"}
        

    def split_bill(self):
        sub_total = self.get_subtotal()
        split = sub_total / self.number_of_diners
        return float("{:.2f}".format(split))

table = Table(6)
table.order('Food1', 20.0, 3)
table.order('Food2', 10.0, 1)
table.order('Food3', 3.20, 1)

print(table.split_bill())