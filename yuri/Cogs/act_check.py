import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Act_check(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    #A test command to see if the "Act" function is working properly as intended

    @client.command()
    @client.guild_only()
    async def act(self,ctx): 
        if ctx.guild.id not in conf.act2:
            await ctx.send("I'm on act1.")
        elif ctx.guild.id in conf.act2:
            await ctx.send("I'm on act2.")
        else:
            await ctx.send("Ok, this is a bug. Can you report this for me? Thanks. (Also report that this is an ELSE statement)")


def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Act_check(bot))
