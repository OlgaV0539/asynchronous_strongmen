import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    for i in range(1,6):
        t = 1 / power
        await asyncio.sleep(t)
        print(f'Силач {name} поднял {i} шар.')

    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    strongman_tasks = [
        start_strongman('Pasha', 3),
        start_strongman('Denis', 4),
        start_strongman('Apollon', 5)
    ]
    await asyncio.gather(*strongman_tasks)


if __name__ == '__main__':
    asyncio.run(start_tournament())
