class Table:

    def __init__(self, dinners):
        self.dinners = dinners
        self.bill = [] # instance variable of bill list


    def order(self, item, price, quantity=1):
        '''

        :param item: the food item
        :param price: the price of the food item
        :param quantity: the quantity of the food item, defaults to 1
        :return: appends item to list
        '''

        for food_item in self.bill:
            if(food_item["item"]) == item:
                food_item["quantity"] = food_item["quantity"] + quantity
                return self.bill

        dict_details = {"item": item, "price": price, "quantity":quantity}
        return self.bill.append(dict_details) # append item to list



    def remove(self, item, price, quantity=1):
        '''
        Function to remove item by decreasing the quantity available
        based on 'item' and 'price'
        :param item: the food item
        :param price: the price of the food item
        :param quantity: the quantity of the food item, defaults to 1
        :return: Bool
        '''
        for food_item in self.bill:

            if food_item["item"] == item and food_item["price"] == price:

                if (food_item["quantity"] - quantity) == 0:
                    self.bill.remove(food_item)
                    return True

                elif (food_item["quantity"] - quantity) < 0:
                    return False

                else:
                    food_item["quantity"] = food_item["quantity"] - quantity
                    return True



    def get_subtotal(self):
        '''
        Function to get subtotal for bill

        :return: the total of the subtotal
        '''
        sum_of_subtotal = 0

        for food_item in self.bill:
            sum_of_subtotal = sum_of_subtotal + (food_item["price"] * food_item["quantity"])

        return sum_of_subtotal



    def get_total(self, service_charge):
        '''
        Function to get the totals of subtotal, service charge and total cost.
        :param service_charge: 10% service charger of the total
        :return: totals_dict - totals in dictionary format
        '''

        sum_of_subtotal = self.get_subtotal() #get the subtotal
        sum_of_service_charge = sum_of_subtotal * service_charge #Sum of the service charge

        total_cost = sum_of_subtotal + sum_of_service_charge #Sum of subtotal and service charge

        #Dict breakdown of the cost
        totals_dict = {"Sub Total": '£{:,.2f}'.format(sum_of_subtotal),
                       "Service Charge": '£{:,.2f}'.format(sum_of_service_charge),
                       "Total": '£{:,.2f}'.format(total_cost)}
        return totals_dict

    def split_bill(self):
        '''
        Function to split the bill which splits the bill to the number of diners equally
        :return: the cost per diner
        '''

        overall_price = self.get_subtotal() #get sub total

        cost_per_diner = overall_price / self.dinners
        return round(cost_per_diner, 2)
