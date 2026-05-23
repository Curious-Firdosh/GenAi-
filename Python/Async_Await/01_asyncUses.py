import asyncio

async def Brew ():
    print("Brewing the coffee...")
    await asyncio.sleep(2) # @ in place of calling api  we did it in real world we call api and that will make  the thread to wait
    print("Coffe Is ready")
    

asyncio.run(Brew())