import time
import asyncio


async def job(t):
    print('start job', t)
    # time.sleep(t)
    await asyncio.sleep(t)
    print("job", t)


async def main(loop):
    # [job(t) for t in range(1,4)]
    tasks = [loop.create_task(job(t)) for t in range(1,4)]
    await asyncio.wait(tasks)


t = time.time()
# main()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
print("No Asyncio take times:", time.time() - t)

