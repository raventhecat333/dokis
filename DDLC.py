import asyncio, discord, json, os
from bot import Character

loop = asyncio.get_event_loop()

for chrfile in [file for file in os.listdir('./characters') if file.endswith('.chr')]:
    
    chrjson = json.loads(open(f"characters/{chrfile}", "r").read())
    loop.create_task(Character(chrjson).start(chrjson["about"]["token"]))

loop.run_forever()