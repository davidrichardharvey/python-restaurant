class Table:

    global bill

    def __init__(self, people: int):
        self.people = people
        self.bill = []
        self.sub_total = 0
        self.total = 0


    def order (self, food: str, price: float, quantity = 1):
        self.food = food
        self.price = price
        self.quantity = quantity


        self.bill.append({
            'item': self.food,
            'price': self.price,
            'quantity': self.quantity})

        # for entry in self.bill:
        #     if entry['food'] == self.food:
        #         print('same')
        #         print(entry['food'])
        #         entry['quantity'] += 1
        #
        #     else:
        #         print("not same")
        #         self.bill.append({
        #             'item': self.food,
        #             'price': self.price,
        #             'quantity': self.quantity})


    def remove(self, food, price, quantity):

        for order in self.bill:
            if order["item"] == food:
                order["quantity"] -= quantity


    def get_subtotal(self):

        for order in self.bill:

            self.sub_total += order["price"] * order["quantity"]

        return round(self.sub_total,2)

    def get_total(self, service_charge=0.10):

        total_dic = {
            'Sub Total':'',
            'Service Charge': '',
            'Total':''
        }



        subTotal = self.get_subtotal()
        totalServiceCharge = round(subTotal * service_charge, 2)
        total = subTotal + totalServiceCharge

        total_dic['Sub Total'] = '£' + str(subTotal)+str(0)
        total_dic['Service Charge'] = '£' + str(totalServiceCharge)
        total_dic['Total'] = '£' + str(round(total, 2))
        return total_dic

        # self.service_charge = service_charge
        # self.total = {
        #
        #     "Sub Total": int(self.get_subtotal()),
        #     "Service Charge": round(self.service_charge * int(self.get_subtotal()),2),
        #     # "Sub Total": int(self.sub_total),
        #
        #     "Total": (int(self.sub_total) * self.service_charge) + self.sub_total
        # }
        #
        # return self.total



    def split_bill(self):
        return round( self.get_subtotal() / self.people, 2)



