
class Table:
    def __init__(self, number_of_diners: int):
        self.bill = []
        self.number_of_diners = number_of_diners

    def order(self, item, price, quantity=1):
        return self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price, quantity):
        for order in self.bill:
            if self.bill[order]["item"] == item and self.bill[order]["price"] == price:
                if (self.bill[order]["quantity"] - quantity) >= 1:
                    self.bill[order]["quantity"] -= quantity
                    return self.bill[order]["quantity"]
                else:
                    return self.bill[order].remove()

    def get_subtotal(self):
        total_price = 0
        for order in self.bill:
            total_price += self.bill[order]["price"] * self.bill[order]["quantity"]
        return round(total_price, 2)

    def get_total(self, service_charge=0.1):
        total_price = self.get_subtotal()
        total_price += total_price * service_charge
        return round(total_price, 2)
        

    def split_bill(self):
        sub_total = self.get_subtotal()
        split = sub_total / self.number_of_diners
        return round(split, 2)
