import asyncio, chrs, discord, importlib, os, re, rstr, sqlite3, sre_yield, traceback
from discord.ext import commands

#character class
class Character(commands.AutoShardedBot):

    def __init__(self, chr):
        self.name = chr["name"]
        self.character = chr["character"]
        self.globalConnection = sqlite3.connect('global.db')
        self.globalCursor = self.globalConnection.cursor()
        self.chrs = chrs.getCharacters()
        super().__init__(command_prefix=sre_yield.AllStrings(self.character.prefix), status=discord.Status.idle, activity=discord.Game(name="Starting Up..."))
        for file in os.listdir("commands"):
            if file.endswith(".py"):
                name = file[:-3]
                try:
                    module = importlib.import_module(f"commands.{name}")
                    if hasattr(module, "check") and getattr(module, "check")(self.character):
                        self.load_extension(f"commands.{name}")
                        print(f"[{self.name}] Loaded command: {name}")
                    elif not hasattr(module, "check"):
                        self.load_extension(f"commands.{name}")
                        print(f"[{self.name}] Loaded command: {name}")
                except (discord.ClientException, ModuleNotFoundError):
                    print(f'[{self.name}] Failed to load command: {name}')
                    print(traceback.format_exc())

        for file in os.listdir(f"events"):
            if file.endswith(".py"):
                name = file[:-3]
                try:
                    self.load_extension(f"events.{name}")
                    print(f"[{self.name}] Loaded event: {name}")
                except (discord.ClientException, ModuleNotFoundError):
                    print(f'[{self.name}] Failed to load event: {name}')
                    print(traceback.format_exc())
        

    async def on_ready(self):
        print(f'Logged on as {self.user} with {self.name}.chr!')
        self.loop.create_task(self.status_task())

    async def on_disconnect(self):
        print(f'{self.user} has disconnected from {self.name}.chr!')

    async def on_resumed(self):
        print(f'{self.user} has resumed back to {self.name}.chr!')

    async def status_task(self):
        while not self.is_closed():
            games = self.character.playing()
            for game in games:
                await self.change_presence(activity=discord.Game(name=rstr.xeger(game)))
                await asyncio.sleep(900)

    async def send(self, sender, message, embed=None):
        try:
            async with sender.message.channel.typing():
                await asyncio.sleep(0.4)
                await sender.send(message, embed=embed)
        except:
            async with sender.typing():
                await asyncio.sleep(0.4)
                await sender.send(message, embed=embed)

    async def detectEveryoneMention(self, sender):
        if re.search("@(everyone|here)",sender.message.content):
            await self.send(sender, self.character.everyone())
            return True
        return False