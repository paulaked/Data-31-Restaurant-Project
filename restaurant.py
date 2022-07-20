class Table:
    def __init__(self, tablenumber):
        self.tablenumber = tablenumber
        self.bill = []

    def order(self, item: str, price, quantity=1):

        if item not in self.bill:  # checking if the item is already on the bill
            cheque = {"item": item, "price": price, "quantity": quantity}
            self.bill.append(cheque)
        else:  # if it is, then adding the quantity
            for food in self.bill:
                if food.items() == item:
                    food.keys(quantity) + 1
        return self.bill

    def remove(self, item, price, quantity):
        for key in self.bill: # Checking if the quantity is less than that on the bill
            if key["item"] == item and key["price"] == price and quantity < key["quantity"]:
                key["quantity"] -= quantity
            elif key["item"] == item and key["price"] == price and quantity >= key["quantity"]:
                self.bill.remove(key)
            else:
                return False

    def get_subtotal(self) -> float:
        cost_of_meal = 0
        for i in self.bill:
            cost_of_meal += (i["price"] * i["quantity"])
        return cost_of_meal

    def get_total(self, service_charge=0.10):
        sub_total = self.get_subtotal()
        charge_rate = sub_total * service_charge
        total = round((sub_total + charge_rate), 2)

        total_dict = {"Sub Total": '£{:,.2f}'.format(sub_total),
                      "Service Charge": '£{:,.2f}'.format(charge_rate),
                      "Total": '£{:,.2f}'.format(total)}

        return total_dict

    def split_bill(self):
        pass
