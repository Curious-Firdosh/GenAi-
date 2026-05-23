# class Factory:
#     name ="Factory_Name" #attribute
    
#     def ProductQuality (self):
#         print("Product is in Good Quality") # method 
        
# print("Hello I m getting Initialized")
# print(Factory.name)
# # print(Factory.ProductQuality())



# # ! Class and object 

# class SuperHero :
#     def __init__(self ,Power , Team , age ):
#         self.Power = Power
#         self.Team = Team
#         self.age = age

#     def ShowDetails (self):
#         print(f"SuperHero {self.Power ,self.age ,self.Team}")
        
# Thor = SuperHero("Thunder", "Avengers" , 1500)
# Thor.ShowDetails()



# # ! Type class methods and attributes

# class Animal: 
    
#     # @ Types of Attributes:
#     Animal_Type = "herbivorus" #@ Class attribute
    
#     def __init__(self , name , food: str, Venomus: str ,age : int ):  # @ instance attributes
#             self.name = name
#             self.food = food
#             self.Venomus = Venomus
#             self.age = age
       
#     # @ Types of Methods:
    
#     def Sound(self , voice:str): # @ instance method
#         self.voice = voice
#         print(f"{self.name} sounds like {self.voice}")

#     @classmethod
#     def class_method (cls):
#         print("that is clss method")
        
#     @staticmethod
#     def static_Method () :
#         print("Hlllo static Method Called")
    


# Dog = Animal(456 , 22 , 15 , "not disclosed")
# Dog.Sound(32)

# 4 Pillers Of the Oops 

class Car : 

    def __init__(self , name , color):
        self.name = name
        self.color = color
        
    def ShowDetails (self):
        print(f"The  {self.name} in {self.color} is Very Populer")

class Bike(Car):
    
    def __init__ (self ,name , color, Wheel:int , Weight):
        super().__init__(name , color)
        self.Wheel = Wheel
        self.Weight = Weight
    
    def ShowDetails(self):
        print(f"{self.name} is very Populer in {self.color} it is {self.Wheel} and its weight is {self.Weight}")
    
   

Splender = Bike("Splender++" ,"Blue" , "2wheeler" , "80Kg")
Splender.ShowDetails()