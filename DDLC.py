import asyncio, chrs, globalVars, os, sqlite3, subprocess, sys, threading, traceback
from bot import Character

def run_chr(chr):
    try:
        asyncio.set_event_loop(asyncio.new_event_loop())
        chr = chrs.loadChr(chr[:-3])
        character = Character(chr=chr)
        character.run(chr["character"].token)
    except Exception as error:
        print(f"Could not run {chr['name']}.py!")
        print(traceback.format_exc)
        print(error)

#region global varianle settings
globalVars.setInteractions()
#endregion

characters =  chrs.getCharacters()

for chr in [file for file in os.listdir('./characters') if file.endswith('.py')]:
    threading.Thread(target=run_chr, args=(chr,)).start()
    print(f'{chr} has successfully been recognized!')

#input stuff here
while True:
    input_value = str(input())
    #do things with the input here