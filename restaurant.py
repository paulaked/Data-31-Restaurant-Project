class Table:
    def __init__(self):
        self.bill = []

    def order(self, item: str, price: float, quantity: int =1):
        for i in self.bill:
            if i['item'] == item and i['price'] == price:
                i['quantity'] += quantity
                return self.bill
        return self.bill.append({'item': item, 'price': price, 'quantity': quantity})


    def remove(self, item: str, price: float, quantity: int):
        for j in self.bill:
            if j['item'] == item:
                j['quantity'] -= quantity
                if j['quantity'] <= 0:
                    return self.bill.remove(j)
        return(self.bill)

    def get_subtotal(self):
        pass
        self.bill.values()

    def get_total(self):
        pass

    def split_bill(self):
        pass

t = Table()
#print(t.item)
#print(t.quantity)
print("Bill: ",t.bill)
print(t.order('pie', 9.6))
print("Bill: ",t.bill)
print(t.order('pizza', 3.50, 4))
print("Bill: ",t.bill)
print(t.order('pizza', 3.50, 2))
print(t.order('pizza', 6.50, 2))
print("Bill: ",t.bill)