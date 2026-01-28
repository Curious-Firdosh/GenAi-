
#! Expressions for item in Itreble if Condition

superHeroes = [
    "Spider-Man",
    "Iron Man",
    "Hulk",
    "Thor",
    "Captain America",
    "Black Widow",
    "Hawkeye",
    "Doctor Strange",
    "Black Panther",
    "Captain Marvel"
]


# @  as Usual Method
filteredHeros1 = []
for hero in superHeroes :
    if("C" in hero) :
        filteredHeros1.append(hero)
        

# ! and the comprehensive way 
filteredHeros2 = [hero  for hero in superHeroes if "C" in hero]

print(f"Heroes {filteredHeros2}" )