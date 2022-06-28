class Table:

    def __init__(self, diners):
        self.diners = diners
        self.bill = []
        self.subtotal = 0
        self.total = 0

    def order(self, item, price, quantity=1):
        for bills in self.bill:
            if bills["item"] == item and bills["price"] == price:
                bills["quantity"] += quantity
                break
        else:
            self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price, quantity=1):
        for bills in self.bill:
            if bills["item"] == item and bills["price"] == price:
                if bills["quantity"] - quantity == 0:
                    self.bill.remove(bills)
                elif bills["quantity"] - quantity < 0:
                    return False
                else:
                    bills["quantity"] -= quantity
                return True
        else:
            return False

    def get_subtotal(self):
        subtotal = 0
        for bills in self.bill:
            subtotal += bills["price"] * bills["quantity"]
        self.subtotal = float("{:.2f}".format(subtotal))
        return subtotal

    def get_total(self, service_charge=0.10):
        self.get_subtotal()
        self.total = self.subtotal + self.subtotal * service_charge
        return {"Sub Total": "£" + "{:.2f}".format(self.subtotal),
                "Service Charge": "£" + str(self.subtotal * service_charge),
                "Total": "£" + str(self.subtotal + self.subtotal * service_charge)}

    def split_bill(self):
        self.get_total()
        splitted_bill = self.subtotal / self.diners
        return splitted_bill
