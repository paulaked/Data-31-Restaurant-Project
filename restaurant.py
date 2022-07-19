class Table:
    def __init__(self, no_people):
        self.bill = []
        self.no_people = no_people

    def order(self, item, price, quantity: int = 1):
        self.item = item
        self.price = price
        self.quantity = quantity

        check = False   #whilst check == False, this means that the item is not already in the bill.

        for i in range(len(self.bill)):
            if item == self.bill[0]["item"]: #checking that the item has already been added to the bill.
                self.bill[0]["quantity"] = int(self.bill[0]["quantity"]) + quantity  #increasing the quantity instead of appending
                check == True   #letting the check know that the item was already in the bill so we do not need to append.

        if check == False:  #this means that the item was not already in the bill.
            self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price, quantity: int = 1):
        original_quantity = self.quantity

        check = False   #check is False if item is not in the bill, but turns True if the item is in the bill.

        #step1: dealing with the cases where the item is in the list.

        for i in range(len(self.bill)):
            if item == self.bill[i]["item"] and price == self.bill[i]["price"]:  # checking that the item is in the bill to remove it.
                check = True
                #now need to subtract the quantity from the overall quantity.
                self.bill[i]["quantity"] = int(self.bill[i]["quantity"]) - quantity
                if self.bill[i]["quantity"] == 0:    #if quantity is reduced to zero, we need to remove from the bill.
                    self.bill.remove(self.bill[i])
                    return True #the method worked as expected so return True
                if int(self.bill[i]["quantity"]) < 0:
                    self.bill[i]["quantity"] = original_quantity #if we can't remove that many items, there should be no changes and so reinstate the original_quantity
                    return False    #the method hasn't worked as we thought so return False

        #step2: dealing with the cases where the item is not in the list.
        if check == False:
            return False

    def get_subtotal(self):     #returns the total cost for the table based on the prices and quantities in the bill.
        sub_total = 0
        for d in self.bill:
            sub_total = sub_total + ( float(d['price']) * float(d['quantity']) )
        return sub_total

    def get_total(self, service_charge_percentage: float = 0.1):

        # I ran the sub_total calculations again because I wasn't sure how to get them from above since there is no self.sub_total (i.e. it is not an instance variable).

        sub_total = 0
        for d in self.bill:
            sub_total = sub_total + ( float(d['price']) * float(d['quantity']) )
        dict = {
            "Sub Total": "£" + "{:.2f}".format(sub_total),
            "Service Charge": "£" + "{:.2f}".format(sub_total * service_charge_percentage),
            "Total": "£" + "{:.2f}".format(sub_total + (sub_total * service_charge_percentage))
        }
        return dict

# when referencing a method from a different method within a class you need to include self.

    def split_bill(self):
        # I ran the sub_total calculations again because I wasn't sure how to get them from above since there is no
        # self.sub_total (i.e. it is not an instance variable).
        sub_total = 0
        for d in self.bill:
            sub_total = sub_total + ( float(d['price']) * float(d['quantity']) )
        return(round(sub_total / self.no_people, 2))
