import asyncio, discord, importlib, json, os, re, rstr, sqlite3, sre_yield, traceback
from discord.ext import commands

#character class
class Character(commands.AutoShardedBot):

    def __init__(self, chrfile):

        self.Config = json.loads(open("config.json", "r").read())
        self.ChrFile = chrfile
        
        super().__init__(command_prefix=sre_yield.AllStrings(self.ChrFile["about"]["prefix"]), status=discord.Status.idle, activity=discord.Game(name="Starting Up..."), owner_ids=self.Config["perms"]["root"])

        self.load_extension("jishaku")

        for file in os.listdir("commands"):

            if file.endswith(".py"):

                name = file[:-3]

                try:

                    module = importlib.import_module(f"commands.{name}")

                    if hasattr(module, "check") and not getattr(module, "check")(self.character):

                        continue

                    self.load_extension(f"commands.{name}")
                    print(f'[{self.ChrFile["about"]["name"]}] Loaded command: {name}')

                except (discord.ClientException, ModuleNotFoundError):

                    print(f'[{self.ChrFile["about"]["name"]}] Failed to load command: {name}')
                    print(traceback.format_exc())

        for file in os.listdir(f"events"):

            if file.endswith(".py"):

                name = file[:-3]

                try:

                    self.load_extension(f"events.{name}")
                    print(f'[{self.ChrFile["about"]["name"]}] Loaded event: {name}')

                except (discord.ClientException, ModuleNotFoundError):

                    print(f'[{self.ChrFile["about"]["name"]}] Failed to load event: {name}')
                    print(traceback.format_exc())

    def GetChrFile(self, fileName):

        with open(f'characters/{fileName.lower()}.chr', 'r') as chr:

            return json.loads(open(chr, "r").read())