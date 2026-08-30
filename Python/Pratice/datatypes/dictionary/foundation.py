


# # ! it is also Mutable like the Lists 

# products["ram"]
# products["price"] = 90000
# products["milage"] = "2hour" # !If "stock" doesn't exist → adds it. If "stock" already exists → updates it.

# products.keys();
# products.values()
# products.items(); # it shows key value pair
# products.get("compney" , "Apple")
# products.get("compney" , "Apple")


# print(products["price"])


# # prices = {}
# # for key, value in products.items():
# #     if key == "price" and value >= 40000:
# #         prices[key] = value

# # print(prices)



# phone = {
#     "name" : "iphone",
#     "price" : 34000,
#     "stock" : 35
# }

# for key, value in phone.items():
#     print(key, value)


# product = {
#     "name": "iPhone 16",
#     "price": 70000
# }

# product["price"] = 65000
# product["stock"] = 25

# print(product)

# products = [
#     {"name": "ASUS TUF", "price": 75000, "category": "laptop"},
#     {"name": "iPhone 16", "price": 70000, "category": "phone"},
#     {"name": "MacBook Air", "price": 90000, "category": "laptop"},
#     {"name": "Lenovo IdeaPad", "price": 60000, "category": "laptop"}
# ]


# for product in products : 
#     if "laptop" in product["category"]:
#         print(product["name"])
        
# # for product in products : 
# #     if  product["category"] == "laptop":
# #         print(product["name"])
    
# for product in products:
#     if "laptop" in product["category"] and product["price"] <= 80000:
#         print(product);

        


# products = [
#     {
#         "name": "ASUS TUF",
#         "details": {
#             "price": 75000,
#             "category": "laptop"
#         }
#     },
#     {
#         "name": "iPhone 16",
#         "details": {
#             "price": 70000,
#             "category": "phone"
#         }
#     },
#     {
#         "name": "Lenovo IdeaPad",
#         "details": {
#             "price": 60000,
#             "category": "laptop"
#         }
#     }
# ]

# laptop = {
#     "name" :"macbook",
#     "price" : 70000,
#     "ram" : "32GB"
# }

# print("price" in laptop)

# for product in products:
#     if product["details"]["category"] == "laptop" and product["details"]["price"] <= 80000 :
#         print(product["name"])
        

products = [
    {"name": "ASUS TUF", "price": 75000, "category": "laptop"},
    {"name": "iPhone 16", "price": 70000, "category": "phone"},
    {"name": "MacBook Air", "price": 90000, "category": "laptop"}
]


for product in products:
    if product["category"] == "laptop" and product["price"] <= 80000:
        print(product["name"])
        
        