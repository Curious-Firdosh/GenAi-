
def makeChai (tea , milk , suger) :
    print(tea , milk , suger);

makeChai("balckTea" , "nott" , 3) #@ Positional -- i know the postion of the argumnet that the blacKTEA = tea , milk = no 

makeChai(tea="MilkTea" , milk="yess" , suger="9") #! Keywords

def making_another_Tea (*ingredeients, **extraa) :
    print(f"Ingredents: {ingredeients}")
    print(f"Extrass: {extraa}")
    
making_another_Tea( "tea", "coffee" , "masala" , "masala");
making_another_Tea(sweet = "5" , masala ="maggie")

