class InvalidChaiiError(Exception): pass

def bill(flavor , cups):
    menu = {"masala" : 40 , "ginger" : 20}
    try :
        if flavor not in menu :
            raise InvalidChaiiError("That flavor is not Available")
        if not isinstance(cups , int) :
            raise TypeError("Cups Always INTEGER")
        total = menu[flavor] * cups
        print(f"YouR Total bILL is {total}")
    except Exception as e :
        print(f"Error : " , e);
    finally :
        print("Thanks For Ordering Chaiii")
        

bill("ginger" , 2)
bill("mint" , 3)
bill("ginger" , "twoo")
bill("mint"*4  , "8")


    