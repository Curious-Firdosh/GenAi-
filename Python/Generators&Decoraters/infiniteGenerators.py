def infinite_chaii(): 
    count = 1;
    while  True:
        yield f"refill Count {count}"
        count += 1 
      

# @ THat i am making if i try to run that refil function without the generator yield it will become very dangerous
user1 = infinite_chaii()
user2 = infinite_chaii()

for _ in  range(4):
    print(next(user1))
    
for _ in range(2) :
    print(next(user2))