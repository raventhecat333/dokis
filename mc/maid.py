import discord, os, traceback, json
from discord.ext import commands

class maid(commands.AutoShardedBot):
    
    def __init__(self):
        self.config = json.loads(open('../config.json', 'r').read())
        self.prefix = commands.when_mentioned_or(self.config[prefix1],self.config[prefix2])
        super().__init__(command_prefix=self.prefix, status=discord.Status.idle, activity=discord.Game(name="Starting Up..."))

        for file in os.listdir("Cogs"):
            if file.endswith(".py"):
                name = file[:-3]
                try:
                    self.load_extension(f"{Cogs.name}")
                except (discord.ClientException, ModuleNotFoundError):
                    print('Failed to load Cog {name}')
                    print(traceback.format_exc())


client = maid()
config = json.loads(open('../config.json', 'r').read())
client.run(config.get('sayori_token'))