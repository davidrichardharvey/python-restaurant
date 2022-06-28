class Table:

    def __init__(self, number_of_dinners):
        self.number_of_dinners = number_of_dinners
        self.bill = []

        # Order method - Takes the menu item, its price and the quantity ordered. If item has already been ordered, increases quanitty in bill. Otherwise, item is added to bill.

    def order(self, item: str, price: float, quantity=1):
        found = False
        for order_bill in self.bill:
            if order_bill['item'] == item and order_bill['price'] == price:
                order_bill['quantity'] += quantity
                found = True

        if not found:
            self.bill.append({"item": item, "price": price, "quantity": quantity})

        print(self.bill)

        # Remove method - Takes a menu item and removes it from the bill

    def remove(self, item: str, price: float, quantity=0):
        for order_item in self.bill:
            if order_item['item'] == item and order_item['price'] == price:
                if order_item['quantity'] - quantity > 0:
                    order_item['quantity'] -= quantity
                else:
                    self.bill.remove(order_item)

                    print(self.bill)
                    return True
        return False

        # Returns a value representing the total price * quantity of each menu item in the bill

    def get_subtotal(self):
        sub_total = 0
        for order_item in self.bill:
            sub_total += order_item['price'] * order_item['quantity']

        return sub_total

   # Returns a string with the Table sub total, service charger and total
    def get_total(self, service_charge=0.10):
        return {'Sub Total': f"£{self.get_subtotal():.2f}",
                'Service Charge': f"£{self.get_subtotal() * service_charge:.2f}",
                'Total': f"£{self.get_subtotal() * (1 + service_charge):.2f}"}

    def split_bill(self):
        split_total = self.get_subtotal() / self.number_of_dinners
        return split_total


