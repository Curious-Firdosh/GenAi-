# Q11 What are the outputs?

text = "Python"

print( text[0]) # P
print ( text[-1]) # n
print(len(text)) # 6



# Q12 What are the outputs?

text = "  hello world  "

print( len(text)) # 15 that will count the length of the string considering spaces at the last and first
print( len(text.strip())) # 11 that used the strip function and the will remove the spaces  from first and last


# 13 What does this print?

text = "Gaming Laptop"

print("laptop" in  text) # false
print( "laptop" in text.lower()) # true


# 14

text = "HELLO"

text.lower()

print(text) # that will print the HELLO Becouse every string method return new string so it used thhe lower but never printed that


# Q15 — Coding 

query = "   GAMING LAPTOP ASUS   "
removed = query.strip()
newQuery = removed.lower()

print( newQuery)


# 16 

name = "Firdosh"
age = 21
goal = "AI Engineer"

print(f"my name is {name} , i am {age} old and i want to become and {goal}")


