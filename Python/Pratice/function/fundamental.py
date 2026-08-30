# def calculate_total(price , quantity ):
#      return price * quantity
 
# result = calculate_total(2 , 389)

# print(result)



# product = {
#     "name": "ASUS TUF",
#     "category": "laptop"
# }

# def is_laptop(product):
#      return product["category"] == "laptop"
 
# print(is_laptop(product))


# def user(name , age , department):
#     print(name , age , department)
    

# user(23 , "hero" , "cse")


# def create_product ( name , price , category = "unknown"):
#     return {
#         "name" : name,
#         "price" : price,
#         "category" : category
#     }
    
    
# laptop = create_product(name="AssusTuff" ,price= 300000 , category="laptop")

# print(laptop)


products = [
    {"name": "ASUS TUF Laptop", "price": 75000},
    {"name": "MacBook Air", "price": 90000},
    {"name": "Lenovo Laptop", "price": 60000}
]


# def filter_prodcuts(products , maxPrice):
    
#     result = []
    
#     for product in products:
#         if product["price"] <= maxPrice:
#             result.append(product)
    
#     return result


# response = filter_prodcuts(products=products , maxPrice= 75000)

# print(response)


def calculate_discount(price , discount = 10):
    return price - ( price * discount / 100)

# discounted_price = calculate_discount(1000)

# print(discounted_price)


def get_price():
    price = 50000
    return price

# result = get_price()

# print(result)



def search_products (products , query:str, max_price):
    
    results = [];
    for product in products:
        if query.lower() in product["name"].lower() and product["price"] <= max_price:
            results.append(product)
    return results
           

# result = search_products(products , "laptop" , 1000000) 

# print(result)

# def greet(name="Firdosh", age):
#     return f"{name} is {age}"


# greet(name="khan", age=34)


def add(a, b):
    return a + b
