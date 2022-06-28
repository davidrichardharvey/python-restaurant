from restaurant import Table
from unittest import main

table01 = Table(5)
print("get 2 risottos")
table01.order("Risotto", 12.50, 2)
print(table01.bill)
print("get 3 burrito")
table01.order("Burrito", 20.43, 3)
print(table01.bill)
print("REMOVE 2 burrito")
table01.remove("Burrito", 20.43, 2)
print(table01.bill)
print("sub total")
print(table01.get_subtotal())
print("full bill")
print(table01.get_total(0.15))
print("bill split")
print(table01.split_bill())

# Run unit tests automatically
main(module='test_module', exit=False)