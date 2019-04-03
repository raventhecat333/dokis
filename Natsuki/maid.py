import discord, os, traceback
from discord.ext import commands
from os import listdir
from os.path import isfile, join
from Cogs.config import conf
#Import some important modules
if conf.sharding is True:
    client = commands.AutoShardedBot(command_prefix=conf.prefix, status=discord.Status.do_not_disturb, activity=discord.Game(name="Starting..."), shard_count=2, shard_ids=(0, 1)) # Defining what our prefix for the bot will be
elif conf.sharding is False:
    client = commands.Bot(command_prefix=conf.prefix, status=discord.Status.do_not_disturb, activity=discord.Game(name="Starting...")) # Defining what our prefix for the bot will be


cogd = conf.cogd

if __name__ == '__main__': # Load every file that have a .py extension in the Cogs folder
    for extension in [f.replace('.py', '') for f in listdir(cogd) if isfile(join(cogd, f))]:
        try:
            client.load_extension(cogd + "." + extension) # Here's were we load them
            print(f"Loaded {extension}")
        except (discord.ClientException, ModuleNotFoundError): # Oh fuck something happened lets reppoooooorrrrrt it!!!!111111!!!!!!
            print(f'\nFailed to load extension {extension} with the Traceback bellow.')
            print("\n")
            traceback.print_exc()#If it fails then give us a traceback
            print("\n")

client.run(conf.token) # Login via our token inside of the config file
