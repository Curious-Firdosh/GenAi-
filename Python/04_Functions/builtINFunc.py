def chaiFlavor (flavor = "masala") :
    """Return  the Flavor Of Chaii"""
    flavor = "ginger"
    return flavor

print(chaiFlavor.__doc__) #! Dunder
print(chaiFlavor())
print(chaiFlavor.__name__) #! Dunder

# @lamda function 

numbers = [1, 2, 3, 4]

squares = list(map(lambda number : number * number , numbers))

print(f"square : {squares}")