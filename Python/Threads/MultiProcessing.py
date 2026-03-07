from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start of {name} chai Making")
    time.sleep(3)
    print(f"End of {name} chai Making")
  
if __name__ == "__main__":
    chaiMakers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i+1}",))  # ← BUG FIXED: args needs () not {}
        for i in range(3)
    ]
    
    for p in chaiMakers:
        p.start()   # all 3 processes start almost simultaneously

    for p in chaiMakers:
        p.join()    # wait for all to finish
        
    print("All Chai Served!")

# > ⚠️ **Bug you had:** `args={f"Chai Makers #{i+1}"}` — curly braces `{}` make a **set**, not a tuple. Should be `args=(value,)` with parentheses and a comma.

# **What happens here:**
# ```
# Start of Chai Maker #1 chai Making  ┐
# Start of Chai Maker #2 chai Making  ├── All start at same time (TRUE parallelism)
# Start of Chai Maker #3 chai Making  ┘
# (3 seconds later...)
# End of Chai Maker #1 chai Making
# End of Chai Maker #2 chai Making
# End of Chai Maker #3 chai Making
# ```

# ---

# ## When to Use What? (Interview Answer)
# ```
# Task is waiting for something?       → Use THREADING
# (API calls, file reading, database)

# Task is heavy calculation?           → Use MULTIPROCESSING  
# (data processing, image/video work)

# Need simple async waiting?           → Use ASYNCIO (async/await)