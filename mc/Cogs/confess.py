import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf


class Confess(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.command()
    async def confess(self, ctx, *, arg=None):
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)
        if arg is None:
            await ctx.send(f"*starts to blush* Ok, I'll admit it <@{ctx.author.id}>, I love you!")
        elif arg == f"<@{conf.sayori_id}>":
            await ctx.send("Hey, Sayori?")
        elif arg == f"<@{conf.monika_id}>":
            await ctx.send("Monika?")
        elif arg == f"<@{conf.yuri_id}>":
            await ctx.send("I-I love you, Yuri.")
        elif arg == f"<@{conf.natsuki_id}>":
            await ctx.send("H-Hey, Natsuki?")
        else:
            await ctx.send(f"*starts to blush* Ok, I'll admit it {arg}, I love you!")

def setup(bot):
    bot.add_cog(Confess(bot))
