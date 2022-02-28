#!/usr/bin/env python

import asyncio, websockets

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with websockets.serve(echo, "0.0.0.0", 8765):
        await asyncio.Future()

asyncio.run(main())
