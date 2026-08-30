#21
# userQuery = input("Search..." )

# print(type(userQuery))
# normalizedQuery = userQuery.strip().lower()


# if "laptop" in normalizedQuery : 
#     print("Searching Laptop....")
# elif "phone" in normalizedQuery : 
#     print("Searching phones")
# else : 
#     print("Searching all products")
    
#22

# product_name = "ASUS TUF Gaming lAPToP"
# normalized_name = product_name.lower()

# product_price = 75000


# if "laptop" in normalized_name and product_price <= 80000:
#     print("Product matches")
# else:
#     print("Product does not match")
    
# # 23 

# age = input ("Enter age :")

# new_age = int(age)
# # here the age is string beouse whatever the value we take from the input is a string so we have to conerver it to desried data type then use it in th code

# if new_age >= 18:
#     print("Adult")
# else:
#     print("Minor")
    

# 24

query = input("Search product: ")
max_price = input("Maximum price: ")

normalizedQuery = query.strip().lower()
new_Price = int(max_price)

if "laptop" in normalizedQuery and new_Price <= 80000:
    print("Show laptop results")
else:
    print("No matching results")