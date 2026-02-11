class chai() :
    temprature = 30
    ingridents = ["elaichi" , "ginger" , "Suger"]

masalaChai = chai()

print(f"masalaChai ingridents -> {masalaChai.ingridents}")
masalaChai.temprature = 40
del masalaChai.temprature
print(f"maslachai after deletion {masalaChai.temprature}") # attrinute shadowing