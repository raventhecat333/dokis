import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Ask(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def shard(self,ctx): 
        if conf.sharding is False:
            await ctx.send("Sorry but this command only works while Sharding!")
        elif conf.sharding is True:
            await ctx.send(f"You're on **Shard {ctx.guild.shard_id}**.")


def setup(bot):
    bot.add_cog(Ask(bot))
