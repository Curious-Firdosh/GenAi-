
# ! A dictionary in Python is a data type that stores data in key–value pairs.

SuperMan = dict( type ="Superhero" , Power = ["laser" , "superhuman"] , eat = ["KELA" , "sANTRA"] )


# print(f"Superman : {SuperMan.keys()} ")
# print(f"Superman : {SuperMan.values()} ")
# print(f"Superman : {SuperMan.items()} ");



THOR = {}

THOR["type"] = "God Of Thunder"
THOR["father"]  = "odin putra"

# del THOR["father"];

# Marvel = THOR.popitem();
THOR.update(SuperMan)

print(f"Thor Update  : {THOR} ")


