import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Ping(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def ping(self, ctx):
        e = discord.Embed(colour=conf.norm)
        e.add_field(name='Pong! :ping_pong:', value=f'`{round(self.b.latency * 1000)}ms`', inline=False)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Ping(bot))
