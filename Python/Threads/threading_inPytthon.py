import threading
import time

def take_Orders():
    for i in range(1,4):
        print(f"Taking Order FROM {i}")
        time.sleep(1)
        
def brew_Chai():
    for i in range(1,4):
        print(f"Brewing Chaiii For {i}")
        time.sleep()
        
        
# creating threading 

order_thread = threading.Thread(target=take_Orders)
brew_thread = threading.Thread(target=brew_Chai)
        
order_thread.start()
brew_thread.start()

order_thread.join()
brew_thread.join()
        