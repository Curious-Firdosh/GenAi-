def brew_Chai (flavor) :
    if flavor not in ["Masala" , "MILK" , "elaichi"] :
        raise ValueError("UnSupported Chai ..")
    print("Brewing Chaiii......")


brew_Chai("greentea")