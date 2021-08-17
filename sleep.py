import asyncio 

async def task1():
    print('Send first email')
    asyncio.create_task(task2())
    await asyncio.sleep(5)
    print('first email reply')

async def task2():
    print('Send second Email')
    asyncio.create_task(task3())
    await asyncio.sleep(2)
    print('Second email reply')

async def task3():
    print('send terza email')
    await asyncio.sleep(1)
    print('terza email reply')

asyncio.run(task1())