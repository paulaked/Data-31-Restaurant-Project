# sub-total returns the total cost for the table based on the prices and quanities in the bill.

#need to go through the list, multiply through each price and quantity and add this to the subtotal.

#Iterate through a list of dictionaries within Python.

bill = [
    {
        "item": "sandwhich",
        "price": "1.5",
        "quantity": "1"
    },
    {
        "item": "crisps",
        "price": "0.5",
        "quantity": "2"
    },
    {
        "item": "water",
        "price": "0.4",
        "quantity": "3"
    },
    {
        "item": "cake",
        "price": "1.1",
        "quantity": "4"
    }
]

print(bill)

sub_total = 0

for d in bill:
    sub_total = sub_total + (float(d['price']) * float(d['quantity']))

print(sub_total)

print("{:.2f}".format(5.514646486484))

# for i in range(len(bill)):
#     if item == bill[0]["item"]:
        #bill[0]["quantity"] = str(int(bill[0]["quantity"]) + 2)

print(bill)
print(list(bill[0].values())[2])
print(bill[0]["quantity"])

bill[0]["quantity"] = str(int(bill[0]["quantity"]) + 2)

print(bill)

class Practise:
    def __init__(self, no_people):
        #self.bill = []
        self.no_people = no_people

    def sub_total_practise(self):
        sub_total_practise_value = self.no_people * 20
        return sub_total_practise_value

    def total_practise(self):
        total_practise_value = self.sub_total_practise() + 100
        return total_practise_value

print(Practise(10).sub_total_practise())
print(Practise(10).total_practise())