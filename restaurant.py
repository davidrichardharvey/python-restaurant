class Table:

    def __init__(self, number_of_diners):
        self.number_of_diners = number_of_diners
        self.bill = []

    def order(self, item, price, quantity=1):
        for items in self.bill:
            if items["item"] == item and items["price"] == price:
                items["quantity"] += quantity
                break
            else:
                self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price, quantity=0):
        for items in self.bill:
            if items["item"] == item and items["price"] == price:
                if items["quantity"] - quantity > 0:
                    items["quantity"] -= quantity
                else:
                    self.bill.remove(item)
                return True
        return False

    def get_subtotal(self):
        subtotal_cost = 0
        for i in self.bill:
            subtotal_cost += i["quantity"] * i["price"]
        return subtotal_cost

    def get_total(self, service_charge=0.1):
        total_dictionary = {
            "Sub Total": "",
            "Service Charge": "",
            "Total": ""
        }

        sub_total = self.sub_total()
        total_service_charge = round(sub_total * service_charge, 2)
        total = sub_total + total_service_charge

        total_dictionary["Sub Total"] = f"£{sub_total}"
        total_dictionary["Service Charge"] = f"£{total_service_charge}"
        total_dictionary["Total"] = f"£{round(total, 2)}"
        return total_dictionary

    def spilt_bill(self):
        return round(self.sub_total/self.number_of_diners, 2)