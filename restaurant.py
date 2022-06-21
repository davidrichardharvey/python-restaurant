from decimal import Decimal
from unicodedata import decimal


class Table:

    def __init__(self, number_of_diners: int):
        self.number_of_diners = number_of_diners
        self.bill = []

    def compare_items_for_ordering(self,
                                   ordered_item):  # check if bill already contains the ordered item. If so, just update quantity
        for purchase in self.bill:
            if purchase["item"] == ordered_item["item"] and purchase["price"] == ordered_item["price"]:
                purchase["quantity"] += ordered_item["quantity"]
                return "Quantity increased"

        self.bill.append(ordered_item)
        return "Order Appended"

    def compare_items_for_removing(self, item_to_remove):
        for purchase in self.bill:
            if purchase["item"] == item_to_remove["item"] and purchase["price"] == item_to_remove["price"]:
                if item_to_remove["quantity"] == purchase[
                    "quantity"]:  # subtract the quantity. If it goes to 0 or lower, remove purchase from bill.
                    self.bill.remove(purchase)
                    return True
                elif item_to_remove["quantity"] < purchase["quantity"]:
                    purchase["quantity"] -= item_to_remove["quantity"]
                    return True
                else:
                    return False

        return False

    def order(self, item: str, price: float, quantity: int = 1):  # Method for ordering items

        menu_item = {"item": item, "price": price, "quantity": quantity}
        self.compare_items_for_ordering(menu_item)

    def remove(self, item: str, price: float, quantity: int = 1):  # Remove matching items from the bill

        menu_item = {"item": item, "price": price, "quantity": quantity}
        self.compare_items_for_removing(menu_item)

    def get_subtotal(self):
        subtotal = 0
        for purchase in self.bill:
            subtotal += purchase["price"] * purchase["quantity"]

        return subtotal

    def to_2dp(self, num):
        num = format(num, '.2f')
        num = Decimal(num)
        return num

    def get_total(self, service_charge_percentage: float = 10):

        subtotal = self.get_subtotal()
        subtotal = self.to_2dp(subtotal)

        service_charge_percentage = Decimal(str(service_charge_percentage))

        costs = {"Sub Total": f"£{subtotal}",
                 "Service Charge": f"£{round(subtotal * service_charge_percentage, 2)}",
                 "Total": f"£{round(subtotal + subtotal * service_charge_percentage, 2)}"
                 }

        return costs

    def split_bill(self):

        return self.get_subtotal() / self.number_of_diners