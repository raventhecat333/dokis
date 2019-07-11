import discord, asyncio, json, discord.utils
from discord.ext import commands
from Cogs.config import conf
#Some imports 

#this is where stuff like @checks.is_dev is made, simply put if your id matches the one on a string the command will work right, else nono


class dev_only(commands.CommandError):# This creates the dev_only error which is used in Error.py
    pass


def dev():# This check will check if the command is being executed by a developer whose id is in the dev_id list in the config file, if not then we will throw an error, else not then run the command ( @checks.dev() )
    def predicate(ctx):
        if ctx.author.id in conf.admins:
            return True
        else:
            raise dev_only
    return commands.check(predicate)

