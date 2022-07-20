class Table:
    def __init__(self, diners=int):
        self.diners = diners
        self.bill = []


    def order(self, item, price,quantity= 1):
        self.bill.append({"item":item,"price":price,"quantity":quantity})
        return self.bill




    def remove(self, item, price,quantity):
        for v in range(0, len(self.bill)):
                    if self.bill[v]["item"] == item and self.bill[v]["price"] == price:
                        if self.bill[v]["quantity"] - int(quantity) >= 1:
                            self.bill[v]["quantity"] -= int(quantity)
                        else:
                            self.bill[v].clear()



    def get_subtotal(self):
        subtotal = 0
        for item in self.bill:
            subtotal += (item["price"] * item["quantity"])
        return subtotal



    #def get_total(self, subtotal, service_charge = 0.10) -> float:

     #   get_total = {"Sub Total": subtotal, "Service Charge":service_charge, "Total": total}
      #  total = service_charge + subtotal
       # return get_total
        #pass

    #def split_bill(self, subtotal, diners):
     #   split_bill(subtotal/diners)
       # return(split_bill())
        #pass
