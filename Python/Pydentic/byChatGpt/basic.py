from pydantic import BaseModel , Field
from typing import Optional
# class User (BaseModel):
#     name : str
#     email : str
#     age: int
#     acive : bool
    
    
# user = User(
#     age="22",
#     name="Firdosh",
#     email="firdosh@example.com",
#     acive=False
# )

# print(user)
    
# print(user.age)
# print(type(user.age))
# print(user)
# print(user.model_dump_json())



# # ! if data comnes form api you coudl validate it 

# data = {
#     "name": "Firdosh",
#     "email": "firdosh@example.com",
#     "age": "25",
#     "acive": True
# }


# user = User.model_validate(data)

# print(user)

# ! Optional || defautl || required 

# class Product (BaseModel):
#     name : str
#     slug : Optional[str] = None 
#     price : int = 999
#     stock : Optional[int] = 30
    
# laptop = Product (
#         name="ASUS TUF",
# )

# print(laptop) 


# ! Field 


class Car(BaseModel):
    name : str = Field(min_length=3 , max_length=25)
    price : int = Field(gt=0)
    stock : int = Field(ge=0)


scorpio = Car(
    name="S11",
    price= 3,
    stock=3,
    compney="Mahindra"
)


print(scorpio.model_dump())