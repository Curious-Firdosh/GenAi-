# 17

price = 70000

if price <= 80000:
     print("Within budget") # that will be printed
else:
     print("budget se baher")


# 18 

marks = 85

if marks >= 90:
    print("A")
elif marks >= 60 : 
    print("B") # thta will be printed
else : 
    print("Chutiya hai APPKA LADKAA")
    

# 19 
 
 
age = 25 

if age >= 18: 
    print("adult")
elif age >= 21:
    print("older") # that will be printed because  the only one cndtion is going to be true so if the age is greater that 21 then he id older and exist the execution 
    
else : 
    print("minor")
    
# 20 

age = 16
has_permisson = True

if  age >= 18 and has_permisson :
    print("Allowed")
else: 
    print("Bhaag") # it is printed becouse the and operator ask that both condtion have to be true but here is only on con stion is true



# 21 

is_admin = False
is_owner = True

if is_admin or is_owner:
    print("Access granted") # that will be printed becoue or operator check both the conditn if one of that is true thta is allowed
else:
    print("Access denied")


