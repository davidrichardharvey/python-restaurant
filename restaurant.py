class Table:

    def __init__(self,number_of_dinners):
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

    #def remove(self, item: str, price: float, quantity=0):




