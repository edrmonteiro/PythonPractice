
import asyncio

def main():
    print('main')

async def asyncFunc1():
    print('asyncFunc1')

async def asyncFunc2(text):
    print(text)
    await asyncFunc1()
    await asyncio.sleep(10)


main()
asyncio.run(asyncFunc1())
asyncio.run(asyncFunc2("test"))

other()

main()


