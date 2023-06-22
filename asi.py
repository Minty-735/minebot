import asyncio

async def func1():
    print("func1 начинает выполнение")
    await asyncio.sleep(2)
    print("func1 завершил выполнение")

async def func2():
    print("func2 начинает выполнение")
    await asyncio.sleep(1)
    print("func2 завершил выполнение")

async def main():
    task1 = asyncio.create_task(func1())  # создаем задачи
    task2 = asyncio.create_task(func2())

    await task1  # ждем выполнения
    await task2

asyncio.run(main())
