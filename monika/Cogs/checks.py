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


class dev_only(commands.CommandError):# This creates the dev_only error which is used in Error.py
    pass


def dev():# This check will check if the command is being executed by a developer whose id is in the dev_id list in the config file, if not then we will throw an error, else not then run the command ( @checks.dev() )
    def predicate(ctx):
        if ctx.author.id in conf.admins:
            return True
        else:
            raise dev_only
    return commands.check(predicate)

def test(enabled=0,admin=0,developer=0):
    def predicate(ctx):
        if developer is 1 and ctx.author.id in conf.admins:
            return True
        if admin is 1:
            return True
        if enabled is 1:
            return True
        else:
            print("Hey that's not right...")
            return False
    return commands.check(predicate)