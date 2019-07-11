import discord, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Rename(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.command()
    @client.guild_only()
    async def rename(self, ctx, name):
        if not ctx.message.channel.permissions_for(ctx.message.author.guild.me).change_nickname:
            await ctx.send("I can't change my own nickname for some reason.")
            return
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)
        await ctx.message.author.guild.me.edit(nick=f"{name}")
        await ctx.send(f"Ok, guess {name} is my name now.")


def setup(bot):
    bot.add_cog(Rename(bot))