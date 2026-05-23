from pydentic import BaseModel

class User(BaseModel):
    id: int
    name : str
    is_active : bool
    

input_data = { 'id' : 101 , 'name': "Firdosh" ,"is_active" : False }

user = User(**input_data)



class Product(BaseModel):
    id : int
    name : str
    price : float
    type : str = "Home Use"
    in_stock : bool = False
    
    
product1 = Product(id = "24" , name = "Keyboard" , price=99 ,  type = "electronics" ,in_stock = True)
product2= Product(id = "29" , name = "Keyboard" , price=10000)

print(product2)
    