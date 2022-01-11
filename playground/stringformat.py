amount = 30 * 49.99
total_amount = f"Total is: {amount: ,.2f}"


sales_tax_rate = f"Sales tax rate is: {0.065: .2%}"
print(sales_tax_rate)

unit_price = 49.95
quantity = 32
sales_tax_rate = 0.065
subtotal = unit_price * quantity
s_subtotal = f"${subtotal:,.2f}"
sales_tax = subtotal * sales_tax_rate
s_sales_tax = f"${sales_tax:,.2f}"
total = f"${subtotal + sales_tax:,.2f}"
output = f"""
Subtotal:  {s_subtotal:>9}
Sales Tax: {s_sales_tax:>9}
Total:     {total:>9}
"""

print(output)

s = "Abracadabra Hocus Pocus you're a turtle dove"
print("t" in s)
print("T" in s)
print("T" not in s)
print("-" * 15)
print(s[0])
print(s[33:39])
print(s[0:44:3])
print(min(s))
print(max(s))
print(s.index("P"))
print(s.index("o", int(len(s) / 2), len(s)))
print(s.count("a"))
print(len(s))
a = len(s) / 2