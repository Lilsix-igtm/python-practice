import json

#The above is an ordinary python dictionary.
student = {
    'name': 'Peter',
    'age': 20,
    'is student': True
}

json_data = json.dumps(student)
print(json_data)

# json refers to the imported module.
# dumps() is a method provided by that module. it Converts Python data into JSON text (in temporary memory)
# student is the dictionary we're converting.
# json_data stores the converted result temporarily.

product = {
    'product_name': "Vitamin C Serum",
    'pric': 15000,
    'availabl': True,
    'quantit': 12,
    'categories': ['Skincare', 'Beauty', 'Face serum',]
}

json_product = json.dumps(product)
print(json_product)

new_product = json.loads(json_product)
print(new_product)

print(new_product['product_name'])
# json.loads() takes JSON text.
# It converts that text into Python data.
# We store the result in new_product.

products = {
    'name': 'Vitamin C serum',
    'price': 15000,
    'availability': True,
    'quantity': 12
}

json_products = json.dumps(products, indent=4)
print(json_products)

p_json = json.loads(json_products)
print(p_json)

#indent=4 tells python "Please arrange the JSON neatly, putting each item on its own line and adding four spaces before items inside the object."
#it is only used when converting from a python format to json string format. i.e when using dumps() good when using loads() bad.