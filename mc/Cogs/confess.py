import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf


class Confess(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.command()
    @client.guild_only()
    async def confess(self, ctx):
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)
        await ctx.send(f"*starts to blush* Ok, I'll admit it <@{ctx.author.id}>, I love you!")


def setup(bot):
    bot.add_cog(Confess(bot))