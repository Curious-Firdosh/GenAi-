


# try:
#     number = int("100")
#     print(number)
# except ValueError:
#      print("invalid")

def convert_price (value):
    try:
        number = int(value)
        return number;
    except ValueError:
        return None
    

def validate_price (price):
    if price <= 0:
        raise ValueError("Price must be greater than zero")
    
    return "Allowed"

validate_price(20)
  
        
        
   
    