import asyncio
import time


async def say_after(delay, what):
    # time.sleep(delay)
    await asyncio.sleep(delay)
    print(what)


async def main():
    t1 = time.time()
    task1 = asyncio.create_task(say_after(4, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))
    print(f"started at {t1}")
    await task1
    await task2
    print(f"finished at {time.time() - t1}")


if __name__ == "__main__":
    asyncio.run(main())