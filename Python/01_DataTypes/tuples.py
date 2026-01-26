
# ! A tuple is an ordered collection of values that cannot be changed after creation.

superHeros = ("superman" , "batman" , "spiderman" , "Thor")

# ! Tuples Are Immutable
(hero1 , hero2 ,hero3 , hero4) = superHeros

print(f"{hero1 , hero2 ,hero3 , hero4} These Are the Super Heroes In Marvel And DC")

#@ Membership Testing

print(f"Is Thor is a Super Hero {"Thor" in superHeros}")