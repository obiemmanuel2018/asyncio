import datetime
import time
import colorama
import asyncio

RUN_ASYNC = True


def main():
    t1 = time.time()

    if RUN_ASYNC:

        loop = asyncio.get_event_loop()
        data = asyncio.Queue()
        tasks = asyncio.gather(
            async_generate_data(5, data,  "task 1"),
            async_generate_data(10, data, 'task 2'),
            async_generate_data(15, data, 'task 3'),
            async_process_data(20, data)
        )
        loop.run_until_complete(tasks)
    else:
        data = []
        generate_data(5, data, "task 1")
        generate_data(10, data, 'task 2')
        generate_data(15, data, 'task 3')
        process_data(20, data)

    t2 = time.time()
    print(colorama.Fore.BLUE + "--Total Time To Completion-- {} seconds".format(t2-t1))


async def async_generate_data(num: int, data: asyncio.Queue, task):

    for idx in range(1, num + 1):
        item = idx * idx
        work = (item, datetime.datetime.now())

        await data.put(work)
        await asyncio.sleep(.5)
        print(colorama.Fore.YELLOW + "--generated data {}....{}".format(idx, task), flush=True)


async def async_process_data(num: int, data: asyncio.Queue):
    processed = 0
    while processed < num:
        processed += 1
        item = await data.get()
        print(colorama.Fore.YELLOW + "--processing item {}".format(item), flush=True)


def generate_data(num: int, data: list, task):

    for idx in range(1, num + 1):
        item = idx * idx
        work = (item, datetime.datetime.now())
        data.append(work)
        time.sleep(.5)
        print(colorama.Fore.YELLOW + "--generated data {}....{}".format(idx, task), flush=True)


def process_data(num: int, data: list):
    processed = 0
    while processed < num:
        processed += 1
        print(colorama.Fore.YELLOW + "--processing item {}".format(data[processed]), flush=True)


if __name__ == "__main__":
    main()
