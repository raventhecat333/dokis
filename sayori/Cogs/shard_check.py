import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Ask(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def shard(self,ctx): # we make arg1 so we can have the command as this "n_ask my dad is in jail lmao" and it will obviously respond, if your missing the "answer arg" which comes after the command then the command will obviously not run
        if conf.sharding is False:
            await ctx.send("Sorry but this command only works while Sharding!")
        elif conf.sharding is True:
            await ctx.send(f"You're on **Shard {ctx.guild.shard_id}**.")


def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Ask(bot))
