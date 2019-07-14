import discord, asyncio, json, discord.utils
from discord.ext import commands
from Cogs.config import conf
#Some imports 
nol=conf.norm
sol=conf.suc
eol=conf.err
wol=conf.warn
ver=conf.version
#this is where stuff like @checks.is_dev is made, simply put if your id matches the one on a string the command will work right, else nono


class blank(commands.CommandError):# If we get an error and we don't want any output at all then we can use this to get that result
    pass


def dev():# This check will check if the command is being executed by a developer whose id is in the dev_id list in the config file, if not then we will throw an error, else not then run the command ( @checks.dev() )
    def predicate(ctx):
        if ctx.author.id in conf.admins:
            return True
        else:
            raise blank
    return commands.check(predicate)

