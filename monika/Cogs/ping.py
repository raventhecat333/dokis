import discord, random, asyncio
from discord.ext import commands as client
#Imports


class Ping(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.green()
        )
        
        embed.add_field(name='Pong! :ping_pong:', value=f'`{round(self.b.latency * 1000)}ms`', inline=False)
        
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Ping(bot))
