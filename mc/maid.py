import discord, os, traceback, chalk, sys
from discord.ext import commands
from Cogs.config import conf
#Import some important modules

if conf.test_mode is True:
    print(chalk.red('''---------------------Testing Mode--------------------- 
Warning!

You are currently running the Pythonic Doki Bot's in testing mode!
Please disable testing mode before launching this code. 
If you are unsure how to turn testing mode off:

1. Go to the config
2. Find "test_mode ="
3. Change "False" to "True"
---------------------Testing Mode--------------------- \n'''))
else:
    pass


async def prefix(bot, message):
  return [conf.prefix1, conf.prefix2]  # or a list, ["pre1","pre2"]


if conf.sharding is True:
    client = commands.AutoShardedBot(command_prefix=prefix, status=discord.Status.idle, activity=discord.Game(name="Starting Up...")) # Defining what our prefix for the bot will be
elif conf.sharding is False: #Just so cheezy's pc doesn't melt.
    client = commands.Bot(command_prefix=prefix, status=discord.Status.idle, activity=discord.Game(name="Starting Up...")) # Defining what our prefix for the bot will be


Cogs = conf.cogd

if __name__ == '__main__': # Load every file that have a .py extension in the Cogs folder
    for file in os.listdir(conf.cogd):
        if file.endswith(".py"):
            name = file[:-3]
            if name == "config" or name == "checks":
                pass
            else:
                try:
                    client.load_extension(f"Cogs.{name}")
                    print(chalk.green(f"[INFO] Loaded {name}"))
                except (discord.ClientException, ModuleNotFoundError):
                    print('[ERROR] Failed to load Cog {name}')
                    print(traceback.format_exc())
                    continue

client.run(conf.token) # Login via our token inside of the config file
