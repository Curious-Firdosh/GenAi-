
#! Single Value
def  cal_Amount (cup , amount) : 
   return cup * amount
   
print(f"{cal_Amount(3 , 5)}");

# ! early of Function

def chaiOrder (order) :
   if order <= 0 :
      return print(f"Chai Is Over")
   return print(f"Chai is Ready")

chaiOrder(0);

# ! Handling Multiple Values 

def chaiCost () :
   return 100, 400

cost , sold = chaiCost()

print(f"Cost : {cost} Sold : {sold}")



   