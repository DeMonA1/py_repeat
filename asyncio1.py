import asyncio


async def wicked():
    print('Surrender, ')
    await asyncio.sleep(2)
    print('Dorothy!')
    
asyncio.run(wicked())


async def say(phrase, seconds):
    print(phrase)
    await asyncio.sleep(seconds)
    
async def wicked():
    task_1 = asyncio.create_task(say('Surrender,', 2))
    task_2 = asyncio.create_task(say('Dorothy!', 0))
    await task_1
    await task_2
    
asyncio.run(wicked())