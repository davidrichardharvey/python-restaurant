class Table:
    def __init__(self, number_of_diners):
        self.number_of_diners = number_of_diners  # number of persons per table
        self.bill = []  # bill list to store items, price and quantity in a DICTIONARY (inside this list)

    # order method
    def order(self, item, price, quantity=1):
        for menu in self.bill:
            if menu.get('item') == item and menu.get('price') == price:
                menu['quantity'] += quantity  # counter to increase number or quantity and respective price
                break
        # append item, price and quantity to bill and round to 2 decimals
        # APPEND adds another dictionary if one already exists
        self.bill.append({"item": item, "price": round(float(price), 2), "quantity": quantity})
        return self.bill

    # remove method
    def remove(self, item, price, quantity=1):
        for menu in self.bill:  # for loop to iterate through list bill
            if menu.get('item') == item and menu.get('price') == price:
                if menu.get('quantity') <= quantity:
                    self.bill.remove(menu)
                    return True
                else:
                    menu['quantity'] -= quantity  # counter to decrease number of quantity
        return False

    # calculate subtotal method
    def get_subtotal(self):
        subtotal = 0  # counter to add the calculations
        for menu in self.bill:  # for loop to iterate through the bill
            subtotal += menu.get("price") * menu.get("quantity")  # multiply price by quantity and then add to subtotal
        return float(round(subtotal, 2))  # return rounded to 2 decimals

    # calculate total with service charge included
    def get_total(self, service_charge=0.10):
        return {'Sub Total': f"£{self.get_subtotal():.2f}",
                'Service Charge': f"£{self.get_subtotal() * service_charge:.2f}",
                'Total': f"£{self.get_subtotal() * (1 + service_charge):.2f}"}

    #  splitting the total by the total number of dinners
    def split_bill(self):
        return round(self.get_subtotal() / self.number_of_diners, 2)
