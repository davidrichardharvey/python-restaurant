class Table:

    def __init__(self, number_of_diners):
        self.number_of_diners = number_of_diners
        self.bill = []
        self.subtotal = 0
        self.total = 0

    def order(self, item, price, quantity=1):
        for items in self.bill:
            if items["item"] == item and items["price"] == price:
                items["quantity"] += quantity
                break
        else:
            self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price, quantity=1):
        for items in self.bill:
            if items["item"] == item and items["price"] == price:
                if items["quantity"] - quantity == 0:
                    self.bill.remove(items)
                elif items["quantity"] - quantity < 0:
                    return False
                else:
                    items["quantity"] -= quantity
                return True
        else:
            return False

    def get_subtotal(self):
        subtotal = 0
        for items in self.bill:
            subtotal += items["price"] * items["quantity"]
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
        bill_after_split = self.subtotal / self.number_of_diners
        return bill_after_split