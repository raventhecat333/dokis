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

    async def Send(self, obj, textID, ping=None, embed=None):

        if not textID or self.ChrFile["messages"][textID]:
            if obj.guild and obj.channel.permissions_for(self.get_guild(obj.guild.id).me).read_messages:
                if obj.channel.permissions_for(self.get_guild(obj.guild.id).me).send_messages:

                    # CHECK HERE FOR TAMPERATION LEVEL HERE AND DETERMINE TAMPER

                    async with self.get_channel(obj.channel.id).typing():
                        
                        outputText = rstr.xeger(random.choice(self.ChrFile["messages"][textID]["dialogues"]))

                        # TESTING FOR THE PLACEHOLDERS
                        #outputText +=  + "ping - {ping} / author - {author} / author_username - {author_username} / author_nickname - {author_nickname} / author_id - {author_id} / mention - {mention} / mention_username - {mention_username} / mention_nickname - {mention_nickname} / mention_id - {mention_id} / content - {content} / content_clean - {content_clean}"
                        
                        outputText = outputText.replace("{ping}", f"<@!{ping}>")
                        outputText = outputText.replace("{author}", f"{obj.message.author.mention}")
                        outputText = outputText.replace("{author_username}", f"{obj.message.author.name}")
                        outputText = outputText.replace("{author_nickname}", f"{obj.message.author.display_name}")
                        outputText = outputText.replace("{author_id}", f"{obj.message.author.id}")

                        mentions = ""
                        mentionsUsernames = ""
                        mentionsNicknames = ""
                        mentionsIds = ""      

                        for member in obj.message.mentions:
                            mentions += f"{member.mention} "
                            mentionsUsernames += f"{member.name} "
                            mentionsNicknames += f"{member.display_name} "
                            mentionsIds += f"{member.id} "                   
                        
                        outputText = outputText.replace("{mention}", f"{mentions}")
                        outputText = outputText.replace("{mention_username}", f"{mentionsUsernames}")
                        outputText = outputText.replace("{mention_nickname}", f"{mentionsNicknames}")
                        outputText = outputText.replace("{mention_id}", f"{mentionsIds}")
                        outputText = outputText.replace("{content}", f"{obj.message.content.partition(' ')[2]}")
                        outputText = outputText.replace("{content_clean}", f"{obj.message.clean_content.partition(' ')[2]}")

                        await asyncio.sleep(0.4)
                        await self.get_channel(obj.channel.id).send(None if not textID else outputText, embed=embed)

                        if "send" in self.ChrFile["messages"][textID]:

                            await self.GetCharacter(self.ChrFile["messages"][textID]["send"]["to"]).Send(obj, self.ChrFile["messages"][textID]["send"]["id"])


                elif obj.guild:

                    if not obj.author.bot:

                        await self.get_user(obj.author.id).send(f"I'm so sorry! But it appears {obj.guild.name} lacks the permissions to let me send messages at {obj.channel.name}!", embed=embed)

    async def DetectEveryoneMention(self, sender):
        if re.search("@(everyone|here)",sender.message.content):
            await self.Send(sender, "everyone")
            return True
        return False