class tshirt :
    origin = "M2 Fashion"


tshirt.compney = "Fastract"

# print(tshirt.origin) # M2 Fashion
# print(tshirt.__name__) # tShirt
# print(tshirt.compney) # Fastract 


# ! Creating Objects from Chaiii

oversizedTshirt = tshirt();

oversizedTshirt.size = "2xl"
print(oversizedTshirt.origin)
print(oversizedTshirt.compney)
print(oversizedTshirt.size)
print(oversizedTshirt)