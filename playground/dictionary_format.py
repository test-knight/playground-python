product = {
    'name': 'Ray-Ban Aviator Sunglasses',
    'price': 112,
    'taxable': True,
    'in_stock': 10,
    'models': ['Gun Metal', 'Metallic']
}

print('Product:   ', product['name'])
print('Price:     ', f"${product['price']:.2f}")
print('Taxable:   ', product['taxable'])
print('In Stock:  ', product['in_stock'])

print('Models:')
for model in product['models']:
    print(' '*11, model)
