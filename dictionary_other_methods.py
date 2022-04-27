product = {
    'name': '',
    'price': 0.00,
    'taxable': '',
    'in_stock': 0,
    'models': [],
    'shippable': False 
}

sku_1 = dict.fromkeys(['name', 'price', 'taxable', 'in_stock', 'models'])
print(sku_1)

# copying keys from another dictionary
sku_2 = dict.fromkeys(product.keys())
print(sku_2)