class Table:
    def __init__(self, number_of_diners):
        self.number_of_diners = number_of_diners
        self.bill = []

    def order(self, item, price, quantity=1):
        for i in self.bill:
            if i.get('item') == item and i.get('price') == price:
                i.quantity['quantity'] += quantity
                break
        self.bill.append({"item": item, "price": price, "quantity": quantity})
        return self.bill

    def remove(self, item, price, quantity=1):
        for i in self.bill:
            if i.get('item') == item and i.get('price') == price and i.get('quantity') <= quantity:
                self.bill.remove(i)
                return True
            else:
                i['quantity'] -= quantity
        return False

    def get_subtotal(self):

        cart = 0
        for i in self.bill:
            cart += i.get('price') * i.get('quantity')
        return cart

    def get_total(self, service_charge=0.10):

        return {'Sub Total': f"£{self.get_subtotal():.2f}",
                'Service Charge': f"£{self.get_subtotal() * service_charge:.2f}",
                'Total': f"£{self.get_subtotal() * (1 + service_charge):.2f}"}

    def split_bill(self):
        return round((self.get_subtotal() / self.number_of_diners), 2)
