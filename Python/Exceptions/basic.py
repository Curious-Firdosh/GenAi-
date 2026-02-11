chai_menue = {"elaichi" : 10, "masala" : 15, "ginger" : 12, "plain" : 8}

try :
    
    order = input("Which Chai You Want :  ")
    if (chai_menue[order]) :
         print("Chaiii Is Readyyy")
except KeyError:
    print("The Key You Are Looking For is Does not Exist")
    
    
