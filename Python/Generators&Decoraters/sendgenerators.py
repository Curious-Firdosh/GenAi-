def chai_coustmer():
    print("Helllo Whatsapp")
    order = yield
    while True :
        print(f"Preparing {order}")
        order = yield # it stoped the execution and waiting fro another value 
        print(f"Prepared {order}")
        
        
firdosh = chai_coustmer() 

next(firdosh)

firdosh.send("Lemon Teaaa ")