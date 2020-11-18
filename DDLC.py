import asyncio, discord, json, os
from bot import Character
from loop import loop

for chrfile in [file for file in os.listdir('./characters') if file.endswith('.chr')]:

    chrjson = json.loads(open(f"characters/{chrfile}", "r").read())
    tokensjson = json.loads(open(f"tokens.json", "r").read())
    loop.characters.append(Character(chrjson))
    loop.create_task(loop.characters[-1].start(tokensjson[chrfile[:-4]]))

loop.run_forever()