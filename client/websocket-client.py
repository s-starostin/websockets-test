#!/usr/bin/env python

import os, asyncio, websockets, datetime, random
from contextlib import suppress

async def hello():
    while True:
        async with websockets.connect(os.environ.get("SERVER_URL", "ws://localhost:8765")) as websocket:
            now = datetime.datetime.utcnow().isoformat() + 'Z'
            await websocket.send(now)
            print("> {}".format(now), flush=True)
            response = await websocket.recv()
            print("< {}".format(response), flush=True)
        await asyncio.sleep(random.randint(1,5))

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    loop.run_until_complete(hello())
finally:
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()
