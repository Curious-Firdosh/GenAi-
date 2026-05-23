import asyncio
import time

async def Brewing (name) :
    print(f'Brewing your {name}')
    await asyncio.sleep(3) #@ we wrote it and called the function 3 times and all will wait for 3 seconds but they will not wait for each other they will run concurrently and after 3 seconds all will be ready at the same time
    await time.sleep(3) #


async def main():
    await asyncio.gather(
        Brewing("Ginger Tea"),
        Brewing("Coffee"),
        Brewing("Masala Tea"),
    )
    
asyncio.run(main())