

class Table:
    def __init__(self, diners):
        self.diners = diners
        self.bill = []



    def order(self, item, price, quantity=1):
        bill = []
        item_found = False
        for ord in self.bill:
            if ord['item'] == item and ord['price'] == price:
                ord[quantity] += quantity
                item_found = True
        if item_found == False:
            self.bill.append({"item":item, "price": price, "quantity": quantity})

        return self.bill

    def remove(self, item, price, quantity=1):
        for ord in self.bill:
            if ord['item'] == item and ord['price'] == price:

                if ord['quantity'] - quantity <= 0:
                    self.remove(item)
                else:
                    ord['quantity'] -= quantity
                break
            else:
                return False
        return self.bill

    def get_subtotal(self):
        sub_total = 0
        for ord in self.bill:
           sub_total += ord["price"] * int(ord["quantity"])
        return sub_total

    def get_total(self, tip = 0.10):
        sub_total = self.get_subtotal()
        service = sub_total*tip
        total = format(sub_total + service, '.2f')
        charge = {"Sub Total": '£' + str(sub_total), "Service Charge": '£' + str(service), "Total": '£' + str(total)}
        return charge

    def split_bill(self):
        sub_total = self.get_subtotal()
        divided = format(sub_total/self.diners, '.2f')
        return '£' + str(divided)

table05 = Table(5)
print(table05.order('Food1', 10.00, 3))
print(table05.get_total(0.15))

table06 = Table(6)
table06.order('Food1', 20.00, 3)
table06.order('Food2', 10.00, 1)
table06.order('Food3', 3.20, 1)
print(table06.split_bill())


table02 = Table(2)
table02.order('Food', 10.00, 5)
print(table02.remove('Food', 10.00, 3))
print(table02.bill)




