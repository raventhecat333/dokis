import discord, os, traceback, chalk, json
from discord.ext import commands
from Cogs.config import conf

class maid(commands.AutoShardedBot):
    
    def __init__(self):
        self.prefix = commands.when_mentioned_or(conf.prefix1,conf.prefix2)
        super().__init__(command_prefix=self.prefix, status=discord.Status.idle, activity=discord.Game(name="Starting Up..."))

        for file in os.listdir("Cogs"):
            if file.endswith(".py"):
                name = file[:-3]
                if name == "config" or name == "checks":
                    pass
                else:
                    try:
                        self.load_extension(f"Cogs.{name}")
                        print(chalk.green(f"Loaded {name}"))
                    except (discord.ClientException, ModuleNotFoundError):
                        print('Failed to load Cog {name}')
                        print(traceback.format_exc())


client = maid()
client.run(conf.token)