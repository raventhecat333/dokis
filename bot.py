import asyncio, discord, importlib, json, os, random, re, rstr, sqlite3, sre_yield, traceback
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

    async def Send(self, obj, textID, embed=None):

        if not textID or self.ChrFile["messages"][textID]:
            if not obj.guild or obj.channel.permissions_for(obj.guild.me).send_messages:

                # CHECK HERE FOR TAMPERATION LEVEL HERE AND DETERMINE TAMPER

                async with obj.channel.typing():

                    await asyncio.sleep(0.4)
                    await obj.channel.send(None if not textID else rstr.xeger(random.choice(self.ChrFile["messages"][textID]["dialogues"])), embed=embed)

                    if "send" in self.ChrFile["messages"][textID]:

                        await self.GetCharacter(self.ChrFile["messages"][textID]["send"]["to"]).Send(obj, self.ChrFile["messages"][textID]["send"]["id"])


            elif obj.guild:

                if not obj.author.bot:

                    await obj.author.send(f"I'm so sorry! But it appears {obj.guild.name} lacks the permissions to let me send messages at {obj.channel.name}!", embed=embed)
