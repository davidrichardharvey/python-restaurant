class Table:
    def __init__(self, number_of_diners):
        self.number_of_diners = number_of_diners
        self.bill = []

    def order(self, item, price, quantity=1):
        # At the start duplicate is false because there are no orders
        dup = False
        for order_item in self.bill:
            if order_item["item"] == item and order_item["price"] == price:
                order_item["quantity"] += quantity
                dup = True
        # If there is no duplicates add the item
        if dup == False:
            self.bill.append({"item": item, "price": price, "quantity": quantity})
        return self.bill

    def remove(self, item, price, quantity=0):
        for order_item in self.bill:
            if order_item["item"] == item and order_item["price"] == price:
                # If the quantity is greater than 0 subtract when you want to remove the same item
                if order_item["quantity"] - quantity > 0:
                    order_item["quantity"] -= quantity
                # If there's only one quantity I want to get rid remove from list
                else:
                    self.bill.remove(order_item)
                return True
        # Return False if no changes have been made
        return False

    def get_subtotal(self):
        subtotal = 0
        for order_item in self.bill:
            subtotal += order_item["price"] * order_item["quantity"]
        return subtotal

    def get_total (self, service_charge = 0.1):
        sv = self.get_subtotal() * service_charge
        total = self.get_subtotal() + sv
        bill_form = "{:.2f}".format(self.get_subtotal())
        return {"Sub Total":f"£{bill_form}", "Service Charge": f"£{sv}", "Total":f"£{total}"}

    def split_bill (self):
        return self.get_subtotal() / self.number_of_diners


