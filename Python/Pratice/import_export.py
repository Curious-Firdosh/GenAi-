from try_except.intial import validate_price
from function.fundamental import search_products
from function.fundamental import add


product = search_products(products = [
    {"name": "ASUS TUF Laptop", "price": 75000},
    {"name": "MacBook Air", "price": 90000},
    {"name": "Lenovo Laptop", "price": 60000}
], query="macbook" , max_price= 800000
)

cal = add(2,5)

print(cal)
print(product)