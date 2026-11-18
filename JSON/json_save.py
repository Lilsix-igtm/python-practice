import json

#dump() is a method in json that stores data permanently on the computer unlike dumps() that stores it temporarily.
order = {
    'Customer': 'Ada',
    'Product': 'Vitamin C serum',
    'Quantity': 2,
    'price': 15000
}

with open('json_order.json', 'w') as file:
    json.dump(order, file, indent=4)

#indent=4 tells python "Please arrange the JSON neatly, putting each item on its own line and adding four spaces before items inside the object."
#it is only used when converting from a python format to json string format. i.e when using dumps() good when using loads() bad.


# Reading JSON files using json.load()
# Imagine Ada's order has already been saved in order.json.
# Tomorrow, you open your online shop's backend again. You want Python to retrieve Ada's order so you can see what she purchased.
# How do we do that?
# We use json.load().

with open('json_order.json', 'r') as file:
    order = json.load(file,)
print(order)