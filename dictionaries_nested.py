products = {
    'sku_001': {'name': 'ray-ban', 'price': 112.90, 'taxable': False},
    'sku_002': {'name': 'cartier', 'price': 1500.00, 'taxable': True},
    'sku_003': {'name': 'Philips brush', 'price': 95, 'taxable': False},
    'sku_004': {'name': 'Vaccumm', 'price': 45, 'taxable': False}
}

print(f"{'Name':<16} {'Price':>12} {'Taxable'}")
print("=" * 50)

for product_key in products.keys():
    product_id = product_key
    product_name = products[product_key]['name']
    price = f"${products[product_key]['price']:,.2f}"
    product_taxable = products[product_key]['taxable']
    print(f'{product_name:<16} {price:>12} {product_taxable}')
