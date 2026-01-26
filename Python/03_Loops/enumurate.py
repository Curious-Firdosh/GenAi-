superHero = ['Thor' , "Salman" , "Spiderman" , "Batman" , "KIRMADA"]

# ! 1st way 
power = list(enumerate(superHero))
for power in power :
    print(f"{power}")
    
# ! 2nd way 
for idx , hero in enumerate(superHero , 1) :
     print(f"PowerFull {idx}: {hero}")
    