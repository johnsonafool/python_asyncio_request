import asyncio
import random
import time
from unittest import result

import requests

# print(start_t)
# print(type(start_t))


def post_server():
    DURATOIN = 5
    POST_TO_SERVER_TIME = 4

    # url = ""

    loop = asyncio.get_event_loop()

    looper_IO = True
    while looper_IO == True:

        # async def post_server():
        #     time.sleep(POST_TO_SERVER_TIME)
        #     res

        lists = []

        def gen_data():
            start_t = time.time()
            time.sleep(DURATOIN)
            stop_t = time.time()
            duration = stop_t - start_t
            if stop_t > start_t:
                print("hi")
                # print(duration)
                # print(random.randint(30))
                ls = f"{duration} | {random.randint(30)}"

                lists.append(ls)

                del stop_t, start_t
                continue

        gen_data()
        looper_IO = False

    return lists


result = post_server()
print(result)
