class Table:

    def __init__(self, dinners):
        self.dinners = dinners
        self.bill = [] # instance variable of bill list


    def order(self, item, price, quantity=1):

        for food_item in self.bill:
            if(food_item["item"]) == item:
                food_item["quantity"] = food_item["quantity"] + quantity
                return

        dict = {"item": item, "price": price, "quantity":quantity}
        self.bill.append(dict)


    def remove(self, item, price, quantity=1):
        for food_item in self.bill:

            if food_item["item"] == item and food_item["price"] == price:

                if (food_item["quantity"] - quantity) == 0:
                    self.bill.remove(food_item)
                    return True

                elif (food_item["quantity"] - quantity) < 0:
                    return False

                else:
                    food_item[quantity] = food_item[quantity] - quantity
                    return True



    def get_subtotal(self):
        sum_of_subtotal = 0

        for food_item in self.bill:
            sum_of_subtotal = sum_of_subtotal + ((food_item["price"]) * (food_item["quantity"]))

        return sum_of_subtotal



    def get_total(self, service_charge = 0.1):

        sum_of_subtotal = self.get_sum_of_subtotal()
        sum_of_service_charge = sum_of_subtotal * service_charge

        total_cost = sum_of_subtotal + sum_of_service_charge

    def split_bill(self):
        pass
