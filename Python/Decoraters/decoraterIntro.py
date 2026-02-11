def my_decorater(func):
    def wrapper():
        print("User ek Bahut Achha Aadmi  h before calling")
        func()
        print("User is very Good Man After intializing")
    return wrapper


@my_decorater
def whats_Your_Name():
    print ("User Is Firdosh Khan")
    
whats_Your_Name()