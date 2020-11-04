import asyncio, discord, importlib, json, os, re, rstr, sqlite3, sre_yield, traceback
from discord.ext import commands
from loop import loop

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

    def GetCharacter(self, Name):

        return next(character for character in loop.characters if character.ChrFile["about"]["name"] == Name)

    async def Send(self, obj, text):

        if not obj.guild or obj.channel.permissions_for(obj.guild.me).send_messages:

            async with obj.channel.typing():

                await asyncio.sleep(0.4)
                await obj.channel.send(message, embed=embed)

        elif obj.guild:

            if not obj.author.bot:

                await obj.author.send(f"I'm so sorry! But it appears {obj.guild.name} lacks the permissions to let me send messages at {obj.channel.name}!", embed=embed)

    async def Recieve(self, obj, character, textID):
        #by detecting textID from character, we can interact and send another recieve to the next in line of a bot conversation
        return
