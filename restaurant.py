#Complete the Table class in restaurant.py. It should be able to instantiate objects to represent tables of diners
#   at a restaurant.
# When objects are created they are passed in the number of people dining at that table. The class should have an
#   instance variable called bill that is a list.
# The class should also contain the following methods:
#
# An order method that accepts an item and a price. It should optionally accept a quantity, which should default to 1 if none is provided.
# The method should append a menu item to the bill in the form of {"item": item, "price": price, "quantity": quantity}.
# If the bill already contains an item with the same item name and price, then it should instead update the quantity by adding on the new quantity to the existing quantity.
#
# A remove method, that is similar to the order method but instead subtracts the quantity from the item in the bill
#   with the matching item and price.
# If this would reduce the quantity to zero, the item should be removed from the bill entirely.
# The method should return True unless there is not an item with the corresponding item name and price
#   (or the corresponding item has a quantity less than the quantity desired for removal), in which case it should return False
#   and make no change to the bill.
#
# A get_subtotal method that returns the total cost for the table based on the prices and quantities in the bill.

# A get_total method that accepts a service charge percentage in the form of a decimal.
#   If no service charge percentage is provided, it should default to 10% (i.e. 0.10).
#   This method should return a dictionary with the following keys: Sub Total, Service Charge, Total.
#   The values should be string representations of the corresponding prices in British pounds and pence.
#       e.g. {"Sub Total": "£120.00", "Service Charge": "£12.00", "Total": "£132.00"}

# A split_bill method, which returns the the subtotal cost of the bill divided by the number of diners as a
#   float rounded up to the nearest penny.

class Table():
    #Instance variables

    #Bill - List containing Table orders- items, prices, and quantities.
    bill = []
    #Diners - Integer representing the number of customers dining at a Table.
    diners = 0


    #Methods

    #Object constructor - Takes the number of people present at the Table as an integer value.
    def __init__(self, number_of_people: int):
        diners = number_of_people
        pass

    #Order method - Takes the menu item, its price and the quantity ordered. If item has already been ordered, increases quanitty in bill. Otherwise, item is added to bill.
    def order(self, item, price, quantity=1):
        if len(self.bill) > 0:
            found = False
            for order_line in self.bill:
                if order_line["item"] == item and order_line["price"] == price:
                    order_line["quantity"] += quantity
                    found = True
            if found == False:
                new_order = {"item": item, "price": price, "quantity": quantity}
                self.bill.append(new_order)
        else:
            new_order = {"item": item, "price": price, "quantity": quantity}
            self.bill.append(new_order)

    #Remove method - Takes a menu item and removes it from the bill
    def remove(self, item, price, quantity=1):
        for order_line in self.bill:
            if order_line["item"] == item and order_line["price"] == price:
               if order_line["quantity"] - quantity == 0:
                   self.bill.remove(order_line)
                   return True
               elif order_line["quantity"] - quantity > 0:
                   order_line["quantity"] -= quantity
                   return True
            else:
                return False

    #Get Subtotal method - Returns an value representing the total price * quantity of each menu item in the bill
    def get_subtotal(self):
        subtotal = 0
        for order_line in self.bill:
            subtotal += order_line["price"] * order_line["quantity"]
        return subtotal

    #Get total - Takes a float representing Table service charge. Returns a string with the Table sub total, service charger and total (subtotal percentage increased by service charge) of each menu item in the bill
    def get_total(self, service_charge=0.1):
        subtotal = self.get_subtotal()
        return f"\"Sub Total\": \"£{subtotal}\", \"Service Charge\": \"£{service_charge}\", \"Total\": \"£{subtotal+(1+service_charge)}\""

    #Split Bill method -  Returns the subtotal divided by the number of diners at Table
    def split_bill(self):
        split = self.get_subtotal() / self.diners
        return split.__round__(4)