# products = ["Laptop", "Phone", "Tablet"]

# products[0]       → first item
# products[-1]      → last item

# products[1] = ... → change item

# append()          → add to end
# remove(value)     → remove by value
# pop(index)        → remove by index
# pop()             → remove last item

# len()             → number of items
# sort()            → sort list

# products[0:2]     → slicing


# products.append("Tablet")
# products.append("Monitor")

# # products.remove("Phone")
# print(products[0:4])


# products = ["Laptop", "Phone", "Tablet"]

# products.append("Monitor")
# products.remove("Phone")
# products[1] = "iPad"

# print(products)


# prices = [50000, 90000, 70000, 30000]

# print(prices[0])
# print(prices[-1])
# print(len(prices))


"""
One terminology correction:

remove() removes an element by value; pop() removes an element by index.
"""

# prices = [50000, 90000, 70000, 120000, 60000]

# cheap_price = []

# for price in prices:
#     if price <= 80000:
#         cheap_price.append(price)

# print(cheap_price)


products = [
    "ASUS Laptop",
    "iPhone",
    "MacBook Laptop",
    "Samsung Phone",
    "Lenovo Laptop"
]

laptops = []

for product in products:
    if "laptop" in product.lower():
        laptops.append(product)
print(laptops)


prices = [50000, 90000, 70000, 120000]
newlist = []

for price in prices:
    if price > 60000 and price <= 90000:
        newlist.append(price)
        
print(newlist)