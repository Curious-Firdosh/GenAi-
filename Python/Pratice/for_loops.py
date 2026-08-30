#1
# products = ["Laptop", "Phone", "Tablet", "Monitor"]

# for product in products:
#     print(product)
# """
# Laptop
# Phone
# Tablet
# Monitor

# """

#2
# numbers = [10, 20, 30, 40, 50]

# for number in numbers:
#     if number >= 25:
#         print(number)

#3

products = [
    "ASUS Laptop",
    "iPhone 16",
    "Samsung Laptop",
    "iPad",
    "Lenovo Laptop"
]


for product in products:
    if "laptop" in product.lower():
        print(product)



prices = [50000, 90000, 70000, 120000, 65000]

for price in prices:
    if price <= 80000:
        print(price)