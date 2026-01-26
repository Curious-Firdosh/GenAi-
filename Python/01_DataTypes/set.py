
# ! A set is an unordered collection of unique values with no duplicates

actors = {"salman" , "shahrukh" , "Aamir" , "Prabhas" , "Vijay", "Vijay"} #@ does not include the duplicate value
MarriedActors = {"kartik" , "Vignesh" , "Atlee" , "Allu" , "salman" , "Vijay"};

allActors = actors | MarriedActors; # ! Union
superStars = actors & MarriedActors; #! Intersection


print(f"All Actors {actors}" )