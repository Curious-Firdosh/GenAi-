seat_type = input("Select Seat Type : (sleeper/genral/ac/premium)").lower()

match seat_type :
    case "genral" : 
        print("most cheepest : good for imidiate")
    case "Sleeper" : 
        print("affordable : Reservation")
    case "ac" : 
        print("Goood : good for long distance")
    case "premium" : 
        print("this is best with al things .. but quite expensive")
    case _: 
        print("Select The Seat Pleeese : ")