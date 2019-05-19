import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Tickle(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    #A test command to see if the "Act" function is working properly as intended

    @client.command(enabled=False)
    async def act_test(self,ctx): 
        if ctx.guild.id in conf.act1:
            await ctx.send("I'm on act1 mode")
        elif ctx.guild.id in conf.act2:
            await ctx.send("I'm on act2 mode")
        else:
            await ctx.send("I'm not in the list ")


def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Tickle(bot))
