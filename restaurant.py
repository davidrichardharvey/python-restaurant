class Table:

    def __init__(self, number_of_diners):
        self.number_of_diners = number_of_diners
        self.bill = []

    def order(self, item, price, quantity=1):
        for items in self.bill:
            if items["item"] == item and items["price"] == price:
                items["quantity"] += quantity
        else:
            self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price, quantity=1):
        for items in self.bill:
            if items["item"] == item and items["price"] == price:
                if items["quantity"] - quantity == 0:
                    self.bill.remove(bills)
                elif items["quantity"] - quantity < 0:
                    return False
                else:
                    items["quantity"] -= quantity
                return True
        else:
            return False

    def get_subtotal(self):
        sub_total = 0
        for items in self.bill:
            sub_total += items["price"] * items["quantity"]
        self.sub_total = round(sub_total, 2)
        return sub_total

    def get_total(self, service_charge=0.1):
        self.get_subtotal()
        total = self.sub_total + self.sub_total * service_charge
        total_service_charge = round(self.sub_total * service_charge, 2)

        return {"Sub Total": f"£{self.sub_total}0",
                "Service Charge": f"£{total_service_charge}",
                "Total": f"£{total}"}

    def split_bill(self):
        self.get_total()
        split = self.sub_total / self.number_of_diners
        return split