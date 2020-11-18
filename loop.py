import asyncio

global loop
loop = asyncio.get_event_loop()
loop.characters = []