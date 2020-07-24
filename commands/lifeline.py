import discord
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Lifeline(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def lifeline(self,ctx):
        await self.bot.send(ctx, self.bot.character.lifeline())

def setup(bot):
    bot.add_cog(Lifeline(bot))

def check(character):
    return hasattr(character, "lifeline")