class Table:
    def __init__(self, number_of_people: int):
        self.number_of_people = number_of_people
        self.bill = []

    def order(self, item: str, price: float, quantity=1):
        duplicate_flag = False
        for bill_order in self.bill:
            if bill_order['item'] == item and bill_order['price'] == price:
                bill_order['quantity'] += quantity
                duplicate_flag = True

        if not duplicate_flag:
            self.bill.append({"item": item, "price": price, "quantity": quantity})

        print(self.bill)

    def remove(self, item: str, price: float, quantity=0):
        for order_item in self.bill:
            if order_item['item'] == item and order_item['price'] == price:
                if order_item["quantity"] - quantity > 0:
                    order_item["quantity"] -= quantity
                else:
                    self.bill.remove(order_item)

                print(self.bill)
                return True

        return False

    def get_subtotal(self):
        sub_total = 0
        for order_item in self.bill:
            sub_total += order_item['price'] * order_item['quantity']

        return sub_total

    def get_total(self, service_c=0.10):
        service_charge = self.get_subtotal() * service_c
        grand_total = self.get_subtotal() + service_charge
        bill_subtotal = "{:.2f}".format(self.get_subtotal())
        return {"Sub Total": f"£{bill_subtotal}", "Service Charge": f"£{service_charge}", "Total": f"£{grand_total}"}

    def split_bill(self):
        split_total = self.get_subtotal() / self.number_of_people
        return split_total
