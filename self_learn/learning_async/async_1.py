import time, asyncio, aiohttp

'''synchronous'''

def synchronous_async():
    #a co-routine
    async def add(x : int, y:int) -> int:
        return x + y

    loop = asyncio.get_event_loop()

    result1 = loop.run_until_complete(add(1, 2))
    result2 = loop.run_until_complete(add(2, 4))


    results = loop.run_until_complete()

'''asynchronous loop'''

def old_asynchronous():
    async def add(x : int , y : int) -> int:
        return x + y

    loop = asyncio.get_event_loop()

    async def get_results():
        result1 = await add(3, 4)
        result2 = await add(1, 2)

        print(result1, result2)
        loop.stop()

    loop.create_task(get_results())

    try:
        loop.run_forever()
    finally:
        loop.close()

'''current asynchronous'''

def current_async():
    async def add(x:int, y:int) -> int:
        return x + y

    async def get_results():

        result1 = await add(1, 2)
        result2 = await add(3, 4)
        result3 = await add(4, 5)
        result4 = await add(5, 6)
        result5 = await add(6, 7)

        print(result1, result2, result3, result4, result5)

    results = asyncio.run(get_results())


'''understanding concurency'''

def manual_coroutine():
    async def add_fast(x:int, y:int):
        print('Starting fast add:')
        await asyncio.sleep(3)
        print('Ready for fast add:')
        return x + y

    async def add_slow(x:int, y:int):
        print('Starting slow add:')
        await asyncio.sleep(5)
        print('Ready for slow add:')
        return x + y

    async def get_tasks():
        task1 = asyncio.create_task(add_slow(5, 5))
        task2 =  asyncio.create_task(add_fast(6, 6))

        print(await task1, await task2)

    asyncio.run(get_tasks())


'''using asyncio.gather() to dynamically go through the coroutines'''
def using_gather():

    async def add(x:int, y:int):
        await asyncio.sleep(3) #even with this .sleep(), because the tasks are running asynchronously, they will be printed at the same time
        return x + y

    async def make_task(add_list):

        cors = [add(x, y) for x,y in add_list] #runs through add_list and creates an object containing the add(x, y) function, making them 'coroutines'
        
        results = await asyncio.gather(*cors) #waits for the functions in the coroutines to complete
        
        print(results)

    asyncio.run(make_task([(1, 1), (2, 2), (3, 3), (4, 4)])) #will print a list containing 2, 4, 6 and 8


'''using as_completed instead of .gather(), to get items as they are returned instead of waiting for everything to return'''

async def add_fast(x:int, y:int):
    print('Starting fast add:')
    await asyncio.sleep(3)
    print('Ready for fast add:')
    return x + y

async def add_slow(x:int, y:int):
    print('Starting slow add:')
    await asyncio.sleep(5)
    print('Ready for slow add:')
    return x + y

async def get_results():
    list = [(1, 1), (2, 2), (3, 3), (4, 4)]

    cors = [add_fast(x, y) for x, y in list] 
    
    for result in asyncio.as_completed(cors): #even with this, because they were scheduled at the same time, they finish their awaits at the same time.
        print(await result)
    
asyncio.run(get_results())