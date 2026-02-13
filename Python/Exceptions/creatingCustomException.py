class outofIngredientError(Exception) :
    pass

def MakeChai(milk , suger) :
    if milk == 0 or suger == 0 :
        raise outofIngredientError("Ingridients are not Available")
    print("Making Chaiii Plzz Wait")
    
MakeChai(2 , 1);
MakeChai(0 ,1 );