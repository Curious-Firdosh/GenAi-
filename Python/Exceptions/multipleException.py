def serve_Chai (item , Quantity) :
    
    try : 
        price = {"masala" : 20}[item]
        cost = price * Quantity
        print(f"Total Cost is {cost}")
    except KeyError:
        print("Sorry That Chai Is Not In The Menue")
    except TypeError:
        print ("Sorry Quentity Must Be In Numbers")
    
serve_Chai("masala" , 2)
pass
serve_Chai("Ginger" ,2)
pass
serve_Chai("masala" ,"two") # THE CONCEPT OF OPERATOR OVERLOADING
