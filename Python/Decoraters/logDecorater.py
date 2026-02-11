from functools import wraps

def authorization (func):
    @wraps(func)
    def wrapper(user_Role):
        if(user_Role != "admin"):
            return print("Access Denied!! only admins are Allowed")
        else :
            return func(user_Role)
    return wrapper


@authorization
def access_tea_Inventory(role):
    print(f"Access Granted To Tea Inventory")
    
access_tea_Inventory("admin")