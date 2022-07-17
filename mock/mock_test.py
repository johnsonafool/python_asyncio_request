import asyncio
import random
import time
from lib2to3.pytree import type_repr
from turtle import pos
from unittest import result

import requests

# print(start_t)
# print(type(start_t))

loop = asyncio.get_event_loop()


def post_server():

    DURATOIN = 3
    POST_TO_SERVER_TIME = 5

    return_lists = []

    try:

        async def post_server():
            url = "https://www.google.com.tw/"
            print("before res ...")
            res = await loop.run_in_executor(None, requests.get, url)
            print(res)

        tasks = []
        lists = []
        looper_IO = True
        while looper_IO == True:

            start_t = time.time()
            time.sleep(DURATOIN)
            stop_t = time.time()
            if stop_t > start_t:  # raw duration will be more than excactly 5s
                duration = stop_t - start_t

                # duration = int(stop_t - start_t)
                lists.append(duration)
                # print(f"hi\t{duration}\t{lists}\t{len(lists)}")

                del stop_t, start_t

                print("hi")

                print(lists)
                if len(lists) > 3:  # clean the lists and send data to server
                    lists.clear()

                task = loop.create_task(post_server())
                tasks.append(task)

                loop.run_until_complete(asyncio.wait(tasks))

            # looper_IO = False

        return_lists = lists
        return return_lists

    except:
        print("end up while looping")
        return lists


# post_server()
result = post_server()
print(result)
