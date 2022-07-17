import asyncio
import time

import requests

loop = asyncio.get_event_loop()


async def post_server():
    url = "https://www.google.com.tw/"
    time.sleep(5)
    print("before res ...")
    res = await loop.run_in_executor(None, requests.get, url)
    print(res)
    print("after res ...")


task = loop.create_task(post_server())

loop.run_until_complete(asyncio.wait(task))


# url = "https://www.google.com.tw/"
# loop = asyncio.get_event_loop()

# start_time = time.time()


# async def send_req(url):
#     t = time.time()
#     print("Send a request at", t - start_time, "seconds.")

#     res = await loop.run_in_executor(None, requests.get, url)

#     t = time.time()
#     print("Receive a response at", t - start_time, "seconds.")


# tasks = []

# for i in range(10):
#     task = loop.create_task(send_req(url))
#     tasks.append(task)

# print(tasks)

# loop.run_until_complete(asyncio.wait(tasks))
