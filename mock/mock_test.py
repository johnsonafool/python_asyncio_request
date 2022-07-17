import asyncio
import random
import time
from cmath import e
from lib2to3.pytree import type_repr
from unittest import result

import requests

# print(start_t)
# print(type(start_t))


def post_server():
    # try:
    DURATOIN = 5
    POST_TO_SERVER_TIME = 4

    # url = ""
    lists = []
    try:

        # loop = asyncio.get_event_loop()

        looper_IO = True
        while looper_IO == True:

            # async def post_server():
            #     time.sleep(POST_TO_SERVER_TIME)
            #     res

            start_t = time.time()
            time.sleep(DURATOIN)
            stop_t = time.time()
            duration = int(stop_t - start_t)
            if stop_t > start_t:
                print("hi")
                print(duration)
                print(random.randint(1, 30))

                # print(ls)
                # print(type(ls))

                lists.append(duration)
                print(lists)

                del stop_t, start_t
                continue

            looper_IO = False

        return lists

    except:
        print("something went wrong")
        return lists


# post_server()
result = post_server()
print(result)
