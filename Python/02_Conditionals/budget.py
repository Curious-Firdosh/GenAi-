
# price = input("Enter Amount : ")

# if int(price) <= 80000 :
#     print("Within Budget")
# else:
#     print("Paisa Nhi Hai Bhaiii")


user_input_query = input("Enter Product")
product_price = 60000

query = user_input_query.strip().lower()

if "laptop" in query and product_price <= 80000 :
    print("available")
else:
  print("NOT aVALABLE")