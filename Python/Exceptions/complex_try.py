def serv_chai (flavor): 
    
    try :
        print("Preparing Chaiii....")
        if flavor == "unknown" :
            raise ValueError (f"{flavor}.. Ook I dont Know That Flavor");
    except ValueError as e:
        print("Error" , e)
    else : 
        print(F"{flavor} Chaii Is Served ....")
    finally : 
        print("Next customer Please")
    

serv_chai("aaam chaii")
serv_chai("unknown")
    