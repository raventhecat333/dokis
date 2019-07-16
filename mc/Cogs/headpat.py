import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Headpat(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    async def headpat(self,ctx):   
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)
        await ctx.send("Stop it!")


def setup(bot):
    bot.add_cog(Headpat(bot))
