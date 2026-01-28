superHeroes = [
   "Black Widow" ,
    "Iron Man",
    "Hulk",
    "Thor",
   "Iron Man",
    "Black Widow",
   "Thor",
    "Doctor Strange",
    "Black Panther",
    "Doctor Strange",
]

#! Find Unique Superheros

uniqueList = {hero for hero in superHeroes if superHeroes.count(hero) == 2}

#* print(f"{uniqueList}");


vilans = {
    "Loki" : ["Asgard" , "Earth",  "Jotunheim"],
    "Thanos" : ["Titan" , "Earth" , "Knowhere"],
    "Green Goblin" : ["Earth" , "knowhere",  "Oscorp"],
    "Magneto" : ["invisible" , "Asgard" , "Jotunheim"],
}

# @ what ever value you are Returning that come in the first place.. like what you want to return 
uniquePlaces = {place for villan in vilans.values() for place in villan}

print(f"UniquePlaces : {uniquePlaces}")