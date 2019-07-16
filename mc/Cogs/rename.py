import discord, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Rename(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.command()
    async def rename(self, ctx, name):
        if not ctx.message.channel.permissions_for(ctx.message.author).manage_nicknames:
            await ctx.send("You don't have the proper permissions to change my name.")
            return
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)
        await ctx.message.author.guild.me.edit(nick=f"{name}")
        await ctx.send(f"Ok, guess {name} is my name now.")


def setup(bot):
    bot.add_cog(Rename(bot))